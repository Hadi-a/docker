# stable official Java runtime base image

FROM openjdk:17-jdk-alpine

# working directory created on container

WORKDIR /app

# Copy source code into the container from host/source location
# COPY . .
COPY src/Main.java /app/Main.java

# Compile the Java code
RUN javac Main.java

# Run the Java application when the container starts
CMD ["java","Main"]
