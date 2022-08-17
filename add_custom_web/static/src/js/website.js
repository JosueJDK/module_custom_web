lista1 = document.getElementsByName("p1");
lista2 = document.getElementsByName("p2");
lista3 = document.getElementsByName("porcent");
for (var x = 0; x < lista1.length; x++) {
    for (var y = 0; y < lista2.length; y++) {
        for (var z = 0; z < lista3.length; z++) {
            v1 = parseFloat(lista1[x].innerHTML)
            v2 = parseFloat(lista2[y].innerHTML)  
            p = ((Math.round(v2) * 100 ) / Math.round(v1))
            const percent = 100 - Math.round(p)
            if(percent == 0){
                lista3[z].innerHTML = "SALE"
            }else{
            lista3[z].innerHTML = Math.round(percent) + "%"}
        }
    }
}