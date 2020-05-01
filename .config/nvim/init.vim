let mapleader=","

call plug#begin('~/.local/share/nvim/plugged')
Plug 'ap/vim-css-color'
Plug 'kovetskiy/sxhkd-vim'
Plug 'tpope/vim-commentary'
Plug 'dracula/vim', { 'as': 'dracula' }
Plug 'morhetz/gruvbox'
Plug 'SirVer/ultisnips' | Plug 'honza/vim-snippets'
Plug 'vifm/vifm.vim'
call plug#end()

set number relativenumber
set clipboard+=unnamedplus
set mouse=a
syntax on
set ignorecase
set smartcase
set termguicolors
set wildmode=longest,list,full
set splitbelow splitright
set nobackup
set nowritebackup
set noswapfile
set scrolloff=999
colorscheme gruvbox
set cursorline

map <leader>h :split<Space>
map <leader>v :vsplit<Space>

" split navigation
map <C-h> <C-w>h
map <C-j> <C-w>j
map <C-k> <C-w>k
map <C-l> <C-w>l
map <A-Tab> <c-w><c-w>

" Make adjusing split sizes a bit more friendly
noremap <silent> <C-Left> :vertical resize +3<CR>
noremap <silent> <C-Right> :vertical resize -3<CR>
noremap <silent> <C-Up> :resize +3<CR>
noremap <silent> <C-Down> :resize -3<CR>

nnoremap S :%s//g<Left><Left>

" save and close quickly without having to correct error
command! Q :q
command! W :w
command! WQ :wq
command! Wq :wq

" remove highlighting of search term
map <Leader><Space> :let @/=''<CR>

" resize splits when vim resizes
autocmd VimResized * wincmd =

" remove trailing whitespace on save
autocmd BufWritePre * %s/\s\+$//e
autocmd BufWritepre * %s/\n\+\%$//e

" load xresources automatically
autocmd BufWritePost *Xresources,*Xdefaults !xrdb %

" load sxhkd automatically
autocmd BufWritePost *sxhkdrc !pkill -USR1 -x sxhkd

" load imwheelrc automatically
autocmd BufWritePost *imwheelrc !imwheel -k

" restart bspwm on config edit
autocmd BufWritePost *bspwmrc,*autostart,*external_rules !bspc wm -r

" restart panel on config edit
autocmd BufWritePost *panel,*panel_bar,*panel_colors !pkill -USR2 panel

" source init.vim
autocmd BufWritePost $MYVIMRC source $MYVIMRC

" (vim-commentry) set " to comment string for vifmrc
autocmd FileType vifm setlocal commentstring=\"\ %s

" add shebang depending on extension
autocmd BufNewFile *.py 0put =\"#!/usr/bin/env python\<nl>\"|$
autocmd BufNewFile *.sh 0put =\"#!/usr/bin/env sh\<nl>\"|$

" Set scripts to be executable from the shell
au BufWritePost * if getline(1) =~ "^#!" | if getline(1) =~ "/bin/" | silent !chmod +x <afile> | endif | endif

autocmd FileType python map <buffer> <F5> :%w !python<cr>

"" snippets
" Trigger configuration. Do not use <tab> if you use https://github.com/Valloric/YouCompleteMe.
let g:UltiSnipsJumpForwardTrigger="<tab>"
let g:UltiSnipsJumpBackwardTrigger="<s-tab>"

" If you want :UltiSnipsEdit to split your window.
let g:UltiSnipsEditSplit="vertical"

" return to last edit position
au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
