# Audio to Text Converter

Công cụ chuyển đổi audio sang text sử dụng OpenAI Whisper, hỗ trợ nhiều ngôn ngữ.

## Tính năng

- ✅ Chuyển đổi audio sang text với độ chính xác cao
- ✅ Hỗ trợ nhiều ngôn ngữ: Tiếng Việt, Tiếng Anh, Tiếng Nhật, Tiếng Thái
- ✅ Web interface đơn giản, dễ sử dụng
- ✅ Tự động sửa lỗi chính tả tiếng Việt
- ✅ Upload và tải xuống file text
- ✅ Theo dõi tiến trình real-time

## Công nghệ

- Python 3.10
- OpenAI Whisper (Medium model)
- Flask
- Docker
- PyTorch CPU

## Cách sử dụng Local

```bash
# Build Docker image
docker build -t audio-to-text .

# Chạy container
docker run --rm -p 5000:5000 -v $(pwd)/whisper_cache:/root/.cache/whisper audio-to-text
```

Truy cập: http://localhost:5000

## Deploy trên Railway

1. Fork repo này
2. Kết nối với Railway
3. Deploy tự động
4. Nhận public URL

## Ngôn ngữ hỗ trợ

- vi - Tiếng Việt
- en - English
- ja - 日本語
- th - ภาษาไทย
- auto - Tự động phát hiện
