from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_website = request.form['selectWebsite']

        # Process based on selected website
        if selected_website == '1':
            input1 = request.form['input1']
            # Process input1 data
            return f"Selected Website: One, Input 1: {input1}"
        elif selected_website == '2':
            input2 = request.form['input2']
            input3 = request.form['input3']
            # Process input2 and input3 data
            return f"Selected Website: Two, Input 2: {input2}, Input 3: {input3}"
        elif selected_website == '3':
            input4 = request.form['input4']
            # Process input4 data
            return f"Selected Website: Three, Input 4: {input4}"
        else:
            return render_template('index.html')
            

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
