# Base image: small and reliable
FROM python:3.11-slim

# Recommended Python flags
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create app directory
WORKDIR /app

# Install system deps only if you need to compile wheels (commented by default)
# RUN apt-get update && apt-get install -y --no-install-recommends build-essential && \
#     rm -rf /var/lib/apt/lists/*

# 1) Copy only requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2) Copy the rest of the source
COPY . .

# (Optional but good) run as non-root
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Expose web port (for FastAPI demo)
EXPOSE 8000

# Start server (adjust if your app entrypoint differs)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
