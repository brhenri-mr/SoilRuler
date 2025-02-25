import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import pandas as pd
from rex.util import pre_tratamento, refino
from rex.engine import creatRuler

df = {}

pdf = "SondagemTestReduzido.pdf"
tipos_solo = ["Areia", "Argila", "Silte", "Laterita", "Rocha", "Cascalho"]
text_filtrado = []
text = []
temp = {'camada':[], 'tamanho':[]}
p_i = -1.45
delta_passo = -1

# Caminho do Tesseract (ajuste caso necessário)
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Wosniak-03\OneDrive\Área de Trabalho\Tesseract\tesseract.exe"  # No Windows

# Converter o PDF para imagens (uma imagem por página)
imagens = convert_from_path(pdf)
for imagem in imagens:
    if isinstance(imagem, Image.Image):

        texto_extraido = pytesseract.image_to_string(imagem)

        # Ignorando caracteres inválidos
        texto_extraido = texto_extraido.encode('utf-8', 'ignore').decode('utf-8')

    else:
        print(imagem)

for entrada in texto_extraido.split('\n'):
    for categoria in tipos_solo:
        if categoria in entrada:
            text.append(entrada)
            break

text = [pre_tratamento(element) for element in text]

#refino(text)

text_aux = text.copy()




for element in text:
    # Verificando se já há uma camada
    if len(temp['camada']) == 0:
        temp['camada'].append(element)
        temp['tamanho'].append(1)

    else:

        if element == temp['camada'][-1]:
            temp['tamanho'][-1] = temp['tamanho'][-1] + 1

        else:

            temp['camada'].append(element)
            temp['tamanho'].append(1)






#creatRuler(p_i*100, delta_passo*100, pd.DataFrame(temp))


