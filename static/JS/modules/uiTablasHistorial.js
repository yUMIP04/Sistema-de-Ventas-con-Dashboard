import Get_PDF from "../api/viewHistorial.js";
import Delete_PDF from "../api/ViewDeleteHistorial.js";


const BodyTable = document.querySelector(".tablaCuerpo-Historial");
const Form_Filtros = document.getElementById("form-filtros");


export default async function LlenarTabla(datos, callback) {

  if ( callback && typeof callback == 'function'){
    callback();
  }

  if(!datos || !datos.pdf) return;

  BodyTable.innerHTML = '';

  Object.values(datos.pdf).forEach(info =>{

    console.log(info);
    if(info){

      if(info[0] === "nombre_pdf" || info[0] === "nombre_archivo") return;

      const fila = document.createElement("tr");

      fila.innerHTML=`<td>${info[0]}</td>
      <td>${info[1]}</td>
      <td>${info[2]}</td>
      <td>
        <a href="/api/ver_pdf/${info[0]}" target="_blank"><i class="bx bx-eye"></i></a>
        <a href="/api/descargarPDF/${info[0]}" class="btn-descargar" download><i class="bx bx-folder-down-arrow"></i></a>
        <a href="" class="btn-eliminar"><i class="bx bx-trash"></i></a>
      </td>
    `;
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

async function Inicializar_Historial() {
  
  try{
    
   const FuncionApi = await Get_PDF();
   LlenarTabla(FuncionApi);

  }catch(e){
    console.log(`Hubo un error al Inicializar el Historial: ${e}`);
  }
}

Inicializar_Historial();

Form_Filtros.addEventListener("reset", (e) =>{
  
  Inicializar_Historial();
})