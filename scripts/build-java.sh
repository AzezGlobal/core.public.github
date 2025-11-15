#!/bin/bash
# Build script for Java components

set -e

echo "Building Core Public GitHub - Java Components"
echo "=============================================="

# Check if Gradle wrapper exists, if not use system gradle
if [ -f "./gradlew" ]; then
    GRADLE_CMD="./gradlew"
else
    GRADLE_CMD="gradle"
fi

echo "Cleaning previous builds..."
$GRADLE_CMD clean

echo "Compiling Java sources..."
$GRADLE_CMD compileJava

echo "Running tests..."
$GRADLE_CMD test

echo "Building artifacts..."
$GRADLE_CMD build

echo ""
echo "Build completed!"
echo "Artifacts location: build/libs/"
