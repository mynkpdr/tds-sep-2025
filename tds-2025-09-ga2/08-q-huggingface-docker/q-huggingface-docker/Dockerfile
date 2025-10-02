# Use a slim Python base image
FROM python:3.11-slim

# Create a non-root user with UID 1000
RUN useradd -m -u 1000 user

# Set the working directory
WORKDIR /home/user/app

# Copy requirements and install dependencies as the root user first
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY --chown=user . .

# Switch to the non-root user
USER user

# Set environment variable for the port and expose it
ARG APP_PORT=7423
ENV APP_PORT=${APP_PORT}
EXPOSE 7423

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7423"]