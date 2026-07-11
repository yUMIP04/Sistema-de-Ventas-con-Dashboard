import GetUsuarios from "../api/ViewUsuarios.js";
import Eliminar_Usuarios from "../api/ViewEliminarUsuario.js";

const TablaUsuarios = document.querySelector(".Tabla-Usuarios");
const CuerpoTabla = document.querySelector(".bodyUsuarios");
const AvisoUsuarioExitoso = document.querySelector(".success-user"); 
const FormularioUsuarios = document.querySelector(".Form-Users");
const btn_aceptar = document.querySelector(".aceptar-usuario");

function Tabla_Usuarios(datos) {

    let contador = 0;

    CuerpoTabla.innerHTML = '';
    
    Object.values(datos.usuarios).forEach(nombres =>{

        contador++;

        const fila = document.createElement("tr");

        fila.className = "border-b border-gray-200 hover:bg-gray-50 transition-colors";

        fila.innerHTML= `
         <td class="px-6 py-4 font-medium text-gray-900 text-left break-all">${contador}</td>
                    <td class="px-6 py-4 text-left whitespace-nowrap">${nombres}</td>
                    <td class="text-center"> <a href="" class="btn-eliminar" title="Eliminar">
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


/*🌟Aviso de Usuario registrado */

FormularioUsuarios.addEventListener("submit", (e) =>{

    const data_form = new FormData(FormularioUsuarios);

    const clave = data_form.get("clave");
    const clave_confirm = data_form.get("clave-confirmacion");

    const clave_limpia = clave.trim();
    const clave_confirm_limpia = clave_confirm.trim();

    const claves_iguales = clave_confirm_limpia === clave_limpia;

    if(claves_iguales){

        alert("Se registro un usuario con exito");
    } else{
        e.preventDefault();
        alert("Las contraseñas no coinciden");
    }
})