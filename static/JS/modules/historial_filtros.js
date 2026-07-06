import FiltrarFecha_PDF from "../api/ViewFiltrosHistorial.js";
import LlenarTabla from "./uiTablasHistorial.js";

const Form_Filtros = document.getElementById("form-filtros");

async function FiltrarFecha_Tabla() {


    Form_Filtros.addEventListener("submit", async (e) =>{

        e.preventDefault();

         const Form_data = new FormData(Form_Filtros);
     
    console.log(Form_data);

    let fecha_form = Form_data.get("fecha-Filtro");

    try{

    
    const filtrarAPI = await FiltrarFecha_PDF(fecha_form);

   
    if(filtrarAPI){

        console.log("Existe una o mas coincidencias");
        await LlenarTabla(filtrarAPI);
    } 

    } catch(e){

        
       
        console.error(`Hubo un error al encontrar una coincidencia: ${e}`);

    }
    })
}

await FiltrarFecha_Tabla();