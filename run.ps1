# Chạy Audio Transcriber với cache model
# Lần đầu: tải model ~1.42GB (2-3 phút)
# Lần sau: model đã cache, chạy ngay

docker run --rm `
  -p 5000:5000 `
  -v D:/audio_to_text/whisper_cache:/root/.cache/whisper `
  audio2text

# Mở browser: http://localhost:5000
