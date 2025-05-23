# Baza: gotowy obraz PyTorch CPU (Torch + TorchVision + Facenet kompatybilne)
FROM pytorch/pytorch

# Instalacja bibliotek systemowych wymaganych przez opencv i pillow
RUN apt-get update && apt-get install -y \
    libgl1 libglib2.0-0 libsm6 libxext6 libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj tylko requirements.txt, by skorzystać z cache
COPY requirements.txt .

# Instalacja zależności pip (torch i torchvision są już w bazie!)
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj cały projekt
COPY . .

# Domyślne uruchomienie
CMD ["python", "src/main.py"]
