const archivo_csv = document.getElementById("file-csv");
const nombre_archivo = document.getElementById("nombre-archivo");
const btn_seleccionar = document.getElementById("btn-seleccionar");
const btn_subir = document.getElementById("btn-subir");
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