async function cargarConfiguracion() {
    const respuesta = await fetch("/api/config");  // Trae el valor de api/config 

    if (!respuesta.ok) {  // Si no hay respuesta, lanza error
        throw new Error("No se pudo cargar");
    }

    const datos = await respuesta.json();
    document.querySelector("#titulo")  // Con la llave obtiene el valor de esa llave
        .textContent = datos.titulo;
}

cargarConfiguracion();

