from flask import Flask, url_for, render_template, redirect
from collections import defaultdict
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
    return render_template('index.html')

@app.route('/predict', methods=('GET', 'POST'))
def predict():
      # NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation

        requestValues = request.get_json()
       
        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer '
                 + "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpGdExSb3BtNUl3N0hMUGhXMzg4S3pJOXpsWkExaUVHaGRoMXFUeXpmRGMifQ.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZSI6IkFkbWluIiwicGVybWlzc2lvbnMiOlsiYWRtaW5pc3RyYXRvciIsImNhbl9wcm92aXNpb24iLCJtYW5hZ2VfY2F0YWxvZyIsImNyZWF0ZV9wcm9qZWN0IiwiY3JlYXRlX3NwYWNlIiwiYWNjZXNzX2NhdGFsb2ciLCJzaWduX2luX29ubHkiXSwiZ3JvdXBzIjpbMTAwMDBdLCJzdWIiOiJhZG1pbiIsImlzcyI6IktOT1hTU08iLCJhdWQiOiJEU1giLCJ1aWQiOiIxMDAwMzMwOTk5IiwiYXV0aGVudGljYXRvciI6ImRlZmF1bHQiLCJkaXNwbGF5X25hbWUiOiJhZG1pbiIsImlhdCI6MTY2NzU4NjIxMywiZXhwIjoxNjY3NjI5Mzc3fQ.co54f3JJ_P2GoxoEaplyJIdB4QRT8jtV1G1qRpnCWTKIVSd7aVjTt7Tn-lo-j5Wm3dPf9_2fasx6K1Wpvk3vp7vo8cOC2TVw_pycDFLKezcpMRVDB5g5A6qdZJvXDDdjVwXt_OhB2I3PDt2u3TzBNHsq3nbq9Wrlb6N0K8IVFU4LFikNPHwBn0aN3EODvWhV371xtu3RM3tU7Qn_MOYfx46RDcRTfFRYpzOoT3MIFIFvJ7foeyKm27hok4nr6GfxSFV--xQ0ApYEeTx8-Ulrn2L9OeVlWQDzBNyYv2cB72x_0HaMIl_XbXWqOQi7chhqu26e4Ds63jH0LFr1yYe9Sw"}

        python_object = ["male",79,0,1,"no","private","urban",98.4,25.2,"former smoker"]
      
        #Transform python objects to  Json

        userInput = []
        userInput.append(python_object)

        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"fields": ["gender", "age", "hypertension","heart_desease", "ever_married", "work_type", "Residence_type", "avg_glucose_level", "bmi", "smoking_status"], "values": userInput }]}

        response_scoring = requests.post("https://cpd-zen.cpd-demo2-dal-cluster-cc3f7f98932dd5458e6ef8ebaf682399-0000.us-south.containers.appdomain.cloud/ml/v4/deployments/b3846840-2881-44ca-a6aa-59e5107622a4/predictions?version=2022-10-28", json=payload_scoring, headers=header, verify=False)
        output = json.loads(response_scoring.text)
        
        print("---respuesta de la api----")
        print(output)
        print("---respuesta de la api----")

        for key in output:
          ab = output[key]
          print(ab)
        

        for key in ab[0]:
          bc = ab[0][key]
        
        stroke = round(bc[0][0],2)
        
        print(".......")
        print(stroke)
  
         # this returns the response back to the front page
        return '{"key":' + str(stroke) + '}'