// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

// Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

// Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)

arrayazo = []
sumado = ''
function solution(number){
  queSos = typeof(number)
  console.log(queSos)
  if (queSos == 'number'){
    number = parseInt(number - 1)
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
  } else {
    console.log('no es un número')
  }
  

  
}

solution(123);
console.log(arrayazo)
console.log(sumado)
