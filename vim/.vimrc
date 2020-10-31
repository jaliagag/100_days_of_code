set number
set mouse=a
set numberwidth=1
set clipboard=unnamed
syntax enable
set showcmd
set ruler
set encoding=utf-8
set sw=2
set laststatus=2


" call plug#begin()
call plug#begin('~\.vim\plugged')

" Temas
Plug 'morhetz/gruvbox'

" IDE
Plug 'easymotion/vim-easymotion'
Plug 'scrooloose/nerdtree'
Plug 'christoomey/vim-tmux-navigator'
" con este plugin, podemos movernos entre los distintos terminales abiertos
" con control + h, j, k y l

call plug#end()

colorscheme gruvbox
let g:gruvbox_contrast_dark= "hard"
" let g:deoplete#enable_at_startup = 1
" let g:jsx_ext_required = 0
let NERDTreeQuitOnOpen=1

let mapleader=" " " cuando quiera usar la tecla leader, va a ser el espacio + otra tecla

nmap <Leader>s <Plug>(easymotion-s2)
" nmap indica que solo funciona en modo normal - espacio + s inicia easymotion
" espacio s > introducir 2 letras > elegir la opción donde quiero ir
nmap <Leader>nt :NERDTreeFind<CR>
" los dos puntos abre la consola - :NERDTreeFind<CR> - cr es la tecla de enter
" dentro de nerdtree entro al menú con la opción 'm'

nmap <Leader>w :w<CR>
nmap <Leader>q :q<CR>



