let sumate = (numero) => {
    let letra = numero.toString();
    let output = [];
    let finaloutput = '';
    function bignumber(numero) {
        numero >= 10;
    }
    if (bignumber == true ) {
        for(var i = 0, len = letra.length; i < len; i += 1) {
            output.push(+letra.charAt(i));

        }
    } else {
        console.log('menor a 10')
    }
    for (var l = 0; output.length > l ;l += 1){
        finaloutput = output[l]+output[l-1]
    }
    if (finaloutput)
    console.log(finaloutput);
}

sumate(16)