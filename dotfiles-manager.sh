#bin/bash
#qtile
# CloningPath=~/utils/Dotfiles_V2
CloningPath=~/Utilities/git-cloning/Dotfiles_V2/
if [ $1 == 'qtile' ]
then
	rm -rf $CloningPath/qtile/
	echo $CloningPath/qtile/
	cp -r ~/.config/qtile $CloningPath
fi
#neovim
if [ $1 == 'nvim' ]
then
	rm -rf $CloningPath/nvim/
	echo $CloningPath/nvim/
	cp -r ~/.config/nvim $CloningPath
fi
#rofi
if [ $1 == 'rofi' ]
then
	rm -rf $CloningPath/rofi/
	echo $CloningPath/rofi/
	cp -r ~/.config/rofi/ $CloningPath
fi
#kitty
if [ $1 == 'kitty' ]
then
	rm -rf $CloningPath/kitty/
	echo $CloningPath/kitty/
	cp -r ~/.config/kitty/ $CloningPath
fi
#dunst
if [ $1 == 'dunst' ]
then
	rm -rf $CloningPath/dunst/
	echo $CloningPath/dunst/
	cp -r ~/.config/dunst/ $CloningPath
fi
#Firefox
if [ $1 == 'firefox' ]
then
	rm -rf $CloningPath/Firefox/Chrome/
	echo $CloningPath/Firefox/Chrome/
	cp -r /home/julius/.mozilla/firefox/svbvp17k.default-release/chrome/ $CloningPath/Firefox/
fi
