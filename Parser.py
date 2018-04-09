from flask import Flask, render_template, request
from datetime import datetime
import json

app = Flask(__name__)
app.FLASK_DEBUG=1

def date_assembler(string):
    try:
        if(len(string)>=5):
            dt = datetime.strptime(string, '%Y.%m.%d.%H.%M.%S')
            return dt
        else:
            return datetime.strptime('2018_02_20_10_30_00', '%Y.%m.%d.%H.%M.%S')
    except Exception as e:
        print(e)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/heat', methods=['POST','GET'])
def heatmap_post():
    try:
        if(request.method == 'POST'):
            text = request.form.get("datefield")

            mydate_string=str(text)

            #TODO:



            requested_date = date_assembler(mydate_string)

            data=[[19.9240094, 47.780369, 15.9]]

            #heatmap database





            return render_template('heat.html', data=json.dumps(data))
        else:
            return render_template('heat.html')
    except Exception as e:
        print(e)
        return render_template('heat.html')

@app.route('/noise', methods=['POST','GET'])
def noise_post():
    try:
        if(request.method == 'POST'):
            text = request.form.get("datefield")
            print(str(text))
            data=[[19.9240094, 47.780369, 15.9]]

            #heatmap database

            return render_template('noise.html', data=json.dumps(data))
        else:
            return render_template('noise.html')
    except Exception as e:
        print(e)
        return render_template('noise.html')

@app.route('/smoke', methods=['POST','GET'])
def smoke_post():
    try:
        if(request.method == 'POST'):
            text = request.form.get("datefield")
            print(str(text))
            data=[[19.9240094, 47.780369, 15.9]]

            #heatmap database

            return render_template('smoke.html', data=json.dumps(data))
        else:
            return render_template('smoke.html')
    except Exception as e:
        print(e)
        return render_template('smoke.html')

@app.route('/light', methods=['POST','GET'])
def light_post():
    try:
        if(request.method == 'POST'):
            text = request.form.get("datefield")
            print(str(text))
            data=[[19.9240094, 47.780369, 15.9]]

            #heatmap database

            return render_template('light.html', data=json.dumps(data))
        else:
            return render_template('light.html')
    except Exception as e:
        print(e)
        return render_template('light.html')

if __name__ == "__main__":
    app.run()