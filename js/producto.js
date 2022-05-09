$(document).ready(function() {
    // let url = 'https://fakestoreapi.com/products'
    let url = 'https://matiaslealtapia.github.io/APItest/productos/perro.json'
    const $cargando = document.getElementById("loading");
    const $tarjetas = document.getElementById("producto-compra");
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
                $("#producto-compra").append('<div class="col"><div class="card shadow-sm"><a href="#"><img src="img/productosperro/Khaki_590x.webp" alt="logo.png" class="bd-placeholder-img card-img-top" width="100%" height="225" role="img"></a><div class="card-body"><h6 class="card-text">Cama de relajaci&oacute;n para mascota tipo Dona Bicolor.</h6><div class="d-flex justify-content-between align-items-center"><small class="text-muted"></small></div></div></div></div><div class="col-8"><div class="card shadow-sm"><h2 class="card-text" style="margin: 20px;">Cama de relajaci&oacute;n para mascota tipo Dona Bicolor.</h2><h3 style="margin: 20px;">$10.000</h3><button class="btn-outline-primary" style="margin: 20px;">COMPRAR</button><button class="btn-outline-secondary" style="margin: 20px;">AÑADIR AL CARRITO</button></div></div>')
            });
        })
        .then(() => console.log(dataStore))
        .catch(error => console.log(error))
        .finally(() => {
            $(".loading-screen").hide();
        })
});