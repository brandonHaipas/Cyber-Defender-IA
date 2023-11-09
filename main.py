from app import app, DEBUG
from utils import classify, OCR
from flask import Flask, jsonify, request

#   En servidor:5001/summ esta app recibe los POST con los textos para procesar
@app.route('/summ', methods=['POST'])
def submit():
    #   request contiene la informacion entregada en la request
    file = request.files['file']
    #   en este caso request.files['texto'] contiene el texto
    img_bytes = file.read()
    text = OCR(img_bytes)
    #   se usa la funcion summarize definida en utils
    if DEBUG:
        print(file)
    result = classify(text)
    return result

if __name__ == "__main__":
    app.run(port=5001)