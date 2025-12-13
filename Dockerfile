FROM python:3.10-slim

RUN apt-get update && apt-get install -y ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy files
COPY app.py .
COPY templates templates/

# Cài PyTorch CPU-only
RUN pip install --no-cache-dir \
    torch==2.1.2+cpu \
    torchvision==0.16.2+cpu \
    torchaudio==2.1.2+cpu \
    -f https://download.pytorch.org/whl/torch_stable.html

# Fix numpy version
RUN pip install --no-cache-dir "numpy<2"

# Cài whisper và Flask
RUN pip install --no-cache-dir openai-whisper flask

EXPOSE 5000

CMD ["python", "app.py"]
