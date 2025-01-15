# Use the Spark base image
FROM spark:latest

# Update package list and install iputils-ping
USER root
RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*

# Switch back to the default Spark user
USER spark

# Set the working directory (optional, modify if needed)
WORKDIR /opt/spark

# Default command (keeps Spark's behavior)
CMD ["/bin/bash"]
