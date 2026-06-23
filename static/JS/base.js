console.log("Si funciono");

const btn_abrir = document.querySelector(".btn-abrir");
const opciones = document.querySelector(".options");
const div_barra = document.querySelector(".btn-barra");

btn_abrir.addEventListener("click", (e) =>{

    const btn_cerrar = document.createElement("button");
    const icon_cerrar = `<i class="bx bx-caret-big-down" /></i>`;

    opciones.style.display = "flex";

    div_barra.removeChild(btn_abrir);

    btn_cerrar.innerHTML = icon_cerrar;
    btn_cerrar.style.cursor = "pointer";
    div_barra.appendChild(btn_cerrar);

    btn_cerrar.addEventListener("click", (e) =>{

        div_barra.removeChild(btn_cerrar);

        div_barra.appendChild(btn_abrir);
        opciones.style.display="none";
    })
})