import pandas as pd
import plotly.express as px
import os


def Create_Graficas (archivo_csv):

    ruta = f'static/uploads/CSV/{archivo_csv}'

    if not os.path.exists(ruta):

        print("❌ El archivo no existe")

    else:

        datos_csv = pd.read_csv(ruta)
        print("🥳 Si existe el archivo")

        #ventas por producto

        ventas = datos_csv["Cantidad Vendida"].str.replace("vendidos", "").str.replace("vendidas", "").str.replace("productos", "").str.replace("cantidad", "")

        ventas_int = ventas.astype('int')
        datos_csv["Cantidad Vendida"] = ventas_int
        
        ventas_producto = {
            "Nombre Producto" : datos_csv["Nombre Producto"],
            "Cantidad Vendida": datos_csv["Cantidad Vendida"]
        }

        Tabla_ventasProducto = pd.DataFrame(ventas_producto)

        print(Tabla_ventasProducto)
Create_Graficas("archivo.csv")