/*API PARA FILTRAR EL HISTORIAL POR EL NOMBRE ARCHIVO */

export default async function Filtrar_NombreArchivo(nombre_archivo) {

    const API = await fetch(`/api/FiltrarNombreArchivo/${nombre_archivo}`, {

        method:'POST',

        headers:{
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({
            "mensaje": "Se encontraron nombre de archivo",
            archivo: nombre_archivo
        })
    })

    const datos = API.json();

    return datos;
}