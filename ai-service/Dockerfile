# Use Python base image
FROM python:3.12-slim

# Prevent .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Show logs immediately
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose FastAPI port
EXPOSE 8001

# Run AI service
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]
