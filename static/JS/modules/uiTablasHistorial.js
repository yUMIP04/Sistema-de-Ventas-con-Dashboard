import Get_PDF from "../api/viewHistorial.js";

const BodyTable = document.querySelector(".tablaCuerpo-Historial");

  const FuncionApi = await Get_PDF();


console.log(FuncionApi);