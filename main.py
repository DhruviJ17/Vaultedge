import os
from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from rotator import rotate_pdf_page

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = 'static'
app.config['UPLOAD_FOLDER1'] = 'result'

@app.route('/')
def index():
    return render_template('main.html')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        page_number = request.form['Page Number']
        angle = request.form['Angle']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            print(file)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            filepath_output = os.path.join(app.config['UPLOAD_FOLDER1'], filename)
            file.save(filepath)
            pdf_in = file
            pdf_writer = rotate_pdf_page(pdf_in, page_number, angle)
            pdf_out = open(filepath_output, 'wb')
            pdf_writer.write(pdf_out)
            pdf_out.close()
    return render_template('main.html', filename = filename)


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()