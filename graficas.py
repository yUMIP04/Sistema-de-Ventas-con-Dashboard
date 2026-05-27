import pandas as pd
import plotly.express as px
import os
import datetime


def Create_Graficas (archivo_csv):

    ruta = f'static/uploads/CSV/{archivo_csv}'

    if not os.path.exists(ruta):

        print("❌ El archivo no existe")

    else:

        datos_csv = pd.read_csv(ruta)
        print(datos_csv)
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

    try:
        Grafica_Barras = px.bar(Tabla_ventasProducto, x="Nombre Producto", y="Cantidad Vendida", title="Ventas por producto")
        #Grafica_Barras.show()

        #return Grafica_Barras
    
    except Exception as e:
        print(f"Hubo un error al Generar la grafica de barras: {e}")

    #ventas por fecha
    
    Precios_float = datos_csv["Precio"].str.replace("$", "").astype('float')
    datos_csv["Precio"] = Precios_float
    fecha_formateada = pd.to_datetime(datos_csv["Fecha"], format='%d/%m/%y', errors='cocerce')
    datos_csv["Fecha"] = fecha_formateada

    agrupando = datos_csv.groupby('')
    ventas_fecha = {
        "Nombre Producto": datos_csv["Nombre Producto"],
        "Precio":datos_csv["Precio"],
        "Fecha": datos_csv["Fecha"]
    }

    TablaVentas_fecha = pd.DataFrame(ventas_fecha)
    
    
Create_Graficas("archivo.csv")