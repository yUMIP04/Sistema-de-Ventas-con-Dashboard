import pandas as pd
import os

archivo_csv = 'static/uploads/CSV/archivo.csv'

def ProcesamientoDatos_CSV(archivo_csv):

  archivo_pandas = pd.read_csv(archivo_csv)

#🌟Revisar que el archivo no este vacio
  if archivo_pandas.empty:
    print("❌ El archivo esta vacio o no tiene Datos.")

  else:
    print("🥳 El archivo contiene Datos.")

    verificar_Archivo = archivo_pandas.columns

    columnas_obligatorias = ['Nombre Producto',  'Categoria', 'Precio', 'Cantidad Vendida', 'Fecha']

    for columna in columnas_obligatorias:
      
      if columna in verificar_Archivo:

        print("🥳Las columnas se encuentran en este archivo")

      else: 

        print("❌Las o alguna columna no se encuentra en el archivo")

    #🌟Que el archivo tenga las columnas que debe traer

ProcesamientoDatos_CSV(archivo_csv)