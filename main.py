from app import app, DEBUG
from utils import classify, OCR
from flask import Flask, jsonify, request

#   En servidor:5001/classify esta app recibe los POST con los textos para procesar
@app.route('/classify', methods=['POST'])
def submit():
    #   request contiene la informacion entregada en la request
    file = request.files['file']
    #   en este caso request.files['texto'] contiene el texto
    text = OCR(file)
    #   se usa la funcion summarize definida en utils
    if DEBUG:
        print(file)
    result = classify(text)
    return result

if __name__ == "__main__":
    app.run(port=5001)