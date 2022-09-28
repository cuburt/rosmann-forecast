import os
import json
import joblib
import numpy as np
from datetime import datetime
from flask import Flask, request

app = Flask(__name__)
model = joblib.load(os.path.join("model_storage", f"rosmann.sav"))

def format_request_payload(request):

    date_object = datetime.strptime(request.get('Date'), '%Y-%m-%d').date()

    request['Year'] = date_object.year
    request['Month'] = date_object.month
    request['Day'] = date_object.day

    mappings = {'0':0, 'a':1, 'b':2, 'c':3, 'd':4}
    state_holiday = request.get('StateHoliday')
    for key, value in mappings.items():
        state_holiday = state_holiday.replace(key, str(value))
    request['StateHoliday'] = int(state_holiday)

    a_list = ['Store', 'DayOfWeek', 'Customers', 'Open', 'Promo', 'StateHoliday', 'SchoolHoliday', 'Year', 'Month', 'Day']

    return np.array([[i[1] for i in [(key, request[key]) for key in a_list if key in request]]])
    
@app.route('/predict', methods=['POST'])
def predict():

    try:

        _input = format_request_payload(request.get_json(force=True))

        output = model.predict(_input)
        _output = float(format(output[0], '.2f'))
        response = json.dumps({"Sales": _output})

    except Exception as e:
        response = json.dumps({"Error": str(e)})

    return response

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)