/*API PARA VER HISTORIAL */

export default async function Get_PDF() {

    try{

        const API =await fetch("/api/obtenerPDF",{
            method: 'GET'
        })

        const datos = await API.json();

        return datos;

    }catch(e){

        console.error(`Hubo un error al obtener la informacion de la API: ${e}`);
    }
    
}

