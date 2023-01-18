from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess

# @hook.subscribe.startup_once

# def autostart():
    # home = os.path.expanduser('~/.config/qtile/autostart.sh')
    # subprocess.call([home])
autostartscriptpath = '~/.config/qtile/autostart.sh'
mod = "mod4"
terminal = "kitty"
file_manager = "nautilus"
browser = "firefox"
launcher = "rofi -show drun -no-default-config"
launcher = "rofi -show drun -config ~/Downloads/dotfiles-main/rofi/config.rasi"
task_switcher = "rofi -show window -no-default-config"
keys = [
    #Media Control:
    Key([mod], "a", lazy.spawn("amixer -q set Master 10%-"), desc="Volume down"),
    Key([mod], "q", lazy.spawn("amixer -q set Master 10%+"), desc="Volume up"),
    # Key([mod], "~", lazy.spawn("./"+autostartscriptpath), desc="Volume up"),
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    #spawn file manager
    Key([mod,"shift"], "Return", lazy.spawn(file_manager), desc="Launch file manager"),
    #spawn browser
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    #spawn rofi
    Key([mod], "p", lazy.spawn(launcher), desc="Launcher prompt"),
    #spawn rofi window switcher
    Key([mod], "o", lazy.spawn(task_switcher), desc="Task switcher"),
    #lock screen and suspend
    Key([mod], "c", lazy.spawn("betterlockscreen -s"), desc="Lock screen"),
    
    #power menu
    Key([mod], "x", lazy.spawn("arcolinux-logout"), desc="Launches arcolinux powermenu"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(margin = 6, border_focus_stack='#d75f5f'),
    layout.Max(margin = 4, border_focus_stack='#d75f5f'),
    layout.Matrix(margin = 8, border_focus_stack='#d75f5f'),
    # layout.TreeTab(margin = 4, border_focus_stack='#d75f5f'),
]

widget_defaults = dict(
    font='iosevka',
    fontsize=12,
    padding=3,
    background='#24283b.55',
)
extension_defaults = widget_defaults.copy()
screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.TextBox(" "),
                # widget.TextBox("Battery:", foreground="#FF9E64"),
                # widget.Battery(charge_char = 'charging', discharge_char = 'discharging', format = '{char} : {percent:2.0%}', foreground="#FF9E64"),
                widget.TextBox("Mode:", foreground="#F7768E"),
                widget.CurrentLayout(foreground="#F7768E"),
                widget.TextBox(" Volume:",foreground="#FF9E64"),
                widget.Volume(foreground="#FF9E64"),
                widget.TextBox(" "),
                widget.GroupBox(disable_drag = True,invert_mouse_wheel=True, active="#E0AF68",inactive="#444B6A"),
                widget.TextBox(" "),
                widget.Prompt(),
                widget.WindowName(foreground="#7AA2F7"),
                # widget.TextBox("Launcher", mouse_callbacks = {"Button1": lazy.spawn("alacritty")}),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("Press &lt;M-p&gt; for launcher  ", foreground="#ad8ee6"),
                widget.Battery(foreground="#7AA2F7",format ='Battery: {percent:2.0%}'),
                widget.TextBox(" "),
                widget.Systray(),
                widget.TextBox(" "),
                widget.Clipboard(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p',foreground="#9ECE6A"),
                widget.TextBox(" "),
                widget.QuickExit(foreground="#FF9E64"),
            ],
            40,
            margin = 5,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.toggle_floating())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='dock'),  # polydock
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "focus"
wmname = "LG3D"
