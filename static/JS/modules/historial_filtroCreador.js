import FiltroCreadorPDF from "../api/ViewFiltroCreadorHistorial.js";
import LlenarTabla from "./uiTablasHistorial.js";

const Form_Filtros = document.getElementById("form-filtros");

async function FiltrarCreador_Tabla() {
    
    Form_Filtros.addEventListener("submit", async (e) =>{

        e.preventDefault();

        const FormData = new FormData(Form_Filtros);

        console.log(FormData);

        let nombreCreador = FormData.get("nombreCreador-Filtro");

        try{

            const APICreador = await FiltroCreadorPDF(nombreCreador);

            if (APICreador) {

                console.log("Se encontro una o mas coincidencias");
                await LlenarTabla(APICreador);

            }
        }catch(e){

            alert("Ese nombre de usuario no existe o no a registrado nada");
            console.error(`Hubo un error al encontrar una coincidencia: ${e}`);
        
        }

    })
}

await FiltrarCreador_Tabla();