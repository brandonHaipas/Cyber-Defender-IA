from app import app, DEBUG
from utils import classify
from flask import Flask, jsonify, request

#   En servidor:5001/summ esta app recibe los POST con los textos para procesar
@app.route('/summ', methods=['POST'])
def submit():
    #   request contiene la informacion entregada en la request
    file = request.files['texto']
    #   en este caso request.files['texto'] contiene el texto
    text =  (file.read()).decode()
    #   se usa la funcion summarize definida en utils
    if DEBUG:
        print(text)
    result = classify(text)
    return result

if __name__ == "__main__":
    app.run(port=5001)