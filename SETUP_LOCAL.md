# Audio to Text Transcriber - Setup Local

## 1. Tạo Virtual Environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

## 2. Cài đặt Dependencies
```bash
pip install -r requirements.txt
```

## 3. Cài FFmpeg (Bắt buộc)
### Windows (Chocolatey):
```bash
choco install ffmpeg -y
```

### Windows (Manual):
- Download từ: https://ffmpeg.org/download.html
- Add folder chứa ffmpeg vào System PATH

### macOS:
```bash
brew install ffmpeg
```

### Linux (Ubuntu):
```bash
sudo apt-get install ffmpeg
```

## 4. Khôi phục Model Cache
- Giải nén file `whisper_cache.zip` vào folder `audio_to_text/`
- Model sẽ nằm tại: `D:\audio_to_text\whisper_cache\`

## 5. Chạy App
```bash
python app.py
```
Truy cập: http://localhost:5000

## Notes
- Lần đầu sẽ load model từ cache (~30 giây)
- Cần ~4-6GB RAM cho Large model
- Upload tối đa 20 file cùng lúc
