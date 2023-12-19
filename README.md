# Cyber-Defender-IA

In order to make this work locally you can start an environment with virtualenv or with conda, after activating your environment go to the app-ia directory, you should execute the next command in your prefered terminal:

```pip install -r requirements.txt```

After installing the requirements for the project, then you can start the Flask app with the next command:

```py main.py```

And your app is up and running, now you can send queries to it with postman or make a web app that uses the link localhost:5001/classify or other link in case that you want to deploy it on the web.

This repository also counts with a web app that uses OCR in order to recognize text, and then it evaluates the text with the ML component. In order to deploy it you must first install tesseractOCR in your desktop.
