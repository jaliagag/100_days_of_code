let highAndLow = (n) => {
  let a = n.split(" ")
  console.log(a)
  let low = a[0]
  let high = a[0]
  for (const item of a){
    console.log(item)
    if (parseInt(item) > parseInt(high)) {
      high = item
    }
    if (parseInt(item) < parseInt(low) ) {
      low = item
    }
  }
  return high + " " + low
}

console.log(highAndLow(("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214"))
