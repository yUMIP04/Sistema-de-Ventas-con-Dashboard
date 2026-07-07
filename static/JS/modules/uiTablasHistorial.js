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

     
fila.className = "hover:bg-gray-50 transition-colors duration-150";

fila.innerHTML = `
  <td class="px-6 py-4 font-medium text-gray-900 text-left break-all">${info[0]}</td>
  <td class="px-6 py-4 text-left whitespace-nowrap">${info[1]}</td>
  <td class="px-6 py-4 text-left">${info[2]}</td>
  <td class="px-6 py-4 text-center whitespace-nowrap">
    <div class="flex items-center justify-center gap-3">
      <a href="/api/ver_pdf/${info[0]}" target="_blank" title="Ver PDF">
        <i class="bx bx-eye bg-[#6FD1D5] text-[#FFFFFF] p-2 rounded-md text-lg hover:bg-[#3B7597] transition-colors duration-200 ease-in-out"></i>
      </a>
      <a href="/api/descargarPDF/${info[0]}" class="btn-descargar" download title="Descargar PDF">
        <i class="bx bx-folder-down-arrow bg-[#D6DB27] text-[#FFFFFF] p-2 rounded-md text-lg hover:bg-yellow-500 transition-colors duration-200 ease-in-out"></i>
      </a>
      <a href="" class="btn-eliminar" title="Eliminar">
        <i class="bx bx-trash bg-red-600 text-[#FFFFFF] p-2 rounded-md text-lg hover:bg-red-700 transition-colors duration-200 ease-in-out"></i>
      </a>
    </div>
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