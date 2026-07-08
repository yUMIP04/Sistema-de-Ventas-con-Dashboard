import GetUsuarios from "../api/ViewUsuarios.js";

const TablaUsuarios = document.querySelector(".Tabla-Usuarios");
const CuerpoTabla = document.querySelector(".bodyUsuarios");

function Tabla_Usuarios(datos) {

    let contador = 0;
    
    Object.values(datos.usuarios).forEach(nombres =>{

        

        contador++;

        const fila = document.createElement("tr");

        

        fila.innerHTML= `
         <td>${contador}</td>
                    <td>${nombres}</td>
                    <td>eliminar</td>
        `;

        CuerpoTabla.appendChild(fila);

    })

}

const ApiGetUsuarios = await GetUsuarios();
console.log( typeof ApiGetUsuarios);

Tabla_Usuarios(ApiGetUsuarios);

console.log("🥳Si funciona el ui para la tabla usuarios");