from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

def date_assembler(string):
    if(len(string)>=5):
        substr = str[-19::]
        dt = datetime.strptime(substr, '%Y_%m_%d_%H_%M')
        return dt
    else:return datetime.strptime('2018_02_20_10_30', '%Y_%m_%d_%H_%M')

@app.route('/<value>')
def heatmap(value):
    if ("noise" in str(value)):
        date = date_assembler(str(value))
        return render_template('noise.html')
    if ("heat" in str(value)):
        date = date_assembler(str(value))
        return render_template('heat.html')
    if ("smoke" in str(value)):
        date = date_assembler(str(value))
        return render_template('smoke.html')
    if ("light" in str(value)):
        date = date_assembler(str(value))
        return render_template('light.html')
    return 404







'''
@app.route('/noise')
def home():
    return render_template('noise.html')

@app.route('/smoke')
def smoke():
    return render_template('smoke.html')

@app.route('/heat')
def heat():
    return render_template('heat.html')

@app.route('/light')
def light():
    return render_template('light.html')
'''
if __name__ == "__main__":
    app.run()