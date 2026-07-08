/* API PARA VER USUARIOS */

export default async function GetUsuarios() {
    
    try{

    
    const API = await fetch('/api/verUsuario', {

        method: 'GET',

        headers: {
            'Content-Type': 'application/json'
        }
    })

    const resultados = await API.json();

    return resultados;

}catch(e){

    console.error(`Hubo un error al utilizar la API para ver Usuarios: ${e}`);
}

}