# .devcontainer/Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /workspace

# Copy the FastAPI application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "hello:app", "--host", "0.0.0.0", "--port", "8000"]