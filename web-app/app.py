from flask import Flask, url_for, render_template, redirect
from forms import PredictForm
from flask import request, sessions
import requests
from flask import json
from flask import jsonify
from flask import Request
from flask import Response
import urllib3
import json
# from flask_wtf import FlaskForm

app = Flask(__name__, instance_relative_config=False)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'development key' #you will need a secret key

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')

@app.route('/', methods=('GET', 'POST'))

def startApp():
    form = PredictForm()
    return render_template('index.html', form=form)

@app.route('/predict', methods=('GET', 'POST'))
def predict():
    form = PredictForm()
    if form.submit():

        # NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation
        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer '
                 + "eyJraWQiOiIyMDIyMDkxMzA4MjciLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC02NjcwMDA0RlFDIiwiaWQiOiJJQk1pZC02NjcwMDA0RlFDIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiOGFjNjg5ZDgtMzA2Yi00MDY3LThiNjktNjZiZjgzNTQ0NGY0IiwiaWRlbnRpZmllciI6IjY2NzAwMDRGUUMiLCJnaXZlbl9uYW1lIjoiTWVyY2VkZXMgQmVsZW4iLCJmYW1pbHlfbmFtZSI6Ik1hZ25lbGxpIiwibmFtZSI6Ik1lcmNlZGVzIEJlbGVuIE1hZ25lbGxpIiwiZW1haWwiOiJtbWFnbmVsbGlAaWJtLmNvbSIsInN1YiI6Im1tYWduZWxsaUBpYm0uY29tIiwiYXV0aG4iOnsic3ViIjoibW1hZ25lbGxpQGlibS5jb20iLCJpYW1faWQiOiJJQk1pZC02NjcwMDA0RlFDIiwibmFtZSI6Ik1lcmNlZGVzIEJlbGVuIE1hZ25lbGxpIiwiZ2l2ZW5fbmFtZSI6Ik1lcmNlZGVzIEJlbGVuIiwiZmFtaWx5X25hbWUiOiJNYWduZWxsaSIsImVtYWlsIjoibW1hZ25lbGxpQGlibS5jb20ifSwiYWNjb3VudCI6eyJib3VuZGFyeSI6Imdsb2JhbCIsInZhbGlkIjp0cnVlLCJic3MiOiIzMzU4ZDhjZjQ3NTY0MWExOTNmMWJjYTQyNjY4MWVjMSIsImZyb3plbiI6dHJ1ZX0sImlhdCI6MTY2NTU5NTQzNywiZXhwIjoxNjY1NTk5MDM3LCJpc3MiOiJodHRwczovL2lhbS5jbG91ZC5pYm0uY29tL29pZGMvdG9rZW4iLCJncmFudF90eXBlIjoidXJuOmlibTpwYXJhbXM6b2F1dGg6Z3JhbnQtdHlwZTphcGlrZXkiLCJzY29wZSI6ImlibSBvcGVuaWQiLCJjbGllbnRfaWQiOiJkZWZhdWx0IiwiYWNyIjoxLCJhbXIiOlsicHdkIl19.uWsmtqOt-2YCgkgRzjIM6l2jaRbZv7YTtP2BQATyvxS3gY6OvOPFKKG0QMkaIEljtyBRxuywB5GKP5ZVluYV7zwfomgjJFc_52WGrjKuDvsW-ZFC5w00fsNZ4G9LNnLF8oVohEZTKE9YaSG9bIpzsIFl2TdKQkUwzlLLj3lriNPrTe8CmHh2-rtAOttXKGlkeIs1mINBygGfSWQQ5TRrAHloWBQljJTvQevx9oUHnd7LtazQH7d6V1KbLHxGeRFFUY7mxteQiMjgrYjD3c4nVVhmXkBAJ5yQhp46vkBLoizUhARCJY3AakunqCK8_C-YNtJI50kjd8HmV9s_bcPpmA"}

        if(form.bmi.data == None): 
          python_object = []
        else:
          python_object = [form.age.data, form.sex.data, float(form.bmi.data),
            form.children.data, form.smoker.data, form.region.data]
        #Transform python objects to  Json

        userInput = []
        userInput.append(python_object)

        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"fields": ["age", "sex", "bmi",
          "children", "smoker", "region"], "values": userInput }]}

        response_scoring = requests.post("https://us-south.ml.cloud.ibm.com/ml/v4/deployments/1ae7bef0-3375-41fa-ae4d-4cad5a8bbc6d/predictions?version=2022-10-12", json=payload_scoring, headers=header)
        output = json.loads(response_scoring.text)
        print(output)
        for key in output:
          ab = output[key]
        

        for key in ab[0]:
          bc = ab[0][key]
        
        roundedCharge = round(bc[0][0],2)

  
        form.abc = roundedCharge # this returns the response back to the front page
        return render_template('index.html', form=form)