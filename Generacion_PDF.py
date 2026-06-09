from reportlab.pdfgen import canvas
import os

ruta = os.path.join(f'static', 'uploads', 'PDFS')



def generar_PDF(archivo, nombre_archivo):

    archivo.drawString(100, 100, "Resultados:")

archivo = canvas.Canvas(f"{nombre_archivo}.pdf")

generar_PDF(archivo)
archivo.showPage()
archivo.save()