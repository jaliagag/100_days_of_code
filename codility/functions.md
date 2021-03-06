# Recommended functions

source: <https://www.freecodecamp.org/news/7-javascript-methods-that-will-boost-your-skills-in-less-than-8-minutes-4cc4c3dca03f/>

1. Spread operator

it expands an array into it's elements

```js
let gato = ["gato", "de", "mierda"];

console.log(...gato);
// gato de mierda
```

2. for...of iterator

The for...of statement loops/iterates through the collection, and provides you the ability to modify specific items. It replaces the conventional way of doing a for-loop.

```js
let gato = ["gato", "duerme", "sueña", "asesino"];

for(const item of gato) {
  console.log(item)
}
```

3. includes()

used to check if a specific string exists in a collection and returns **true** or **false**.

```js
const gato = {"cama", "manta", "calor"};

const esta = gato.includes("manta")

console.log(esta);
// true
```

4. some()

The some() method checks if some elements exists in an array, and returns true or false. This is somewhat similar to the concept of the includes() method, except the argument is a function and not a string.

```js
const age = [1, 2, 3, 4]

age.some(function(person){
  return person >= 3
});

age.some((person) => person >= 3);

// true
```

5. Every()

The every() method loops through the array, checks every item, and returns true or false. Same concept as some(). Except every item must satisfy the conditional statement, otherwise, it will return false.

```js
const age = [12, 15, 23]

age.every((person) => person >= 18); // false
```

6. Filter()

The filter() method creates a new array with all elements that pass the test.

```js
const prices = [1500, 2000, 1300]

prices.filter((asdf) => asdf > 1700) // [2000]
```

7. Map()

The map() method is similar to the filter() method in terms of returning a new array. However, the only difference is that it is used to modify items.

```js
const prices = [1500, 2000, 1300];

prices.map((item) => item*0.75)
```

8. Reduce()

The reduce() method can be used to transform an array into something else, which could be an integer, an object, a chain of promises ( sequential execution of promises) etc. For practical reasons, a simple use case would be to sum a list of integers. In short, it “reduces” the whole array into one value.

```js
const weeklyExpenses = [500, 150, 700, 1100]

weeklyExpenses.reduce((first, last) => first + last );

```






source <https://davidwalsh.name/essential-javascript-functions>
