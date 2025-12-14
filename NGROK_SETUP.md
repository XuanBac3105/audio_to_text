# Cài Đặt & Sử Dụng NGROK

NGROK cho phép chia sẻ ứng dụng Flask chạy trên máy local của bạn với mọi người qua internet công cộng.

## 📥 Cài Đặt NGROK

### Bước 1: Download
1. Truy cập: https://ngrok.com/download/windows?tab=download
2. Chọn **Windows** 
3. Click download (hoặc download trực tiếp: https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip)

### Bước 2: Giải nén
```bash
# Hoặc dùng PowerShell
Expand-Archive -Path "D:\Downloads\ngrok-v3-stable-windows-amd64.zip" -DestinationPath "D:\audio_to_text"
```

Bạn sẽ có file `ngrok.exe` trong folder `D:\audio_to_text`

### Bước 3: (Tuỳ chọn) Tạo tài khoản ngrok
1. Truy cập: https://dashboard.ngrok.com/signup
2. Đăng ký tài khoản miễn phí
3. Copy **Auth Token** của bạn

### Bước 4: Kết nối Auth Token (nếu có)
```bash
.\ngrok.exe authtoken YOUR_AUTH_TOKEN_HERE
```

## 🚀 Sử Dụng NGROK

### Bước 1: Chạy Flask App
```bash
cd d:\audio_to_text
python app.py
# Hoặc:
cd d:\audio_to_text_api
python app.py
```

Output sẽ là:
```
 * Running on http://127.0.0.1:5000
```

### Bước 2: Mở Terminal mới và chạy NGROK
```bash
cd d:\audio_to_text
.\ngrok.exe http 5000
```

Output sẽ hiển thị:
```
ngrok by @inconshreveable                                    (Ctrl+C to quit)

Session Status                online
Account                       yourname (Plan: Free)
Version                       3.x.x
Region                        us (United States)
Latency                       45ms
Web Interface                 http://127.0.0.1:4040

Forwarding                    https://xxxx-xxxx-xxxx.ngrok.io -> http://localhost:5000
```

### Bước 3: Chia sẻ URL
Copy URL từ dòng `Forwarding`: **https://xxxx-xxxx-xxxx.ngrok.io**

Chia sẻ URL này với ai muốn dùng app của bạn!

## 📝 Ví Dụ Hoàn Chỉnh

**Terminal 1 - Chạy Flask:**
```bash
cd d:\audio_to_text
(venv) python app.py
 * Running on http://127.0.0.1:5000
```

**Terminal 2 - Chạy NGROK:**
```bash
cd d:\audio_to_text
.\ngrok.exe http 5000
# Output:
# Forwarding: https://abc123-def456.ngrok.io -> http://localhost:5000
```

**Terminal 3 - (Tuỳ chọn) Kiểm tra:**
```bash
# Bạn hoặc bạn bè có thể truy cập:
https://abc123-def456.ngrok.io
```

## ⚙️ Các Tùy Chọn Hữu Ích

### Chỉ định subdomain (cần Pro)
```bash
.\ngrok.exe http 5000 -subdomain=my-audio-app
# Output: https://my-audio-app.ngrok.io
```

### Chỉ định region (cần Pro)
```bash
.\ngrok.exe http 5000 -region eu
# Available: us, eu, au, ap, sa, jp, in
```

### Xem traffic
```
http://127.0.0.1:4040
```
Truy cập web interface để xem tất cả requests/responses

## 🔒 Bảo Mật

### Basic Auth (thêm mật khẩu)
```bash
.\ngrok.exe http 5000 -auth "user:password"
```

### IP Whitelist (chỉ cho phép IP nhất định)
```bash
.\ngrok.exe http 5000 -allow-ip 192.168.1.100
```

## 🎯 Workflow Hàng Ngày

```bash
# 1. Mở 2 terminal
# Terminal 1:
cd d:\audio_to_text
python app.py

# Terminal 2:
cd d:\audio_to_text
.\ngrok.exe http 5000

# 2. Copy URL: https://xxxx.ngrok.io
# 3. Chia sẻ với người khác
# 4. Họ dùng app của bạn online!
```

## ⏱️ Thời Gian Sống của URL

- **Miễn phí**: URL thay đổi mỗi lần restart ngrok
- **Pro ($5/month)**: URL cố định

## 🆘 Troubleshooting

### "error=ERR_NGROK_110 Unable to connect"
→ Kiểm tra Flask app đang chạy trên port 5000

### "Tunnel error: 401 Unauthorized"
→ Auth token sai hoặc chưa setup, chạy: `.\ngrok.exe authtoken YOUR_TOKEN`

### "error=ERR_NGROK_104 Connection refused"
→ Port 5000 bị chiếm, thay đổi port:
```bash
python app.py  # Thay đổi port trong app.py
.\ngrok.exe http 5001  # Hoặc chạy ngrok trên port khác
```

## 📚 Tài Liệu Thêm

- NGROK Docs: https://ngrok.com/docs
- Getting Started: https://ngrok.com/docs/getting-started
- API Reference: https://ngrok.com/docs/api

## 💡 Mẹo

1. **Chạy trên background**: Dùng `start ngrok.exe http 5000` để chạy ngrok mà không block terminal
2. **Multiple ports**: Có thể forward nhiều port: `.\ngrok.exe http 5000 http 8000`
3. **Inspect traffic**: Truy cập `http://localhost:4040` để debug requests
4. **Disable browser**: Thêm `-bind-tls=false` nếu gặp SSL issues

---

**Sẵn sàng chia sẻ app của bạn! 🎉**
