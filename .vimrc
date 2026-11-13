:set number
set nocompatible
set encoding=utf-8
set hidden
set history=1000
syntax on
set number
set relativenumber
set laststatus=2
set showcmd
set wildmenu
set lazyredraw
set autoindent
set smartindent
set expandtab
set tabstop=4
set shiftwidth=4
set incsearch
set hlsearch
set ignorecase
set scrolloff=999
set textwidth=80
set formatoptions+=tcrq
set colorcolumn+=1
set showmatch
set splitbelow splitright
set timeoutlen=300
set ttimeoutlen=10

let mapleader = " "

inoremap jk <Esc>
tnoremap jk <Esc>

nnoremap <Leader>n :NERDTreeToggle<CR>
nnoremap <Leader>f :NERDTreeFind<CR>

nnoremap <Leader>p :CtrlP<CR>
nnoremap <Leader>m :CtrlPMRUFiles<CR>
nnoremap <Leader>b :CtrlPBuffer<CR>

nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

nnoremap <Leader>v :vsplit<CR>
nnoremap <Leader>s :split<CR>

nnoremap <leader>t :below term ++rows=12 ipython --no-autoindent<CR>
nnoremap <leader>r :w<CR>:below term ++rows=12 ipython -i %<CR>
nnoremap <leader>q :bd!<CR>
tnoremap <leader>q <C-w>:bd!<CR>
tnoremap <Esc> <C-\><C-n>

call plug#begin()
Plug 'hdima/python-syntax'

" Appearance
Plug 'catppuccin/vim', { 'as': 'catppuccin', 'branch': 'main' }
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'morhetz/gruvbox'

" Navigation
Plug 'preservim/nerdtree'

" Editing Productivity
Plug 'Vimjas/vim-python-pep8-indent'
Plug 'preservim/nerdcommenter'
Plug 'jiangmiao/auto-pairs'
Plug 'tpope/vim-surround'

" Python additions
Plug 'jpalardy/vim-slime' 

call plug#end()

let g:airline_powerline_fonts = 1
let g:catppuccin_flavor = "mocha"

let python_highlight_all = 1

" NERDTree Tweaks
let NERDTreeShowHidden = 1
let NERDTreeWinSize = 26
let NERDTreeAutoDeleteBuffer = 1
let NERDTreeMinimalUI = 1
let NERDTreeIgnore = ['\.pyc$', '\~$', '__pycache__$', '\.egg-info$']

let g:slime_target = "vimterminal"
let g:slime_python_ipython = 1 

set termguicolors

" Force 256-color support and set terminal codes for true color environments
set t_Co=256
if exists('+termguicolors')
  let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
  let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"
  set termguicolors
endif

colorscheme catppuccin
highlight ColorColumn guibg=#313244 ctermbg=236

" Native Tab / Shift-Tab completion (works regardless of plugins)
inoremap <expr> <Tab>   pumvisible() ? "\<C-n>" : (col('.') > 1 && getline('.')[col('.') - 2] =~ '\k') ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"
inoremap <expr> <CR>    pumvisible() ? "\<C-y>" : "\<CR>"

" Enable built-in Python 3 omni-completion (works for imports & object methods!)
autocmd FileType python setlocal omnifunc=python3complete#Complete

" Trigger omni-completion easily with Ctrl+Space (or Ctrl+@ in many terminals)
inoremap <C-Space> <C-x><C-o>
inoremap <C-@> <C-x><C-o>

autocmd FileType python setlocal keywordprg=python3\ -m\ pydoc

" Tell <C-n> / Tab completion to include dictionary words
set complete+=k
autocmd FileType python setlocal dictionary+=~/.vim/python_dict.txt


augroup EnforceLineWrapping
    autocmd!
    autocmd FileType * setlocal textwidth=80 formatoptions+=trcq colorcolumn=81
augroup END
