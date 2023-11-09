# -*- coding: utf-8 -*- 
from app import model, tokenizer, device
import io
import torch

DEBUG = False

def classify(text):
    if DEBUG:
        print('/////////////////////////////////')
        print(text)
        print('/////////////////////////////////')

    #   tokenizer recibe el texto (String) y entrega inputs_ids y attention_mask, que son Tensor, el tipo que usa Pytorch para los vectores / tensores
    input = tokenizer(text, return_tensors="pt").to(device)
    with torch.no_grad():
        logits= model(**input).logits
    predicted_class_id = logits.argmax().item()
    out = model.config.id2label[predicted_class_id]
    return out