# -*- coding: utf-8 -*- 
from app import model, tokenizer, device
import io
import torch
import cv2
import pytesseract

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


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def thresholding_invert(image):
  image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
  # Contar píxeles negros y blancos
  total_pixels = image.size
  black_pixels = np.count_nonzero(image == 0)
  white_pixels = total_pixels - black_pixels

  # Determinar si hay más píxeles negros que blancos
  if black_pixels > white_pixels:
      # Invertir colores (negro a blanco, blanco a negro)
      image = cv2.bitwise_not(image)
      
  return image



def OCR(img_bytes):
    img = cv2.imread(img_bytes)
    gray = get_grayscale(img)
    thres = thresholding_invert(gray)
    data = pytesseract.image_to_strig(thres, lang="spa")
    return data
