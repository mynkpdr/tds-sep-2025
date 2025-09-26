FROM python:3.11-slim
# Set working directory
WORKDIR /app
# Typically, you would use `COPY . .` to copy files from the host machine,
# but here we're just using a simple script.
RUN echo 'print("Hello, world!")' > app.py
# Run the script
CMD ["python", "app.py"]