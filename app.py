from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import os
from datetime import datetime

app = Flask(__name__, static_folder='static')
app.secret_key = 'your-secret-key-here'  # Required for flash messages

# Simulated storage (in a real app, this would be a database)
files = []

@app.route('/')
def index():
    return render_template('index.html', files=files)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))
    
    # Simulate file storage
    file_info = {
        'name': file.filename,
        'upload_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'size': '1MB'  # Simulated size
    }
    files.append(file_info)
    flash('File uploaded successfully!')
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['POST'])
def update_file(index):
    if 0 <= index < len(files):
        new_name = request.form.get('new_name')
        if new_name:
            files[index]['name'] = new_name
            flash('File updated successfully!')
        else:
            flash('Invalid file name')
    else:
        flash('File not found')
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_file(index):
    if 0 <= index < len(files):
        files.pop(index)
        flash('File deleted successfully!')
    else:
        flash('File not found')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 