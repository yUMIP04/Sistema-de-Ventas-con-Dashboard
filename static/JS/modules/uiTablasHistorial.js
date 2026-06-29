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
                <td><a href=""><i class="bx bx-eye" /></i></a>
                    <a href=""><i class="bx bx-trash" /></i></a>
                </td>
    `
    BodyTable.appendChild(fila);
    
  })
}

console.log(FuncionApi);
LlenarTabla();