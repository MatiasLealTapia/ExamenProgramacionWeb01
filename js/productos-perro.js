$(document).ready(function() {
    // let url = 'https://fakestoreapi.com/products'
    let url = 'https://matiaslealtapia.github.io/APItest/productos/perro.json'
    const $cargando = document.getElementById("loading");
    const $tarjetas = document.getElementById("productos");
    fetch(url)
        .then(res => {
            if (res.ok == true) {
                console.log("GET request successful")
            } else {
                console.log("GET request unsuccessful")
            }
            return res
        })
        .then(res => res.json())
        .then(data => {
            dataStore = data
            $.each(data, function(i, item){
                let precioclp = Math.trunc(item.price*865.83)
                $("#productos").append('<div class="col"> <form action="productocompra.html" id="miForm"> <div class="card shadow-sm" id="imagen-productos"> <input type="text" name="category" id="category" value="'+item.category+'" style="display: none;"> <input type="text" name="id" id="id" value="'+item.id+'" style="display: none;"> <img src='+item.image+' alt="logo.png" class="bd-placeholder-img card-img-top" width="100%" height="225" role="img"> <div class="card-body" id="titulo-productos"> <p class="card-text">'+item.title+'.</p> <div class="d-flex justify-content-between align-items-center" id="precio-productos"> <small class="text-muted">$'+precioclp+' CLP</small> <input type="submit" class="btn btn-primary" id="enviar" value="Ver producto"> </div></div></div></form></div>')
            });
        })
        .then(() => console.log(dataStore))
        .catch(error => console.log(error))
        .finally(() => {
            $(".loading-screen").hide();
        })
});