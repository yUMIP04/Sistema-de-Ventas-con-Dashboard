import FiltrarFecha_PDF from "../api/ViewFiltrosHistorial.js";

const FormularioFiltros = document.getElementById("form-filtros");




async function Formulario_Filtros() {

    FormularioFiltros.addEventListener("submit", async (e) =>{
        e.preventDefault();

        const datosForm = new FormData(FormularioFiltros);
        let datoFecha = datosForm.get("fecha-Filtro");
        try{
        const API_filtrarFecha = await FiltrarFecha_PDF(datoFecha);

        if (API_filtrarFecha){

            console.log("Si existe una coincidencia");
        }

        } catch(e){
            console.error(`Hubo un error al encontrar una coincidencia`);
        }
    })

 }



await Formulario_Filtros();