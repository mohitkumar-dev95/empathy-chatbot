FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Upgrade pip to fix known hash checking bugs on slow networks
RUN pip install --upgrade pip

# Pre-install the failing dependencies from the official PyPI index
RUN pip install --retries 10 --default-timeout=1000 --no-cache-dir mpmath sympy

# Install CPU-only PyTorch
RUN pip install --retries 10 --default-timeout=1000 --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Copy the requirements file
COPY requirements.txt .

# Install remaining dependencies
RUN pip install --retries 10 --default-timeout=1000 --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the correct port for the FastAPI app
EXPOSE 8000

# Command to run the application using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
