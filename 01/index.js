let sumate = (numero) => {
    let letra = numero.toString();
    let output = [];
    if (numero >= 10) {
        for(var i = 0, len = letra.length; i < len; i += 1) {
            output.push(+letra.charAt(i));
            console.log(output);
        }
    } else {
        console.log('menor a 10')
    }
}

sumate(10)