import Get_PDF from "../api/viewHistorial.js";
import Delete_PDF from "../api/ViewDeleteHistorial.js";

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
       <td><a href="/api/ver_pdf/${info[0]}" target="blank" ><i class="bx bx-eye" /></i></a>
               <a href="/api/descargarPDF/${info[0]}" class="btn-descargar"  download><i class="bx bx-folder-down-arrow"></i></a>
                    <a href="" class="btn-eliminar"><i class="bx bx-trash" /></i></a>
                </td>
      `
      BodyTable.appendChild(fila);

      const btn_delete = fila.querySelector(".btn-eliminar");
      const btn_descargar = fila.querySelector(".btn-descargar");

      btn_delete.addEventListener("click", async (e) =>{
        e.preventDefault();

        const APIDelete = await Delete_PDF(info[0])

        if (APIDelete){

          console.log("Borrando el archivo...");
          BodyTable.removeChild(fila);
          console.log("Se borro de manera correcta la fila");
        }
      })
    }
  })
}

const FuncionApi = await Get_PDF();
LlenarTabla(FuncionApi);

