from flask import Flask,request
import util

app = Flask(__name__)

@app.route('/get_column_names')
def get_column_names():
    response = {'Data Columns' : util.showColumns()}
    return response

@app.route('/predict_rtw',methods=['POST'])
def predict_rtw():
    cfy = float(request.form['claimyear'])
    agency = float(request.form['agency'])
    age = float(request.form['age'])
    iag = request.form['injurygroup']
    blg = request.form['bodygroup']
    mcg = request.form['mechanismgroup']
    nature = request.form['nature']
    major = request.form['major']
    gender = request.form['gender']

    rtw = util.predict_returnToWorkCategory(cfy,agency,age,iag,blg,mcg,nature,
                                            major,gender)
    response = {'Estimated_Return' : rtw}
    return response

app.run()
