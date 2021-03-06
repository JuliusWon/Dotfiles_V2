# Setup NeoVim
Step 1: Install NeoVim:
```bash
sudo pacman -S nvim
```
Step 2: Install [Vim-Plugged](https://github.com/junegunn/vim-plug):
```bash
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```
Step 3: Copy dotfiles to the right directory:
```bash
git clone 'https://github.com/JuliusWon/Dotfiles_V2.git'
rm -rf ~/.config/nvim
cp -r Dotfiles_V2/nvim .config/nvim	
```
Step 4: Setup CoC autocompletion (optional):
```
#run in neovim
:CocInstall coc-omnisharp
:CocInstall coc-pairs
```
# Setup Qtile:
Step 1: Install Qtile:
```bash
sudo pacman -S qtile
```
Step 2: Clone Repo:
```bash
git clone 'https://github.com/JuliusWon/Dotfiles_V2.git'
```
Step 3: Copy files:
```bash
rm -rf ~/.config/qtile
cp -r Dotfiles_V2/qtile .config/qtile
```
Step 4: Recompile Qtile. On the default config the hotkey for this is Control+Super+R
# Setup Rofi:
Step 1: Install Rofi:
```bash
sudo pacman -S rofi
```
Step 2: Clone Repo:
```bash
git clone 'https://github.com/JuliusWon/Dotfiles_V2.git'
```
Step 3: Copy files:
```bash
rm -rf ~/.config/rofi
cp -r Dotfiles_V2/rofi .config/rofi
```
# Setup Kitty:
Step 1: Install kitty and fonts:
```bash
sudo pacman -S kitty
sudo pacman -S ttc-iosevka
```
Step 2: Clone Repo:
```bash
git clone 'https://github.com/JuliusWon/Dotfiles_V2.git'
```
Step 3: Copy files:
```bash
rm -rf ~/.config/kitty
cp -r Dotfiles_V2/kitty .config/kitty
```
# Setup Dunst:
Step 1: Install Dunst:
```bash
sudo pacman -S dunst
```
Step 2: Clone Repo:
```bash
git clone 'https://github.com/JuliusWon/Dotfiles_V2.git'
```
Step 3: Copy files:
```bash
rm -rf ~/.config/dunst
cp -r Dotfiles_V2/dunst .config/dunst
```
