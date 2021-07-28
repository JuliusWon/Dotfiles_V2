#bin/bash
#qtile
if [ $1 == 'qtile' ]
then
	rm -rf ~/Utilities/git-cloning/Dotfiles_V2/qtile/
	cp -r ~/.config/qtile ~/Utilities/git-cloning/Dotfiles_V2/
fi
#neovim
if [ $1 == 'nvim' ]
then
	rm -rf ~/Utilities/git-cloning/Dotfiles_V2/neovim/
	cp -r ~/.config/nvim ~/Utilities/git-cloning/Dotfiles_V2/
fi
#rofi
if [ $1 == 'rofi' ]
then
	rm -rf ~/Utilities/git-cloning/Dotfiles_V2/rofi/
	cp -r ~/.config/rofi/ ~/Utilities/git-cloning/Dotfiles_V2/
fi
#kitty
if [ $1 == 'kitty' ]
then
	rm -rf ~/Utilities/git-cloning/Dotfiles_V2/kitty/
	cp -r ~/.config/kitty/ ~/Utilities/git-cloning/Dotfiles_V2/
fi
