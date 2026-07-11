const archivo_csv = document.getElementById("file-csv");
const nombre_archivo = document.getElementById("nombre-archivo");
const btn_seleccionar = document.getElementById("btn-seleccionar");
const btn_subir = document.getElementById("btn-subir");
const btn_aceptar = document.querySelector(".aceptar-pdf");
const cartel_pdf = document.querySelector(".success-pdf");
const FormPdf = document.querySelector(".form-pdf");


console.log("🥳Si funciono");

btn_seleccionar.addEventListener("click", () =>{

   archivo_csv.click();

  
});

archivo_csv.addEventListener("change", () =>{
    console.log("Archivo seleccionado");

    if(archivo_csv.files.length > 0){
        nombre_archivo.innerHTML = `<strong>Archivo Seleccionado: ${archivo_csv.files[0].name}</strong>`;
        
    
    }else{
        nombre_archivo.innerHTML = "<strong>Inserta tu archivo CSV</strong>"
    }
})



   btn_subir.addEventListener("click", (event) =>{

    if(archivo_csv.files.length === 0){

        event.preventDefault();
        alert("Error: No se ha seleccionado ningun archivo aun")
    } else{
        alert("Archivo subido correctamente")
    }
})

/*🌟CARTEL DEL PDF CREADO */

btn_aceptar.addEventListener("click", (e) => {
    e.preventDefault();

    cartel_pdf.classList.remove("flex");
    cartel_pdf.classList.add("hidden");
});

FormPdf.addEventListener("submit", (e) =>{

   const Total_Ventas = document.querySelector(".Total-ventas");
    const Total_ventasValor = Total_Ventas.textContent.trim();

  
    const ventas_totalLimpio = Total_ventasValor.replace(/[$,]/g, "");
    const ventas_totalfloat = parseFloat(ventas_totalLimpio);

    
    if (isNaN(ventas_totalfloat) || ventas_totalfloat <= 0) {
        e.preventDefault(); 
        alert("No se puede producir el PDF porque no hay ventas registradas.");
        return; 
    }

    
    cartel_pdf.classList.remove("hidden");
    cartel_pdf.classList.add("flex");
})

