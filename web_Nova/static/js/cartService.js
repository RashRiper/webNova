const cuentaCarritoElement = document.getElementById("cuentaCarrito");

function agregarAlCarrito(producto){
    const memoria = JSON.parse(localStorage.getItem("componente"));
    console.log(memoria);
    let cuenta = 0;
    if(!memoria){
        const nProducto = getNuevoProductoParaMemoria(producto);
        localStorage.setItem("componente",JSON.stringify([nProducto]));
        cuenta = 1;
    } else{
        const indiceProducto = memoria.findIndex(componente => componente.id === producto.id);
        console.log(indiceProducto);
        const nuevaMemoria = memoria;
        if(indiceProducto === -1){
            nuevaMemoria.push(getNuevoProductoParaMemoria(producto));
            cuenta = 1;
        } else{
            nuevaMemoria[indiceProducto].cantidad ++;
            cuenta = nuevaMemoria[indiceProducto].cantidad;
        }
        localStorage.setItem("componente",JSON.stringify(nuevaMemoria));
    }
    actualizarNumCarrito();
    return cuenta;
}





