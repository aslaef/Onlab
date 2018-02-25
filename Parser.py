from flask import Flask, render_template, request, flash
from datetime import datetime
import json

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
        #date = date_assembler(str(value))
        return render_template('noise.html')
    if ("heat" in str(value)):
        #date = date_assembler(str(value))
        return render_template('heat.html')
    if ("smoke" in str(value)):
        #date = date_assembler(str(value))
        return render_template('smoke.html')
    if ("light" in str(value)):
        #date = date_assembler(str(value))
        return render_template('light.html')
    return 404





@app.route('/heat', methods=['POST','GET'])
def heatmap_post():
    try:
        if(request.method == 'POST'):
            text = request.form.get("datefield")
            print(str(text))
            data=[[19.9240094, 47.780369, 15.9]]

            #heatmap database


            return render_template('heat.html', data=json.dumps(data))
        else:
            return render_template('heat.html')
    except Exception as e:
        print(e)
        return render_template('heat.html')

if __name__ == "__main__":
    app.run()