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
    $("body").hide();
})
window.onload = function() {
    alert("Cargó la página");
    $("body").show();
};