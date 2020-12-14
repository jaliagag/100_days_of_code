let filter_list = (n) => {
  let arrayFinal = []
  for (const item of n) {
    if (typeof item == "number" && item >= 0) {
      arrayFinal.push(item)
    }
  }
  return arrayFinal
}

console.log(filter_list([3,"hola",2,34, -1]))
