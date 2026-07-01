import Get_PDF from "../api/viewHistorial.js";

const BodyTable = document.querySelector(".tablaCuerpo-Historial");

  const FuncionApi = [await Get_PDF()];

  
async function LlenarTabla() {
  
  FuncionApi.forEach(info =>{
    
    const fila = document.createElement("tr");

    fila.innerHTML =`
      <td>${info.nombre_PDF}</td>
                <td>${info.Fecha}</td>
                <td>${info.Creador}</td>
                <td><a href="/api/ver_pdf/${info.nombre_PDF}" target="blank" ><i class="bx bx-eye" /></i></a>
               <a href="/api/descargarPDF/${info.nombre_PDF}" class="btn-descargar"  download><i class="bx bx-folder-down-arrow"></i></a>
                    <a href="/api/eliminar/${info.nombre_PDF}" class="btn-eliminar"><i class="bx bx-trash" /></i></a>
                </td>
    `
    BodyTable.appendChild(fila);
    
    const btn_delete = fila.querySelector(".btn-eliminar");
    const btn_descargar = fila.querySelector(".btn-descargar");

    btn_delete.addEventListener("click", (e) =>{

      e.preventDefault();
      
      if(btn_delete){

        BodyTable.removeChild(fila);

        console.log("Eliminando del fronted la informacion del archivo...");
      }
    })

    

  })
}

console.log(FuncionApi);
LlenarTabla();