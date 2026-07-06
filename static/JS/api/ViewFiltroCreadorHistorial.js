/*API PARA FILTRAR EL CREADOR EN HISTORIAL */

export default async function FiltroCreadorPDF(nombre_creador) {
    

    try{ 

    const API = await fetch(`/api/FiltrarCreador/${nombre_creador}`, {

        method: 'POST',

        headers:{
            'Content-Type': 'application/json'
        },

        body:JSON.stringify({
            "mensaje": "Se encontro al creador",
            creador: nombre_creador
        })
    })

    const datos = API.json;

    return datos;
} catch(e){

    console.error(`Hubo un error al usar la API para el filtro del creador del PDF: ${e}`);
}

}