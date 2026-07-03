/*API PARA ELIMINAR PDF */

async function Delete_PDF(nombre) {
    
    const API = await fetch(`/api/eliminar/${nombre}`,{

        method: 'DELETE'
    })
}