$(document).ready(function() {
    $("#error").hide();
    $("#formulario").submit(function() {
        var mensaje = "";

        if ($("#id_calificacion").val() == 0) {
            mensaje = "Elija una calificaci&oacute;n";
        }

        if (mensaje != "") {
            $("#error").html(mensaje);
            $("#error").show();
            event.preventDefault();
        }
    })
    $("#formAddProducto").submit(function() {
        var mensaje = "";

        if ($("#id_idCat").val() == 0) {
            mensaje = "Seleccione una categor&iacute;a";
        }

        if (mensaje != "") {
            $("#error").html(mensaje);
            $("#error").show();
            event.preventDefault();
        }
    })
    $("#SuscribirseForm").submit(function() {
        var mensaje = "";

        if ($("#id_donacion").val() < 500) {
            mensaje = "Escoga un monto igual o superior a $500";
        }

        if (mensaje != "") {
            $("#error").html(mensaje);
            $("#error").show();
            event.preventDefault();
        }
    })
    const $seleccionArchivo = document.querySelector("#id_imgPro");
    const $previsualizar = document.querySelector("#imagenPrevisualizada")
    $seleccionArchivo.addEventListener("change", () => {
        const archivo = $seleccionArchivo.files;
        if (!archivo || !archivo.length) {
            $previsualizar.scr = "";
            return;
        }
        const primerArchivo = archivo[0];
        const objectURL = URL.createObjectURL(primerArchivo);
        $previsualizar.src = objectURL;
    });
});

function pierdeFoco() {
    if ($("#id_calificacion").val() != 0) {
        var mensaje = "";
        $("#error").html(mensaje);
        $("#error").hide();
    }
    else{
        var mensaje = "Elija una calificaci&oacute;n";
        $("#error").html(mensaje);
        $("#error").show();
    }
    if ($("#id_idCat").val() != 0) {
        var mensaje = "";
        $("#error").html(mensaje);
        $("#error").hide();
    }
    else{
        var mensaje = "Seleccione una categor&iacute;a";
        $("#error").html(mensaje);
        $("#error").show();
    }
}



// $(document).ready(function() {
//     $("body").hide();
// })
// window.onload = function() {
//     alert("Cargó la página");
//     $("body").show();
// };