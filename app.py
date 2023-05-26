from flask import Flask, render_template
import scale
import data
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

notas = data.notas

'''
Index route
'''
@app.route("/")
def index():

    return "Bienvenido !!"

'''
Index Chords

Params:
Clave: the note over build the musical circle
tonalidad: the mode
'''
@app.route("/circulo/<int:clave>/<int:tonalidad>", methods=["GET"])
def contacto(clave, tonalidad):
    doml = clave+7
    segtono = clave+2
    domll = segtono+7
    acordes = ["", "", "", ""]

    for nota in  notas:
        no = nota["semitono"]
        if no == clave:
            acordes[0] = nota["nota"]
    if clave == 1:
        for nota in notas:
            no = nota["semitono"]
            if no == doml:
                acordes[3] = nota["nota"]
            if no == segtono:
                acordes[2] = nota["nota"]
            if no == domll:
                acordes[1] = nota["nota"]
        return acordes
    else:
        return "no es DO"


@app.route("/escala/<int:note>/<int:tonalidad>",methods=["GET"])
def escala(note, tonalidad):

    if tonalidad == 1:
        escala = (2, 2, 1, 2, 2, 2, 1, 2)
        return scale.scales.scaleMayor_contructor(escala,note)
    if tonalidad == 69:
        escala = (3, 2, 1, 1, 3, 2, 2)
        return scale.scales.scaleMayor_contructor(escala,note)


