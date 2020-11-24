function sinRestar (num1, num2) {
  let num3 = 0;
  for (i = num2; num1 > i ; i++) {
    num3 += 1;
  }
  console.log('valor final: ' + num3)
}

// sinRestar(9,4)

let sinMulti = (num1, num2) => {
  let num3 = 0;
  for (i = 1; i <= num2 ; i++){
    num3 += num1
  }
  console.log(num3);
}

// sinMulti(2,2) 

let sinDiv = (num1, num2) => {
  let num3 = 0;
  for (i = 1; num1 >= num2 ; i++){
    num3++;
    num1 -= num2;
  }
  console.log(num3);
}

// sinDiv(100, 5)
