from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import os
import datetime
import plotly.express as px

from StylesPDFS.Membretado import Titulo_Membretado
from StylesPDFS.Estilos_Titulo import Estilo_Titulo, Estilo_infoArchivo
from StylesPDFS.Estilos_Tabla import Tabla_Resultados


def Generar_PDF(nombre_archivo, nombre_csv, fecha, total_ventasDinero, total_productosVendidos, promedio):

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
           doc = SimpleDocTemplate(ruta_final, pagesize=letter, leftMargin=72, rightMargin=72, topMargin=142, bottomMargin=72)

           #Variables a agregar
           Titulo_Resultados = Paragraph("<b>Resultados del Analisis de Venta</b>", Titulo_Estilo )
           infoArchivo_List = [f"<b>Nombre del archivo:</b> {nombre_csv}",
                               f"<b>Fecha de resultados:</b> {fecha}"]
           
           datos_Tabla = [
                          ["Total Ventas(Dinero):", total_ventasDinero],
                          ["Total de Productos Vendidos:", total_productosVendidos],
                          ["Promedio de Ventas:", promedio]]
           Estilo_Tabla = Tabla_Resultados(datos_Tabla)

           Titulo_Graficas = Paragraph("<b>Graficas</b>", Titulo_Estilo )
           
            #Agregando objetos al PDF
           story.append(Titulo_Resultados)

           for info in infoArchivo_List:
               story.append(Paragraph(info, info_Estilo))

           story.append(Spacer(1, 20))
           story.append(Estilo_Tabla)
           story.append(Spacer(1, 20))
           story.append(Titulo_Graficas)

           #integracion graficas

           nombre_limpio_csv = os.path.basename(nombre_csv)

           ruta_img_barras = f"static/uploads/IMG_Graficas/grafica_Barras_{nombre_limpio_csv}.png"
           ruta_img_lineas = f"static/uploads/IMG_Graficas/grafica_Lineas_{nombre_limpio_csv}.png"
           ruta_img_pastel = f"static/uploads/IMG_Graficas/grafica_Pastel_{nombre_limpio_csv}.png"


           if os.path.exists(ruta_img_barras):
               
               story.append(Spacer(1,12))
               img_barras = Image(ruta_img_barras, width=420, height=245)
               img_barras.hAlign='LEFT'
               story.append(img_barras)

           if os.path.exists(ruta_img_lineas):
               
               story.append(Spacer(1,12))
               img_lineas = Image(ruta_img_lineas, width=420, height=245)
               img_lineas.hAlign = 'LEFT'
               story.append(img_lineas)

           if os.path.exists(ruta_img_pastel):
               
               story.append(Spacer(1,12))
               img_pastel = Image(ruta_img_pastel, width=420, height=245)
               img_pastel.hAlign='LEFT'
               story.append(img_pastel)

           doc.build(story, onFirstPage=Titulo_Membretado, onLaterPages=Titulo_Membretado)

           print("Creando el archivo pdf con exito")
        except Exception as e:

            print(f"Hubo un error al crear el archivo pdf : {e}")
            return None


fecha_resultados = datetime.datetime.now().strftime('%A'+ " " + '%B' + " " + '%Y')
Generar_PDF("Prueba.pdf", "archivoPrueba.csv", fecha_resultados, "12", "120", "9.9")