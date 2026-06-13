from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import os
from StylesPDFS.Membretado import Titulo_Membretado
from StylesPDFS.Estilos_Titulo import Estilo_Titulo, Estilo_infoArchivo
import datetime

def Generar_PDF(nombre_archivo, nombre_csv, fecha=None):

    ruta = os.path.join('static', 'uploads', 'PDFS')

    if not os.path.exists(ruta):
        
        print("No existe la ruta ¡Estoy por crearla!")
        os.makedirs(ruta)

    else:

        print("¡Si existe la ruta!")
        ruta_final = os.path.join(ruta, nombre_archivo)

        story = []

        #Estilos
        Titulo_Estilo = Estilo_Titulo()
        info_Estilo = Estilo_infoArchivo()

        try:
           
           #Creacion del Archivo
           doc = SimpleDocTemplate(ruta_final, pagesizes="letter", leftMargin=72, rightMargin=72, topMargin=142, bottomMargin=72)

           #Variables a agregar
           Titulo_Resultados = Paragraph("<b>Resultados del Analisis de Venta</b>", Titulo_Estilo )
           infoArchivo_List = [f"<b>Nombre del archivo:</b> {nombre_csv}",
                               f"<b>Fecha de resultados:</b> {fecha}"]
          
            #Agregando objetos al PDF
           story.append(Titulo_Resultados)

           for info in infoArchivo_List:
               story.append(Paragraph(info, info_Estilo))

          
           

           doc.build(story, onFirstPage=Titulo_Membretado, onLaterPages=Titulo_Membretado)

           print("Creando el archivo pdf con exito")
        except Exception as e:

            print(f"Hubo un error al crear el archivo pdf : {e}")
            return None


fecha_resultados = datetime.datetime.now().strftime('%A'+ " " + '%B' + " " + '%Y')
Generar_PDF("Prueba.pdf", "archivoPrueba.csv", fecha_resultados)