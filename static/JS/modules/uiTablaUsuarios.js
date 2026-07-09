import GetUsuarios from "../api/ViewUsuarios.js";
import Eliminar_Usuarios from "../api/ViewEliminarUsuario.js";

const TablaUsuarios = document.querySelector(".Tabla-Usuarios");
const CuerpoTabla = document.querySelector(".bodyUsuarios");

function Tabla_Usuarios(datos) {

    let contador = 0;

    CuerpoTabla.innerHTML = '';
    
    Object.values(datos.usuarios).forEach(nombres =>{

        contador++;

        const fila = document.createElement("tr");

        

        fila.innerHTML= `
         <td>${contador}</td>
                    <td>${nombres}</td>
                    <td> <a href="" class="btn-eliminar" title="Eliminar">
        <i class="bx bx-trash bg-red-600 text-[#FFFFFF] p-2 rounded-md text-lg hover:bg-red-700 transition-colors duration-200 ease-in-out"></i>
      </a></td>
        `;

        CuerpoTabla.appendChild(fila);

        const btn_eliminar = fila.querySelector(".btn-eliminar");

        btn_eliminar.addEventListener("click", async  (e) =>{

            e.preventDefault();

            const APIDelete = await Eliminar_Usuarios(nombres);

            if(APIDelete){

                try{
                    console.log("Eliminando usuario...");
                    CuerpoTabla.removeChild(fila);
                    console.log("El usuario se elimino con exito");

                }catch(e){

                    console.log(`Hubo un error al eliminar el usuario:${e}`);
                }
            }
             
        })
    })

}

const ApiGetUsuarios = await GetUsuarios();

Tabla_Usuarios(ApiGetUsuarios);

console.log("🥳Si funciona el ui para la tabla usuarios");