function solution (n) {
  let highest = 0;
  for (const item of n) {
    if (-item in n) {
      if (-item > highest) {
	highest = -item;
      }
    } 
  }
    return highest; 
}


console.log(solution([3, 2, -2, 5, -3]))
