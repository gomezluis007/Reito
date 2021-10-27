function muestraModal(url, titulo){
    document.getElementById('formEliminar').action=url;
    document.getElementById('texto').innerHTML= `¿Deseas eliminar el Reito hacia ${titulo}?`
}
