# Algoritmos

Cómo hacer para restar dos números, 5 y 1, sin usar una resta. El resultado tiene que ser 4. Crear una tercera variable - a la variable "1" le vamos sumando 1 y vamos comprobando que sea igual; si no es igual, sumamos también a la tercera variable.

```js
function sinRestar (num1, num2) {
  let num3 = 0;
  for (i = num2; num1 > i ; i++) {
    num3 += 1;
  }
  console.log('valor final: ' + num3)
}

sinRestar(9,4)
```

Multiplicar sin multiplicar

```js
let sinMulti = (num1, num2) => {
  let num3 = 0;
  for (i = 1; i <= num2 ; i++){
    num3 += num1
  }
  console.log(num3);
}
```

Dividir sin dividir

```js
let sinDiv = (num1, num2) => {
  let num3 = 0;
  for (i = 1; num1 >= num2 ; i++){
    num3++;
    num1 -= num2;
  }
  console.log(num3);
}
```
