#bin/bash
#qtile
CloningPath=~/utils/Dotfiles_V2/
CloningPath=~/Utilities/git-cloning/Dotfiles_V2/
if [ $1 == 'qtile' ]
then
	rm -rf $CloningPath/qtile/
	cp -r ~/.config/qtile $CloningPath
fi
#neovim
if [ $1 == 'nvim' ]
then
	rm -rf $CloningPath/neovim/
	cp -r ~/.config/nvim $CloningPath
fi
#rofi
if [ $1 == 'rofi' ]
then
	rm -rf $CloningPath/rofi/
	cp -r ~/.config/rofi/ $CloningPath
fi
#kitty
if [ $1 == 'kitty' ]
then
	rm -rf $CloningPath/kitty/
	cp -r ~/.config/kitty/ $CloningPath
fi
