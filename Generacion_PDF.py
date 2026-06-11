from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import os
from StylesPDFS.Membretado import Titulo_Membretado

def Generar_PDF(nombre_archivo):

    ruta = os.path.join('static', 'uploads', 'PDFS')

    if not os.path.exists(ruta):
        
        print("No existe la ruta ¡Estoy por crearla!")
        os.makedirs(ruta)

    else:

        print("¡Si existe la ruta!")
        ruta_final = os.path.join(ruta, nombre_archivo)

        story = []

        #Estilos

        try:

           doc = SimpleDocTemplate(ruta_final, pagesizes="letter", leftMargin=72, rightMargin=72, topMargin=142, bottomMargin=72)

           Titulo_Resultados = Paragraph("<b>Resultados</b>")

           story.append(Titulo_Resultados)

           doc.build(story, onFirstPage=Titulo_Membretado, onLaterPages=Titulo_Membretado)

           print("Creando el archivo pdf con exito")
        except Exception as e:

            print(f"Hubo un error al crear el archivo pdf : {e}")
            return None



Generar_PDF("Prueba.pdf")