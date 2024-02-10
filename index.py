import cv2

# Carregar uma imagem
imagem = cv2.imread('image.jpg')

# Exibir a imagem
cv2.imshow('Janela de Imagem', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Converter para escala de cinza
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow('Escala de Cinza', cinza)
cv2.waitKey(0)

# Desfocar uma imagem
desfocada = cv2.GaussianBlur(cinza, (7, 7), 0)
cv2.imshow('Imagem Desfocada', desfocada)
cv2.waitKey(0)

# Detecção de bordas Canny
bordas = cv2.Canny(imagem, 100, 200)
cv2.imshow('Detecção de Bordas', bordas)
cv2.waitKey(0)

classificador = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

rostos = classificador.detectMultiScale(cinza, 1.2, 4)
for (x, y, w, h) in rostos:
    cv2.rectangle(imagem, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Detecção de Rostos', imagem)
cv2.waitKey(0)