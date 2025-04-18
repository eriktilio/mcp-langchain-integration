# Generated by https://smithery.ai. See: https://smithery.ai/docs/config#dockerfile
FROM python:3.11-slim

# Install dependencies
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose any ports if needed
# No ports to expose for stdio transport

# Start the MCP server
CMD ["python", "server.py"]
