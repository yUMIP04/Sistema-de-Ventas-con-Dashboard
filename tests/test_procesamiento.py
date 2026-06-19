import pytest
import pandas as pd
from aux_pandas import ProcesamientoDatos_CSV

@pytest.fixture

def csv_de_juguete(tmp_path):

    datos_falsos = {
        "Fecha": ["15/06/2026"],
        "Categoria": ["Electronica"],
        "Nombre Producto": ["Teclado"],
        "Cantidad Vendida": ["2 productos"],  
        "Precio": ["$100.00"]
    }

    df = pd.DataFrame(datos_falsos)

    ruta_del_Archivo = tmp_path / "ventas_juguete.csv"

    df.to_csv(ruta_del_Archivo, index=False)

    return str(ruta_del_Archivo)

def test_procesamiento_valores_correctos(csv_de_juguete):

    total_dinero, total_productos, ticket_promedio, cat_max = ProcesamientoDatos_CSV(csv_de_juguete)

    assert total_dinero == 200.0
    assert total_productos == 2
    assert ticket_promedio == 200.0
    assert cat_max.lower() == "electronica"