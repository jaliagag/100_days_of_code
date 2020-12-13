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


source <https://davidwalsh.name/essential-javascript-functions>
