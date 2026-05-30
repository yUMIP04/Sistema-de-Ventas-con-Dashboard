import pandas as pd
import os
import datetime

def ProcesamientoDatos_CSV(archivo_csv):
    ruta_csv = f'static/uploads/CSV/{archivo_csv}'

    try:
        if os.path.exists(ruta_csv):
            print("👌Se encontro con exito el archivo")
            
            #🌟limpieza datos

            csv = pd.read_csv(ruta_csv)

            precio_formateado = csv["Precio"].str.lower().str.replace("$", "").str.replace("pesos", "").astype('float')
            cantidad_formateada = csv["Cantidad Vendida"].str.lower().str.replace("vendidos", "").str.replace("vendidas", "").str.replace("vendido", "").str.replace("vendida", "").astype('int')
            fecha_formateada = pd.to_datetime(csv["Fecha"], format='%d/%m/%Y', errors='raise')

            csv["Precio"] = precio_formateado
            csv["Cantidad Vendida"] = cantidad_formateada
            csv["Fecha"] = fecha_formateada
            print(csv)
            
        else:
            print("❌ No se encontro ningun archivo csv.")
            return None
        
    except Exception as e:
        print(f"Hubo un error al encontrar el archivo: {e}")
        return None

ProcesamientoDatos_CSV("archivo.csv")