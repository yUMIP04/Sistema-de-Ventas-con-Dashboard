import Get_PDF from "../api/viewHistorial.js";

const BodyTable = document.querySelector(".tablaCuerpo-Historial");

 async function LlenarTabla(datos) {

  Object.values(datos.pdf).forEach(info =>{

    console.log(info);
    if(info){

      const fila = document.createElement("tr");

      fila.innerHTML=`
      <td>${info[0]}</td>
      <td>${info[1]}</td>
      <td>${info[2]}</td>
      <td> <td><a href="/api/ver_pdf/${info[0]}" target="blank" ><i class="bx bx-eye" /></i></a>
               <a href="/api/descargarPDF/${info[0]}" class="btn-descargar"  download><i class="bx bx-folder-down-arrow"></i></a>
                    <a href="/api/eliminar/${info[0]}" class="btn-eliminar"><i class="bx bx-trash" /></i></a>
                </td></td>
      `
      BodyTable.appendChild(fila);

      const btn_delete = fila.querySelector(".btn-eliminar");
      const btn_descargar = fila.querySelector("btn-descargar");

      btn_delete.addEventListener("click", (e) =>{
        e.preventDefault();

        if(btn_delete){
          BodyTable.removeChild(fila);

          console.log("Eliminando archivo...");
        }
      })
    }
  })
}

const FuncionApi = await Get_PDF();
LlenarTabla(FuncionApi);

