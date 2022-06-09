$(document).ready(function() {
    try {
        const getUrlParams = link => {
            const paramsData = link.match(/([^?=&]+)(=([^&]*))/g) || [];
            return paramsData.reduce(
                (a,v) => ((a[v.slice(0, v.indexOf('='))] = v.slice(v.indexOf('=') + 1)), a), {}
            )
        }
        const result = getUrlParams(location.href);
        Object.entries(result).forEach(par =>{
            const clave = par[0];
            let valor = par[1];
            if(clave == 'category'){
                return url = 'https://matiaslealtapia.github.io/APItest/productos/'+valor+'.json'
            }
            const valorError = valor.substring(0,1)+'#'
            if(valor == valorError){
                valor = valor.substring(0,1)
            }
            if(clave == 'id'){
                return id = valor
            }
        })
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
                    if(item.id == id){
                        let precioclp = Math.trunc(item.price*865.83)
                        function format(num) {
                            var array = num.toString().split('');
                            var index = -3;
                            while (array.length + index > 0) {
                                array.splice(index, 0, ',');
                                index -= 4;
                            }
                            return array.join('');
                        };
                        precioclp = format(precioclp)
                        $("#producto-compra").append('<div class="col"><div class="card shadow-sm"><a href="'+item.image+'"><img src='+item.image+' alt="'+item.image+'.png" class="bd-placeholder-img card-img-top" width="100%" height="225" role="img"></a><div class="card-body"><h6 class="card-text">'+item.title+'</h6><div class="d-flex justify-content-between align-items-center"><small class="text-muted"></small></div></div></div></div><div class="col-8"><div class="card shadow-sm"><h2 class="card-text" style="margin: 20px;">'+item.title+'</h2><h3 style="margin: 20px;">$'+precioclp+' CLP</h3><button class="btn-outline-primary" style="margin: 20px;">COMPRAR</button><button class="btn-outline-secondary" style="margin: 20px;">AÑADIR AL CARRITO</button></div></div>')
                        document.title=item.title;
                    }
                });
            })
            .then(() => console.log(dataStore))
            .catch(error => {
                console.log(error)
                $("#loading").html("Error, por favor intente mas tarde.")
            })
            .finally(() => {
                $(".loading-screen").hide();
            })
    } catch (error) {
        console.log(error)
        $("#loading").html("Error, por favor intente mas tarde.")
    }
});




