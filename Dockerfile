FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install uv using pipx
RUN apt-get update && apt-get install -y curl && \
    pip install --no-cache-dir pipx && \
    pipx install uv && \
    pipx ensurepath

ENV PATH="/root/.local/bin:$PATH"

# Copy project metadata
COPY pyproject.toml /app/

# Compile and install dependencies with uv, using --system flag
RUN uv pip compile --system pyproject.toml -o requirements.txt && \
    uv pip install --system -r requirements.txt

# Copy the rest of the code
COPY . /app

CMD ["python", "main.py"]