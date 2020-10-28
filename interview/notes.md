# Problemas

## 1

- Input: string con un texto
- Output: número de apariciones de cada palabra

```md
Hola qué tal, bienvendios un día más a BettaTech. En el vídeo de hoy vamos a resolver problemas.
```

```js
let text = "";

function normalize(word: string) {
    return word.toLowerCase().replace(/[.!,]/g, "");
}
// pasar todo a lower case y eliminar puntos, exclamaciones y comas
function wordRepeitions(text: string) {
    let dict; {[ key; string]: number} = {};
    let separatedWords = text.split(" ");
    for (let word of separatedWords) {
        if (normalize(word) in dict) {
            ++dict[normalize(word)];
        } else {
            dict[normalize(word)] = 1;
        }
    }
    console.log(dict);
}
```

## Estructura de Datos

Formas de guardar y gestionar información.

- <https://www.educative.io/blog/data-strucutres-hash-table-javascript>
- <https://medium.com/techwomenc/estructuras-de-datos-a29062de5483>
- <https://github.com/trekhleb/javascript-algorithms>
- <https://www.codeproject.com/articles/669131/data-structures-with-javascript#:~:text=%20Data%20Structures%20with%20JavaScript%20%201%20Stack.,of%20groups%20of%20nodes%20which%20together...%20More%20>
- <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures>
- <https://data-flair.training/blogs/javascript-data-structures/>
- 
