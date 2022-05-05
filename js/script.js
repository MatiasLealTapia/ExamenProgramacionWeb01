$(document).ready(function() {
    $("#error").hide();
    $("#formulario").submit(function() {
        var mensaje = "";

        if ($("#calificaciones").val() == 0) {
            mensaje = "Elija una calificaci&oacute;n";
        }

        if (mensaje != "") {
            $("#error").html(mensaje);
            $("#error").show();
            event.preventDefault();
        } else if (mensaje == "") {
            alert("Tu comentario se envio correctamente. Gracias!")
        }
    })
});

$(document).ready(function() {
    let url = 'https://fakestoreapi.com/products'
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
                // $("#productos").append("<tr><td>"+ item.id+
                //                         "</td><td>" + item.title+
                //                         "</td><td><img src='"+item.image+"' style='width: 100px; height: 100px;''>"+
                //                         "</td><td>"+item.descriptin+"</td></tr>");
                // tarjeta = ("<div class='col'>"+
                //     "<div class='card shadow-sm'>"+
                //     "<a href='./productocompra.html'><img src="+item.image+" alt='logo.png' class='bd-placeholder-img card-img-top' width='100%' height='225' role='img'></a>"+
                //     "<div class='card-body'>"+
                //         "<p class='card-text'>Cama de relajaci&oacute;n para mascota tipo Dona Bicolor.</p>"+
                //         "<div class='d-flex justify-content-between align-items-center'>"+
                //         "<small class='text-muted'>$10.000</small>"+
                //         "</div>"+
                //     "</div>"+
                //     "</div>"+
                // "</div>"
                //     );
                // $("productos").append("<div class='col'>"+
                //     "<div class='card shadow-sm'>"+
                //     "<a href='./productocompra.html'><img src="+item.image+" alt='logo.png' class='bd-placeholder-img card-img-top' width='100%' height='225' role='img'></a>"+
                //     "<div class='card-body'>"+
                //         "<p class='card-text'>Cama de relajaci&oacute;n para mascota tipo Dona Bicolor.</p>"+
                //         "<div class='d-flex justify-content-between align-items-center'>"+
                //         "<small class='text-muted'>$10.000</small>"+
                //         "</div>"+
                //     "</div>"+
                //     "</div>"+
                // "</div>"
                //     );
                // $tarjetas.innerHTML = tarjeta
                // $("#imagen-productos").append('<a href="./productocompra.html"><img src='+item.image+' alt="logo.png" class="bd-placeholder-img card-img-top" width="100%" height="225" role="img"></a>')
                // $("#titulo-productos").append('<p class="card-text">'+item.title+'.</p>')
                // $("#precio-productos").append('<small class="text-muted">'+item.price+'</small>')
                $("#productos").append('<div class="col"> <div class="card shadow-sm" id="imagen-productos"> <a href="./productocompra.html"><img src='+item.image+' alt="logo.png" class="bd-placeholder-img card-img-top" width="100%" height="225" role="img"></a> <div class="card-body" id="titulo-productos"> <p class="card-text">'+item.title+'.</p> <div class="d-flex justify-content-between align-items-center" id="precio-productos"> <small class="text-muted">$'+item.price+'</small> </div></div></div></div>')
            });
        })
        .then(() => console.log(dataStore))
        .catch(error => console.log(error))
        .finally(() => {
            $(".loading-screen").hide();
        })
});

function pierdeFoco() {
    if ($("#calificaciones").val() != 0) {
        mensaje = "";
        $("#error").hide();
    }
}




// $(document).ready(function() {
//     $("body").hide();
// })
// window.onload = function() {
//     alert("Cargó la página");
//     $("body").show();
// };