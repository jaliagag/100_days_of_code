/*
 * a binary gap within a positive integer N is any maximal sequence of
 * consecutie zeroes that is surrounded by ones at both ends in the binary representation of N
 * 
 * for example, number 9 has binary representation 1001 and contains a binary gap of length 2. the number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
 * the number 20 has binary representation 10100 and contains one binary ap of length 1. the number 15 has binary representation 1111 and has no binary gaps. 
 * the number 32 has binary representation 100000 and has no binary gaps
 *
 * write a function that given a positive integer N, returns the length of its longest ginary gap. the function should return 0 if N doesn't have a binary gap
 *
 * for example given N = 1041 the function should return 5, because N has binary representation 10000010001 and o its longest binary gap is of length 5. given n = 32 the function should return 0, because n has binary representation 1000000 and this no binary gaps
 * write an efficient algorithm for th efollowing assumptions
 *
 * - n is an integer within the rang [1...2, 147, 483, 647]
 * https://www.youtube.com/watch?v=HoT3y-L2t20
 * https://www.youtube.com/watch?v=LE8j4KGoarc
 * https://github.com/search?q=codility
 * https://github.com/yaseenshaik/codility-solutions-javascript
 *
 */

var a = 32

let binGap = (number) => {
  let b = a.toString(2)
  console.log(b)
  let c = b.toString().length
  let countingZeros = 0
  let biggestRun = 0
  let d = b.split("")
  
  // substraction elements
  let range = 0;
  let oneQ = 0;

  for (i = 0 ; c > i ; i++){
    if (d[i] == 1){
      oneQ += 1
      range = (i+1) - range
    }
  }
  console.log(range)
  if (oneQ == 1) {
    return 0
  }
}

binGap(a)






