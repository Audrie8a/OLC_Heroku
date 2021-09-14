from Analyzer.Panther import parser
from typing import List, Text
from flask import *
from werkzeug.wrappers import response
from flask_cors import CORS, cross_origin
from Environment.Listas import Listas
from Reportes.Reportes import Reportes
from flask import render_template
import json


app= Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/Inicio')
def hello_world():
    return render_template('index.html')



@app.route('/Entrada', methods=['POST'])
def Entrada():
    Texto= request.json['Texto']
    #print(Texto)
    parser.parse(Texto)
    #Respuesta= json.dumps(Listas.getListSaida())
    response= jsonify( {"Respuesta": Listas.getListSaida(),
                        "Tamano": len(Listas.getListSaida())})
    response.headers.add("Access-Control-Allow-Origin", "*")
    #Reportes.Tabla_Errores()
    Listas.LimpiarLsts()
    return response

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)




