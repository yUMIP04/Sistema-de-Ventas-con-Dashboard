from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

def Generar_PDF(nombre_archivo):

    ruta = os.path.join('static', 'uploads', 'PDFS')

    if not os.path.exists(ruta):
        
        print("No existe la ruta ¡Estoy por crearla!")
        os.makedirs(ruta)

    else:

        print("¡Si existe la ruta!")
        ruta_final = os.path.join(ruta, nombre_archivo)
        print("Redirigiendo a la ruta: ", ruta_final)

        

Generar_PDF("Prueba.pdf")