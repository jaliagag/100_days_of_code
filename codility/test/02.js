let solution = (n) => {
  let sums = {};
  
  for (i=0; i < n.length ;i++) {
    if (n.length%2 == 0) {
      if (i%2 == 0) {
	let a = n[i] + n[i+1];
	if (a in sums){
	  ++sums[a];
	} else {
	  sums[a] = 1;
	}
      }
      if (i == (n.length-1)){
	let a = n[i] + n[i-1];
	if (a in sums){
	  ++sums[a];
	} else {
	  sums[a] = 1;
	}
      }
    }
    if (n.length%2 != 0){
      if (i%2 == 0) {
	let a = n[i] + n[i+1];
	if (a in sums){
	  ++sums[a];
	} else {
	  sums[a] = 1;
	}
      }
    }
  }
  let highest = 0;
  let final = 0;
  let newArr = Object.values(sums)
  
  for (const item of newArr){
    if(item > highest){
      highest = item;
    }
  }

  for(i=0;i<n.length;i++){
    if((n[i]+n[i+1]) == highest){
      final += 1;
    }
  }

  return highest 
}

a = [10, 1, 3, 1, 2, 2, 1, 0, 4]

console.log(solution(a))
