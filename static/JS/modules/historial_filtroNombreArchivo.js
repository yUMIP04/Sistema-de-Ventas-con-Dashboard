import Filtrar_NombreArchivo from "../api/ViewFiltroNombreArchivo.js";
import LlenarTabla from "./uiTablasHistorial.js";

const Form_Filtros = document.getElementById("form-filtros");

async function FiltrarNombreArchivo_Tabla() {
    

    Form_Filtros.addEventListener("submit", async (e) =>{

        e.preventDefault();

        const form_data = new FormData(Form_Filtros);

        let form_nombreArchivo = form_data.get("nombreArchivo-Filtro");

        try{ 

        
        const API_NombreArchivo = await Filtrar_NombreArchivo(form_nombreArchivo);

        if (API_NombreArchivo){

            console.log("Si hay coincidencias del nombre de archivo");
            await LlenarTabla(API_NombreArchivo);
        }

        }catch(e){

            console.error(`Hubo un error al encontrar coincidencias: ${e}`);
        }
    })
}

await FiltrarNombreArchivo_Tabla();