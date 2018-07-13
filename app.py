import os
from flask import Flask, request, redirect, url_for,flash,render_template,send_from_directory, jsonify
from werkzeug.utils import secure_filename
#from classification import neural
import Testing1

UPLOAD_FOLDER = '/home/ryanazrian/Desktop/PCD/Project/code/CodeFix/WEB/temp'
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api', methods=['GET', 'POST'])
def uploads_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            matang, berat = Testing1.imageProcess(filename)
            hasil  = [matang, berat]
            #return render_template('hasil/index.html',filename=filename, berhasil="1",kematangan=matang, berat=berat,file_url=matang)
            # return  '{} {}'.format(matang, berat)
            return jsonify(matang, berat)
    return render_template('upload/index.html',)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            matang, berat = Testing1.imageProcess(filename)
            hasil  = [matang, berat]
            return render_template('hasil/index.html',filename=filename, berhasil="1",kematangan=matang, berat=berat,file_url=matang)
            # return  '{} {}'.format(matang, berat)
            # return jsonify(matang, berat)
    return render_template('upload/index.html',)


@app.route('/ambil/<filename>', methods=['GET', 'POST'])
def show_file(filename):
    return send_from_directory('temp/', filename,as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)