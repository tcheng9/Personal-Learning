from flask import Flask,render_template,request
from srs_maker import srs_model

app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('form.html')
 
'''
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html',form_data = form_data)
''' 


@app.route('/result', methods = ["POST", "GET"])

def html_table():
    if request.method == "POST":
        cutoff = request.form["Cutoff"]
        
        df = srs_model(cutoff)
        
        return render_template('simple.html', tables = [df.to_html(classes = 'data')], titles = df.columns.values)
    if request.method == "GET":
        return f"This is the incorrect way"
 
app.run(host='localhost', port=5000)
