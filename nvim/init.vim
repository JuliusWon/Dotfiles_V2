"Plugins
silent! if plug#begin('~/.vim/plugged')
Plug 'ryanoasis/vim-devicons'
Plug 'tpope/vim-commentary'
Plug 'itchyny/lightline.vim'
Plug 'OmniSharp/omnisharp-vim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'ghifarit53/tokyonight-vim'
Plug 'joshdick/onedark.vim'
Plug 'kyazdani42/nvim-web-devicons'
Plug 'romgrk/barbar.nvim'
Plug 'preservim/nerdtree'
call plug#end()
endif
if (empty($TMUX))
  if (has("nvim"))
    "For Neovim 0.1.3 and 0.1.4 < https://github.com/neovim/neovim/pull/2198 >
    let $NVIM_TUI_ENABLE_TRUE_COLOR=1
  endif
  if (has("termguicolors"))
    set termguicolors
  endif
endif
"General settings
let g:lsc_auto_map = v:true
:set nowrap
:set softtabstop=0 noexpandtab
:set shiftwidth=4
:set tabstop=4
:set nu
:set clipboard=unnamedplus
:set mouse=a
let bufferline = get(g:, 'bufferline', {})
let g:bufferline.animation = v:false
let g:bufferline.tabpages = v:true
"Color Sceme Stuff
let g:onedark_terminal_italics = 1
let g:onedark_hide_endofbuffer = 1
let g:onedark_termcolors = 256
let g:tokyonight_style = "storm"
" syntax on
set termguicolors
let g:tokyonight_enable_italic = 1
colorscheme tokyonight
"Keyboard shortcuts labeled, continues to end of file
"Commenting lines easily
nnoremap <space>/ :Commentary <CR>
" Remap splits navigation to just CTRL + hjkl
nnoremap <C-t> :tabedit <CR> 
nnoremap <C-]> :tabnext <CR>
nnoremap <C-[> :tabprevious <CR>
nnoremap <C-w> :q <CR>
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l
nnoremap <C-b> :b 
" Make adjusing split sizes a bit more friendly
noremap <C-Right> :vertical resize -3<CR>
noremap <C-Left> :vertical resize +3<CR>
noremap <C-Up> :resize +3<CR>
noremap <C-Down> :resize -3<CR>
" Enable snippet completion, using the ultisnips plugin
 let g:OmniSharp_want_snippet=1
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
" nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>
 autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif
 autocmd BufEnter * if winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif
 " Open the existing NERDTree on each new tab.
autocmd BufWinEnter * if getcmdwintype() == '' | silent NERDTreeMirror | endif
" Start NERDTree and put the cursor back in the other window.
autocmd VimEnter * NERDTree | wincmd p
