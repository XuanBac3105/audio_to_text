from flask import Flask, render_template, request, jsonify, send_file
import whisper
import os
import re
from werkzeug.utils import secure_filename
import threading
import queue

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp/uploads'
app.config['OUTPUT_FOLDER'] = '/tmp/outputs'
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

# Dictionary sửa lỗi phổ biến
corrections = {
    "dung truyền": "rung chuyển",
    "chiến trưởng": "chiến trường",
    "bông kê": "boong kê",
    "trang trì": "trang bị",
    "miền chống": "mìn chống",
    "phủ ký": "phủ kín",
    "cánh dừng": "cánh rừng",
    "dậy sống": "dậy sóng",
    "cơn rông": "cơn dông",
    "tây nguyên": "Tây Nguyên",
}

def correct_text(text):
    for wrong, right in corrections.items():
        text = re.sub(wrong, right, text, flags=re.IGNORECASE)
    return text

# Global variables
models_cache = {}
log_queue = queue.Queue()
processing_status = {"running": False, "current": 0, "total": 0}

def load_model(model_size):
    if model_size not in models_cache:
        models_cache[model_size] = whisper.load_model(model_size)
    return models_cache[model_size]

def process_files(files, language, model_size, output_name):
    global processing_status
    processing_status["running"] = True
    processing_status["total"] = len(files)
    
    log_queue.put(f"Files selected: {len(files)}")
    log_queue.put(f"Model: {model_size} | Language: {language}")
    log_queue.put(f"Số file: {len(files)}")
    log_queue.put("Bắt đầu transcribe...")
    
    model = load_model(model_size)
    output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_name)
    
    with open(output_path, "w", encoding="utf-8") as out:
        for idx, file_path in enumerate(files, 1):
            processing_status["current"] = idx
            filename = os.path.basename(file_path)
            log_queue.put(f"Đang xử lý {idx}/{len(files)}: {filename}")
            
            result = model.transcribe(file_path, language=language if language != "auto" else None)
            text = result["text"].strip()
            corrected = correct_text(text)
            out.write(corrected + "\n\n")
    
    log_queue.put("DONE")
    processing_status["running"] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        return jsonify({"error": "No files"}), 400
    
    files = request.files.getlist('files')
    language = request.form.get('language', 'vi')
    model_size = request.form.get('model', 'small')
    output_name = request.form.get('output_name', 'output.txt')
    
    saved_files = []
    for file in files:
        if file.filename:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            saved_files.append(filepath)
    
    # Start processing in background
    thread = threading.Thread(target=process_files, args=(saved_files, language, model_size, output_name))
    thread.start()
    
    return jsonify({"message": "Processing started", "files": len(saved_files)})

@app.route('/logs')
def get_logs():
    logs = []
    while not log_queue.empty():
        logs.append(log_queue.get())
    return jsonify({"logs": logs, "status": processing_status})

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join(app.config['OUTPUT_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
