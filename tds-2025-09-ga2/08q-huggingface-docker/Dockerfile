# Use a small python image
FROM python:3.11-slim

# Create a user with UID 1000
RUN useradd -m -u 1000 user

# Set working dir
WORKDIR /home/user/app

# Copy only requirements first to leverage layer caching
COPY --chown=user requirements.txt ./requirements.txt

# Install system deps (if any) and python deps
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy rest of the source
COPY --chown=user . .

# Switch to non-root user to match Spaces runtime
USER user
ENV HOME=/home/user
ENV PATH=/home/user/.local/bin:$PATH

# Application port expected by the Space
ENV APP_PORT=7423
EXPOSE 7423

# Run the app on the configured port
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7423"]