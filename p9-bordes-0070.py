# Axel Guzman 0070
# problema 27
import cv2

# Cargar imagen del delfín
imagen = cv2.imread("delfin.jpg")

if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar bordes
bordes = cv2.Canny(gris, 100, 200)

# Encontrar contornos
contornos, jerarquia = cv2.findContours(
    bordes,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Dibujar contornos
resultado = imagen.copy()
cv2.drawContours(resultado, contornos, -1, (0, 255, 0), 2)

# Mostrar imágenes
cv2.imshow("Delfin original 0070", imagen)
cv2.imshow("Bordes 0070", bordes)
cv2.imshow("Contornos del delfin 0070", resultado)

# Guardar resultado
cv2.imwrite("delfin_contornos.jpg", resultado)

print("Contornos encontrados:", len(contornos))

cv2.waitKey(0)
cv2.destroyAllWindows()
print("programa realizado por Axel Guzman 0070")