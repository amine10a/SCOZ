from flask import Flask, render_template, request, send_file
from utils.versteigerungskalender import verstei, save_to_excel_verstei
from utils.unternehmensregister import unter, save_to_excel_unternehmensregister
from waitress import serve

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        site = request.form.get('site')
        sector = request.form.get('sector')
        keywords = request.form.get('keywords')

        if site == 'versteigerungskalender':
            data = verstei(keywords, sector)
            filename = "verstei_data.xlsx"
            file = save_to_excel_verstei(data, filename)
            return render_template('index.html', filename=file)
        
        if site == "unternehmensregister":
            data = unter(keywords, sector)
            filename = "unternehmensregister_data.xlsx"
            file = save_to_excel_unternehmensregister(data, filename)
            return render_template('index.html', filename=file)
        
        if site == "firminform":
            data = unter(keywords, sector)
            filename = "firminform_data.xlsx"
            file = save_to_excel_unternehmensregister(data, filename)
            return render_template('index.html', filename=file)

    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    path = filename  # Assuming the file is in the current working directory
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
