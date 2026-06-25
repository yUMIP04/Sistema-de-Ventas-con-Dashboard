import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
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

    os.makedirs('static/uploads/IMG_Graficas', exist_ok=True)

    nombre_con_Extension =os.path.basename(archivo_csv) 
    nombre_limpio_csv = os.path.splitext(nombre_con_Extension)[0]

    #Grafica de Barras
    try:
      
        tabla_barras = datos_csv.groupby("Nombre Producto")["Cantidad Vendida"].sum().reset_index()
        Grafica_Barras = px.bar(tabla_barras, x="Nombre Producto", y="Cantidad Vendida", title="Ventas por producto", color_discrete_sequence=['#3B7597'])

        Grafica_Barras.update_layout(
            autosize=True,
            height=280,
            margin = dict(l=10, r=10, t=25, b=10)
        )
        div_barras = Grafica_Barras.to_html(full_html = False, include_plotlyjs="cdn")

        plt.figure(figsize=(6, 3.5))
        plt.bar(tabla_barras["Nombre Producto"], tabla_barras["Cantidad Vendida"], color = "#3B7597")
        plt.title("Ventas por producto")
        plt.xticks(rotation=15)
        plt.tight_layout()
        plt.savefig(f"static/uploads/IMG_Graficas/grafica_Barras_{nombre_limpio_csv}", dpi=200)
        plt.close()

    except Exception as e:
        print(f"Hubo un error al Generar la grafica de barras: {e}")

    # Grafica de Lineas
    try:
        tabla_lineas = datos_csv.groupby(['Fecha', 'Nombre Producto'])['Precio'].sum().reset_index()
        Grafica_Lineas = px.line(tabla_lineas, x='Fecha', y='Precio', color='Nombre Producto', title='Ventas por Fecha y Producto', color_discrete_sequence=['#093C5D', '#3B7597', '#6FD1D7'])
        Grafica_Lineas.update_layout(
            autosize=True, 
            height=280,
              margin=dict(l=10, r=10, t=25, b=10)
        )

        div_lineas = Grafica_Lineas.to_html(full_html = False, include_plotlyjs=False)

        plt.figure(figsize=(6, 3.5))

        for producto, grupo in tabla_lineas.groupby('Nombre Producto'):

            plt.plot(grupo['Fecha'], grupo['Precio'], label=producto, marker='o')

        plt.title('Ventas por Fecha y Producto')
        plt.legend(fontsize=8)
        plt.tight_layout()
        plt.savefig(f"static/uploads/IMG_Graficas/grafica_Lineas_{nombre_limpio_csv}", dpi=200)
        plt.close()

    except Exception as e:
        print(f"Hubo un error al crear la grafica de lineas: {e}")

   
    try:
        tabla_pastel = datos_csv.groupby('Categoria')["Ingresos Totales"].sum().reset_index()
        Grafica_Pastel = px.pie(tabla_pastel, values="Ingresos Totales", names="Categoria", title="Distribucion por Categoria", color_discrete_sequence=['#093C5D', '#3B7597', '#6FD1D7'])
        Grafica_Pastel.update_layout(
              autosize=True, 
            height=280,
              margin=dict(l=10, r=10, t=25, b=10)
        )
        div_pastel = Grafica_Pastel.to_html(full_html=False, include_plotlyjs=False)

        plt.figure(figsize=(6, 3.5))
        plt.pie(tabla_pastel["Ingresos Totales"], labels=tabla_pastel["Categoria"], autopct='%1.1f%%', colors=['#3B7597', '#94B4C6', '#D6E4ED'])
        plt.title("Distribucion por Categoria")
        plt.tight_layout()
        plt.savefig(f"static/uploads/IMG_Graficas/grafica_Pastel_{nombre_limpio_csv}", dpi=200)
        plt.close()
        
    except Exception as e:
        print(f"Hubo un error al crear la grafica de pastel: {e}")
    

    return div_pastel, div_lineas, div_barras