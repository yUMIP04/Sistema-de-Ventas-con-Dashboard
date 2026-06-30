import Get_PDF from "../api/viewHistorial.js";

const BodyTable = document.querySelector(".tablaCuerpo-Historial");

  const FuncionApi = [await Get_PDF()];

  
async function LlenarTabla() {
  
  FuncionApi.forEach(info =>{
    
    const fila = document.createElement("tr");

    const btn_ver = document.createElement("a");
    const btn_delete = document.createElement("a");

    btn_ver.textContent = '<i class="bx bx-eye" /></i>';
    btn_delete.textContent = '<i class="bx bx-trash" /></i>';
    
    fila.innerHTML =`
      <td>${info.nombre_PDF}</td>
                <td>${info.Fecha}</td>
                <td>${info.Creador}</td>
                <td><a href="/api/ver_pdf/${info.nombre_PDF}" target="blank" ><i class="bx bx-eye" /></i></a>
                    <a href=""><i class="bx bx-trash" /></i></a>
                </td>
    `
    BodyTable.appendChild(fila);
    
  })
}

console.log(FuncionApi);
LlenarTabla();