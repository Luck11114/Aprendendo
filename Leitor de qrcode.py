from pyzbar.pyzbar import decode
from PIL import Image
caminho = "C:/Users/luckp/Desktop/Testes/qrcode.png"
imagem = Image.open(caminho)
print(decode(imagem))