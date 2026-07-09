/*🌟 API PARA ELIMINAR USUARIOS */

export default async function Eliminar_Usuarios(nombre) {
    
    const API = await fetch(`/api/EliminarUsuario/${nombre}`,{

        method: 'DELETE',

        headers:{
            'Content-Type': 'application/json'
        }
    })

    const datos = await API.json();

    return datos;
}