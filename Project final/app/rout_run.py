from flask import Flask, render_template, request, send_file
from utils.versteigerungskalender import verstei
from utils.insolvenzbekanntmachungen import Insolvenzbekanntmachungen
from utils.dealone import deal
from waitress import serve
from utils.tools import save_to_excel,reverse_date_format

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        site = request.form.get('site')
        

        if site == 'versteigerungskalender':
            sector = request.form.get('sector')
            keywords = request.form.get('keywords')
            data = verstei(keywords, sector)
            filename = "verstei_data.xlsx"
            file = save_to_excel(data, filename)
            return render_template('down.html', filename=file)
        
        if site == "Insolvenzbekanntmachungen":
            keywords = request.form.get('keywords')
            dateStart = reverse_date_format(request.form.get('dateStart'))
            dateEnd = reverse_date_format(request.form.get('dateEnd'))
            data = Insolvenzbekanntmachungen(keywords,dateStart,dateEnd)
            filename = "insolv_data.xlsx"
            file = save_to_excel(data, filename)
            return render_template('down.html', filename=file)
        
        if site == "dealone":
            keywords = request.form.get('keywords')
            data = deal(keywords)
            filename = "DealOne_data.xlsx"
            file = save_to_excel(data, filename)
            return render_template('down.html', filename=file)

    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    path = filename  # Assuming the file is in the current working directory
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
