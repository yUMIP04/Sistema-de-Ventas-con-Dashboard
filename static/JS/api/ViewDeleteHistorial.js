/*API PARA ELIMINAR PDF */

export default async function Delete_PDF(nombre) {
    
    const API = await fetch(`/api/eliminar/${nombre}`,{

        method: 'DELETE',
        headers:{
            'content-Type': 'application/json'
        }
    })

    const datos = API.json();

    return datos;
}