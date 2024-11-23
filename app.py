from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
import os
from fpdf import FPDF
import docx
import zipfile

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'docx'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max 16 MB

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Convert DOCX to PDF
        pdf_filename = convert_docx_to_pdf(file_path)

        # Get metadata
        metadata = get_file_metadata(file_path)

        return jsonify({
            "message": "File uploaded successfully",
            "pdf_filename": pdf_filename,
            "metadata": metadata
        })
    else:
        return jsonify({"error": "Invalid file type. Only .docx allowed."}), 400

@app.route('/download/<pdf_filename>')
def download_file(pdf_filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], pdf_filename), as_attachment=True)

def convert_docx_to_pdf(docx_file):
    # Simple conversion of DOCX content to PDF using FPDF
    doc = docx.Document(docx_file)
    pdf_filename = docx_file.rsplit('.', 1)[0] + '.pdf'
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for para in doc.paragraphs:
        pdf.multi_cell(0, 10, para.text)

    pdf.output(pdf_filename)
    return pdf_filename

def get_file_metadata(file_path):
    # Simple metadata extraction
    file_stats = os.stat(file_path)
    return {
        'filename': os.path.basename(file_path),
        'size': file_stats.st_size,
        'last_modified': file_stats.st_mtime
    }

if __name__ == "__main__":
    app.run(debug=True)
