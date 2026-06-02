import pandas as pd
import os
import datetime

def ProcesamientoDatos_CSV(ruta_csv):

    try:
        if os.path.exists(ruta_csv):
            print("👌Se encontro con exito el archivo")

            
            #🌟limpieza datos

            csv = pd.read_csv(ruta_csv)

            if not csv.empty:
                
                print("👌El archivo tiene contenido")

                columnas_obligatorias = {"Nombre Producto", "Categoria", "Precio", "Cantidad Vendida", "Fecha"}
                
                revision_columnasObligatorias = columnas_obligatorias.issubset(csv.columns)

                if revision_columnasObligatorias:
                   
                   print("👌 El archivo tiene las columnas obligatorias")

                   precio_formateado = csv["Precio"].str.lower().str.replace("$", "").str.replace("pesos", "").astype('float')
                   cantidad_formateada = csv["Cantidad Vendida"].str.lower().str.replace("vendidos", "").str.replace("vendidas", "").str.replace("vendido", "").str.replace("vendida", "").astype('int')
                   fecha_formateada = pd.to_datetime(csv["Fecha"], format='%d/%m/%Y', errors='raise')

                   csv["Precio"] = precio_formateado
                   csv["Cantidad Vendida"] = cantidad_formateada
                   csv["Fecha"] = fecha_formateada
                   

                   #🌟Calculos

                   #total ventas
                   csv["Total Ventas"] = csv["Cantidad Vendida"].mul(csv["Precio"])
                   total_ventas_dinero = csv["Total Ventas"].sum()
                   

                   print(f"El total de ventas en dinero es $ {total_ventas_dinero } ")
                   
                   #total productos vendidos

                   totalProductos_vendidos = csv["Cantidad Vendida"].sum()

                   print(totalProductos_vendidos)  

                   #promedio de ventas
                    
                   ticket_promedio = csv["Total Ventas"].mean()

                   print(f"El promedio de ventas {ticket_promedio}")

                   #producto mas vendido

                   producto_vendidoMax = csv.groupby(["Nombre Producto", "Categoria", "Precio", "Fecha", "Total Ventas"])["Cantidad Vendida"].max().reset_index()


                   #Categoria con mas ingresos

                   agrupando_categorias = csv.groupby('Categoria')["Precio"].sum().sort_values(ascending=False)
                   print(agrupando_categorias)

                   return csv, total_ventas_dinero, totalProductos_vendidos,ticket_promedio, producto_vendidoMax, agrupando_categorias
                   
        else:
            print("❌ No se encontro ningun archivo csv.")
            return None
        
    except Exception as e:
        print(f"Hubo un error al encontrar el archivo: {e}")
        return None

