/* API PARA FILTRAR POR FECHA */

export default async function FiltrarFecha_PDF(fecha) {
    
    try{

    
    const API = await fetch(`/api/FiltrarFecha/${fecha}`, {

        method: 'POST',

        headers:{
            'content-type':'application/json'
        },
        body:JSON.stringify({
            mensaje:"Se encontro la fecha",
            fecha : fecha
        })

    })
        const datos = API.json();
        return datos;

} catch(e){

    console.error(`Hubo un error al filtrar los datos por medio de la API: ${e}`);
}

}