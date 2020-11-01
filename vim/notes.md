# VIM CHEATSHEET
# VIM

| key | acción |
| ---- |---- |
| h | <-- |
| j | abajo |
| k | arrba |
| l | --> |
| w/e | palabra siguiente - también puedo poner un número antes de ese comando para ver cuántas veces quiero que se ejecute|
| b | objeto de texto anterior - lo mismo, le pongo un numero de veces que quiero que se ejecute |
| B | palabra anterior |
| i | insertar antes del caracter |
| a | insertar después del caracter |
| A | ir al final de la línea e insertar |
| o | meter un intro cambiar a la línea nueva y comenzar a editar |
| O | abrir una línea arriba |
| x | eliminar caracter |
| gd | definición de la constante |
| gf | go to file |
| ctrol + o | volver |
| ctrol + i | va al archivo|
| { | párrafo anterior |
| } | párrafo siguiente |
| dw | delete word |
| u | deshacer |
| ctrol + r | rehacer |
| d$ | eliminar todo lo que viene desde el lugar donde estoy hasta el final de la línea |
| d + operadores de movimiento | dw, de, db |
| dnw | cantidad de veces que quiero que se elimine una palabra |
| dd | elimina la línea completamente |
| p | pega después del cursor |
| P | pega antes del cursor |
| r + caracter | reemplazar |
| cw | change word - cambiar palabra |
| ciw | cambiar texto dentro de comillas o la palabra que sea donde esté parado |
| gg | comienzo del archivo |
| G | final del archivo |
| nG | ir a una línea específica |
| / | buscar desde la posición en adelante |
| ? | buscar para atrás |
| % | moverse entre paréntesis o {} |
| 0| ir al inicio de la línea |
| $ | ir al final de la línea |
| :s/reemplazaesto/poresto | reemplazar la primera ocurrencia | 
| :s/reemplazaesto/poresto/g | reemplaza en toda la línea |
| :%s/reemplazaesto/poresto/gc | reemplazar todo el documento y pregunta si estás seguro |
| R | reemplazar |
| modo VISUAL + seleccionar + y | copiar |
| p | pegar |


## Mind you

Los archivos principales y que hay que modificar para modificar la apariencia de nvim están en:

- MAC: ~/.config/nvim > init.vim
- Windows: 
  - C:\Users\jaliaga\AppData\Local\nvim > init.vim

```md
set runtime^=~\.vim runtimepath+=~\.vim\after
let &packpath=&runtimepath
source ~\.vimrc
```

  - C:\Users\jaliaga > .vimrc 








