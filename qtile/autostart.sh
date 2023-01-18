#!/bin/sh
nitrogen --restore &
picom --experimental-backends &
./.screenlayout/normal.sh &
xss-lock --transfer-sleep-lock -- i3lock --nofork --radius=150 --ring-width=15 -f -e --blur=.75 -k --indicator --inside-color=00000000 &
