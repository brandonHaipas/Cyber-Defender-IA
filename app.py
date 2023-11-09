# -*- coding: utf-8 -*- 
import json
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from flask import Flask

app = Flask(__name__)

#
#   App contiene el modelo de IA, en este cargo se descarga, pero tambien se puede abrir el binario de un modelo (ej: mi_modelo.bin) 
#   desde PyTorch
#

device = 'cuda' if torch.cuda.is_available() else 'cpu'

#   El tokenizer preprocesa el texto, recibe un texto (String) y entrega un diccionario con los inputs_ids y mascaras de atencion,
#   que se entregan posteriormente al modelo 
tokenizer = AutoTokenizer.from_pretrained("dccuchile/distilbert-base-spanish-uncased")
model = AutoModelForSequenceClassification.from_pretrained('Brandon-h/distilbert-finetuned-spanish-offensive-language').to(device)

DEBUG = True