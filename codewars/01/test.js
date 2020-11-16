let testArray = []

function add(thing){
    if (testArray.includes(thing) == true) {
        return console.log('False')
    } else {
        testArray.push(thing)
        console.log(testArray)
        return 
    }
}

add(1)
add(2)
add(3)
add(1)
add(3)
add(2)

console.log(testArray)