FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    ca-certificates \
  && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=7002

WORKDIR $HOME
USER user

RUN git clone --depth 1 https://github.com/LUC4N3X/Torrenthan app
WORKDIR $HOME/app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 7002
CMD ["sh","-c","uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
