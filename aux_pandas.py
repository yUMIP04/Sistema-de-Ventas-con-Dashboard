import pandas as pd
import os

def ProcesamientoDatos_CSV(archivo_csv):

  archivo_csv = f'static/uploads/CSV/{archivo_csv}'
  archivo_pandas = pd.read_csv(archivo_csv)

#🌟Revisar que el archivo no este vacio
  if archivo_pandas.empty:
    print("❌ El archivo esta vacio o no tiene Datos.")

  else:
    print("🥳 El archivo contiene Datos.")

     #🌟Que el archivo tenga las columnas que debe traer
  verificar_Archivo = archivo_pandas.columns

  columnas_obligatorias = ['Nombre Producto',  'Categoria', 'Precio', 'Cantidad Vendida', 'Fecha']

  for columna in columnas_obligatorias:
      
    if columna in verificar_Archivo:

      print("🥳Las columnas se encuentran en este archivo")

    else: 

      print("❌Las o alguna columna no se encuentra en el archivo")

        #🌟total ventas
  pandas_precio = archivo_pandas["Precio"].str.replace("$", "")
  pandas_ventas =archivo_pandas["Cantidad Vendida"].str.replace("vendidos", "").str.replace("vendidas", "")

  precio_int = pandas_precio.astype('float')
  ventas_int = pandas_ventas.astype('int')

  Precio_Ventas = precio_int * ventas_int
  
  TotalMonetario_Ventas = Precio_Ventas.sum()

  #🌟 total productos vendidos

  TotalProduct_Vendidos = sum(ventas_int)

  #🌟 promedio de ventas

  Promedio_Ventas = precio_int.mean()
  
  #🌟 categoria con mas ingresos
  archivo_pandas["Precio"] = pandas_precio.astype('float')

  agrupando_categorias = archivo_pandas.groupby('Categoria')["Precio"].sum().sort_values(ascending=False)

  #🌟 producto mas vendido
  NombreProducto_tabla = archivo_pandas["Nombre Producto"]

  datosMax ={
    "Nombre Producto": NombreProducto_tabla,
    "Cantidad Vendida": ventas_int
  }

  TablaProductos_Max = pd.DataFrame(datosMax)

  ProductoMax_Vendido = TablaProductos_Max.sort_values(by='Cantidad Vendida', ascending=False)

  print(ProductoMax_Vendido)

  print(agrupando_categorias)
  #🌟 salidas de la consola
  print(f"Total de ventas:${TotalMonetario_Ventas}.")
  print(f"Cifra de productos vendidos: {TotalProduct_Vendidos} piezas de toda la tienda.")
  print(f"Promedio de ventas es: {Promedio_Ventas}")

ProcesamientoDatos_CSV("archivo.csv")