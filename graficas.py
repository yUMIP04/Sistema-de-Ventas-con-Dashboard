import pandas as pd
import plotly.express as px
import os

def Create_Graficas (archivo_csv, filtro_fecha_inicio = None, filtro_fecha_fin = None, filtro_categoria = None, filtro_producto = None):


    if not os.path.exists(archivo_csv):
        print("❌ El archivo no existe")
        return None

    #LIMPIANDO ARCHIVOS CSV

    datos_csv = pd.read_csv(archivo_csv)

    
    ventas = datos_csv["Cantidad Vendida"].astype(str).str.lower().str.replace("vendidos", "").str.replace("vendidas", "").str.replace("productos", "").str.replace("cantidad", "").str.strip()
    datos_csv["Cantidad Vendida"] = ventas.astype('int')
    
    
    datos_csv["Precio"] = datos_csv["Precio"].astype(str).str.replace("$", "", regex=False).str.replace(",", "", regex=False).str.strip().astype('float')
    
    
    datos_csv["Fecha"] = pd.to_datetime(datos_csv["Fecha"], dayfirst=True, errors='coerce')
    
    
    datos_csv["Ingresos Totales"] = datos_csv["Precio"] * datos_csv["Cantidad Vendida"]

    datos_csv["Nombre Producto"] = datos_csv["Nombre Producto"].str.lower().str.strip()

    datos_csv["Categoria"] = datos_csv["Categoria"].str.lower().str.strip()
    
    


   #FILTROS

    if filtro_fecha_inicio and filtro_fecha_fin:
        inicio = pd.to_datetime(filtro_fecha_inicio, dayfirst=True)
        fin = pd.to_datetime(filtro_fecha_fin, dayfirst=True)
        datos_csv = datos_csv[(datos_csv["Fecha"] >= inicio) & (datos_csv["Fecha"] <= fin)] 

    if filtro_categoria:
        datos_csv = datos_csv[datos_csv["Categoria"] == filtro_categoria]

    if filtro_producto:
        datos_csv = datos_csv[datos_csv["Nombre Producto"] == filtro_producto]


   #CREANDO GRAFICAS (LOGICA)

    div_barras = ""
    div_lineas = ""
    div_pastel = ""
    #Grafica de Barras
    try:
      
        tabla_barras = datos_csv.groupby("Nombre Producto")["Cantidad Vendida"].sum().reset_index()
        Grafica_Barras = px.bar(tabla_barras, x="Nombre Producto", y="Cantidad Vendida", title="Ventas por producto")
        div_barras =   Grafica_Barras.to_html(full_html = False, include_plotlyjs="cdn")
    except Exception as e:
        print(f"Hubo un error al Generar la grafica de barras: {e}")

    # Grafica de Lineas
    try:
        tabla_lineas = datos_csv.groupby(['Fecha', 'Nombre Producto'])['Precio'].sum().reset_index()
        Grafica_Lineas = px.line(tabla_lineas, x='Fecha', y='Precio', color='Nombre Producto', title='Ventas por Fecha y Producto')
        div_lineas = Grafica_Lineas.to_html(full_html = False, include_plotlyjs=False)
    except Exception as e:
        print(f"Hubo un error al crear la grafica de lineas: {e}")

   
    try:
        tabla_pastel = datos_csv.groupby('Categoria')["Ingresos Totales"].sum().reset_index()
        Grafica_Pastel = px.pie(tabla_pastel, values="Ingresos Totales", names="Categoria", title="Distribucion por Categoria")
        div_pastel = Grafica_Pastel.to_html(full_html=False, include_plotlyjs=False)
    except Exception as e:
        print(f"Hubo un error al crear la grafica de pastel: {e}")

    #Creacion de graficas
    #Grafica_Barras.show()
    #Grafica_Lineas.show()
    #Grafica_Pastel.show()
    
    
   
    
    return div_pastel, div_lineas, div_barras

