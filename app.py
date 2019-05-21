import os
from flask import Flask, request, render_template, url_for, redirect
from autonomous_ldap_register.csv_module import read_csv_file

app = Flask(__name__)


@app.route("/")
def file_front_page():
    return render_template('fileform.html')


@app.route("/handleUpload", methods=['POST'])
def handle_file_upload():
    directory_path = os.getcwd()
    if 'csv-file' in request.files:
        csv_file = request.files['csv-file']
        if csv_file.filename != '':
            file_path = directory_path + '/' + csv_file.filename
            csv_file.save(os.path.join(directory_path + '/', csv_file.filename))
            read_csv_file(file_path)
    return redirect(url_for('file_front_page'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
