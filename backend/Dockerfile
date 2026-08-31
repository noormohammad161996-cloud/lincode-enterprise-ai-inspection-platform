# Use official Python image
FROM python:3.12-slim

# Prevent Python from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Show logs immediately
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install curl for Docker health checks
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Copy application source code
COPY . .

# Create a non-root user named appuser
RUN useradd -m appuser

# Give ownership of the application folder to appuser
RUN chown -R appuser:appuser /app

# Switch from root to appuser
USER appuser

# Expose FastAPI port
EXPOSE 8000

# Docker checks this endpoint every 30 seconds
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
CMD curl -f http://localhost:8000/health/ || exit 1

# Start FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]