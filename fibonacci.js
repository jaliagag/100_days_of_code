function fibo(x) {
  let a = 0;
  let b = 1;
  console.log(1)
  for(i = 0; i < x; i++){
    let c = a + b;
    console.log(c)
    a = b
    b = c
  }
}

fibo(64)
