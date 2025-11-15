# Multi-stage Dockerfile for Core Public GitHub frameworks

# Stage 1: Python environment
FROM python:3.11-slim as python-base

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy Python requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY examples/ ./examples/

# Stage 2: Java environment (optional)
FROM openjdk:17-slim as java-base

WORKDIR /app

# Install Gradle
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Copy Gradle files
COPY build.gradle .
COPY gradle/ ./gradle/
COPY gradlew .

# Download dependencies
RUN chmod +x gradlew && \
    ./gradlew dependencies --no-daemon || true

# Copy source code
COPY src/ ./src/

# Build Java components
RUN ./gradlew build --no-daemon

# Stage 3: Final runtime image
FROM python:3.11-slim

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy Python dependencies and code from python-base
COPY --from=python-base /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=python-base /app/src ./src
COPY --from=python-base /app/examples ./examples

# Copy Java artifacts from java-base (if needed)
COPY --from=java-base /app/build/libs ./libs

# Create non-root user
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

USER appuser

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src/main

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Default command
CMD ["python", "-m", "pytest", "src/test/", "-v"]
