# Google Gemini API Setup Guide 🤖

## Cách lấy Google Gemini API Key (Miễn phí!)

### Bước 1: Truy cập Google AI Studio
1. Mở: https://ai.google.dev
2. Hoặc đi trực tiếp: https://makersuite.google.com/app/apikey

### Bước 2: Đăng nhập Google Account
- Nếu chưa có, hãy tạo một Google Account
- Đăng nhập bằng tài khoản Google của bạn

### Bước 3: Tạo API Key
1. Click "Create API Key" (Tạo khóa API)
2. Chọn "Create API key in new project" 
3. Google sẽ tự động tạo key cho bạn
4. Copy key đó (dạng: `AIzaSyD...`)

### Bước 4: Cấu hình .env
1. Trong folder `audio_to_text`, tìm file `.env` (nếu chưa có thì tạo mới)
2. Thêm dòng sau:
```
GOOGLE_GEMINI_API_KEY=AIzaSyD_xxxxxxxxxxxxxx
```
3. Thay `AIzaSyD_xxxxxxxxxxxxxx` bằng API key thực của bạn
4. **Lưu file .env**

### Bước 5: Cài đặt dependencies
Chạy lệnh này trong folder `audio_to_text`:
```bash
pip install -r requirements.txt
```

### Bước 6: Chạy ứng dụng
```bash
python app.py
```

## Chi tiết hơn

### Quyền lợi của Gemini API miễn phí:
- ✅ 60 request/phút (Sufficient cho transcription + improvement)
- ✅ Hoàn toàn miễn phí
- ✅ Không cần credit card
- ✅ Sử dụng mô hình `gemini-pro` - model mạnh nhất

### Cách sử dụng:
1. Sau khi cấu hình .env, upload file audio
2. Ứng dụng sẽ:
   - 🎤 Transcribe từ faster-whisper
   - 🤖 Improve text bằng Gemini (sửa chính tả, ngữ pháp)
   - 📥 Download kết quả

### Nếu API key không tìm thấy:
- App sẽ hiển thị cảnh báo: `⚠️ Gemini API key không tìm thấy`
- Text gốc từ Whisper sẽ được trả về mà không improve

### Troubleshooting:
1. **"API key không hợp lệ"** → Kiểm tra lại API key trong .env
2. **"Rate limit exceeded"** → Chờ một chút rồi thử lại (60 requests/phút)
3. **".env file not found"** → Tạo file `.env` trong folder `audio_to_text`

## Link hữu ích:
- Google AI Studio: https://ai.google.dev
- API Key Manager: https://makersuite.google.com/app/apikey
- Gemini Documentation: https://ai.google.dev/docs
