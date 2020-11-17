function solution(number){
  arrayazo = []
  sumado = '';
  queSos = typeof(number);
  if (queSos == 'number'){
    number = parseInt(number - 1);
    if (number < 0 ) {
      return 0
    } else {
      for (i = 1; i <= number; i++){
	if(i%3 == 0){
	  if(arrayazo.includes(i) == true){
	    // do not add 
	  } else {
	    arrayazo.push(i)
	  }
        }
        if(i%5 == 0){
	 if(arrayazo.includes(i) == true){
	    // do not add
	  } else {
	    arrayazo.push(i)
	  }
	}
      }
    return sumado = arrayazo.reduce((first, last)=> first + last)
    } 
  } else {
    console.log('no es un número')
  }
}