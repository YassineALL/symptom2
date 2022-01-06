from flask import Flask, request, jsonify
import util
from flask_cors import CORS
import math
import numpy as np



app = Flask(__name__)
CORS(app)

@app.route('/get_symptom_names', methods=['GET'])
def get_symptom_names():
     response = jsonify({
         'symptom': util.get_data_columns()
     })
     response.headers.add('Access-Control-Allow-Origin', '*')

     return response

@app.route('/get_diseases_names', methods=['GET'])
def get_diseases_names():
     response = jsonify({
         'diseases': util.get_diseases_names()
     })
     print( util.get_diseases_names())
     response.headers.add('Access-Control-Allow-Origin', '*')

     return response

@app.route('/predict_disease', methods = ['GET','POST'])
def predict_disease():


     S1 = request.form['S1']
     S2 = request.form['S2']
     S3 = request.form['S3']
     S4 = request.form['S4']
     S5 = request.form.get('S5',None)
     S6 = request.form.get('S6',None)
     print(type(S6))
     # is_NaN = math.isnan(request.form['S6'])
     # if is_NaN == True :
     #      S6 == 0

     if (S6 == None) and  (S5 == None):

               print(S1, S2, S3, S4, S5,S6)
               response = jsonify({

                    'predict_disease': util.predict_disease(S1, S2, S3, S4)
               })
               print("response ", response)
               response.headers.add('Access-Control-Allow-Origin', '*')


     elif (S6 == None):


          response = jsonify({
               'predict_disease': util.predict_disease(S1, S2, S3, S4, S5 )
          })
          print("response ", response)
          response.headers.add('Access-Control-Allow-Origin', '*')

     # elif (S5 == None):
     #
     #      response = jsonify({
     #           'predict_disease': util.predict_disease(S1, S2, S3, S4, S6,S5 =0 )
     #      })
     #      print("response ", response)
     #      response.headers.add('Access-Control-Allow-Origin', '*')



     # elif S5 == None  :
     #
     #
     else :

        response = jsonify({
            'predict_disease': util.predict_disease(S1,S2,S3,S4,S5,S6)
        })
        print("response ",response)
        response.headers.add('Access-Control-Allow-Origin', '*')

     # if S5 == None:
     #
     #     response = jsonify({
     #         'predict_disease': util.predict_disease(S1, S2, S3, S4)
     #    })
     #     print("response ", response)
     #     response.headers.add('Access-Control-Allow-Origin', '*')
     return response



@app.route('/description', methods = ['GET'])
def description():
     response = jsonify({
         'Description of the disease': util.description()
     })
     response.headers.add('Access-Control-Allow-Origin', '*')

     return response

@app.route('/precaution', methods = ['GET'])
def precaution():
     response = jsonify({
         'Precaution of the disease': util.precaution()
     })
     response.headers.add('Access-Control-Allow-Origin', '*')

     return response

if __name__ == "__main__":
   util.load_saved_artifacts()
   app.run(debug = True)