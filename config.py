# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile           import bar, layout, widget
from libqtile.config    import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy      import lazy
from libqtile.utils     import guess_terminal
from spotify            import Spotify
import os

mod = "mod4"
#terminal = guess_terminal()
terminal = 'alacritty'
# qtile_path = path.join(path.expanduser('~'), ".config", "qtile")

# @hook.subscribe.startup_once
#  def autostart():
#      subprocess.call([path.join(qtile_path, 'autostart.sh')])

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "l",     lazy.layout.left(),             desc="Move focus to left"),
    Key([mod], "j",     lazy.layout.right(),            desc="Move focus to right"),
    Key([mod], "k",     lazy.layout.down(),             desc="Move focus down"),
    Key([mod], "i",     lazy.layout.up(),               desc="Move focus up"),
    Key([mod], "n",     lazy.layout.normalize(),        desc="Reset all window sizes"),
    Key([mod], "w",     lazy.window.kill(),             desc="Kill focused window"),
    Key([mod], "r",     lazy.spawncmd(),                desc="Spawn a command using a prompt widget"),
    Key([mod], "m",     lazy.next_screen(),             desc='Next monitor'),
    Key([mod], "o",     lazy.spawn("rofi -show run")),
    Key([mod], "s",     lazy.spawn("scrot")),
    Key([mod], "e",     lazy.spawn("pcmanfm")),
    Key([mod], "s",     lazy.spawn("spotify")),
    Key([mod], "space", lazy.layout.next(),             desc="Move window focus to other window"),
    
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "l", lazy.layout.shuffle_left(),    desc="Move window to the left"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_right(),   desc="Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(),    desc="Move window down"),
    Key([mod, "shift"], "i", lazy.layout.shuffle_up(),      desc="Move window up"),
    Key([mod, 'shift'], "s", lazy.spawn("scrot -s")),
    Key([mod, 'shift'], "m", lazy.spawn("rofi -show")),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "l", lazy.layout.grow_left(),   desc="Grow window to the left"),
    Key([mod, "control"], "j", lazy.layout.grow_right(),  desc="Grow window to the right"),
    Key([mod, "control"], "k", lazy.layout.grow_down(),   desc="Grow window down"),
    Key([mod, "control"], "i", lazy.layout.grow_up(),     desc="Grow window up"),
    Key([mod, "control"], "q", lazy.shutdown(),           desc="Shutdown Qtile"),
    Key([mod, "control"], "r", lazy.reload_config(),      desc="Reload the config"),
    
   
    Key(['mod1'], "p",  lazy.spawn("playerctl play-pause")),
    Key(['mod1'], "d",  lazy.spawn("playerctl next")),
    Key(['mod1'], "a",  lazy.spawn("playerctl previous")),
    Key(['mod1'], "w",  lazy.spawn("pamixer -i 5")),
    Key(['mod1'], "s",  lazy.spawn("pamixer -d 5")),
    Key(['mod1'], "e",  lazy.spawn("setxkbmap es")),
    Key(['mod1'], "i",  lazy.spawn("setxkbmap us")),
    Key(['mod1'], "l",  lazy.spawn("betterlockscreen -l")),

    
   
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod],"Return", lazy.spawn(terminal),   desc="Launch terminal"),
    Key([mod], "Tab",   lazy.next_layout(),     desc="Toggle between layouts"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
   # Toggle between different layouts as defined below 
]



groups = []

# # FOR QWERTY KEYBOARDS
group_names = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
# # group_labels = ["", "", "", "", "", "", "", "", "", "",]
group_labels = ["", "", "", " ", "", "5", "6", "7", "8", "9"]

# FOR QWERTY KEYBOARDS
# group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

# FOR AZERTY KEYBOARDS
#group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

# group_labels = ["", "", "", "", "", "", "", "", "", "",]
#group_labels = ["Web", "Edit", "Ink", "Gimp", "Meld", "Vlc", "VB", "Thunar", "Mail", "Music",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        # Key([mod], "Tab", lazy.screen.next_group()),
        # Key(["mod1"], "Tab", lazy.screen.next_group()),
        # Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])
# groups = []



# for i in range(len(group_names)):
#     groups.append(
#         Group(
#             name=group_names[i],
#             layout=group_layouts[i].lower(),
#             label=group_labels[i],
#         ))

# for i in groups:
#     keys.extend(
#         [
#             # mod1 + letter of group = switch to group
#             Key(
#                 [mod],
#                 i.name,
#                 lazy.group[i.name].toscreen(),
#                 desc="Switch to group {}".format(i.name),
#             ),
#             # mod1 + shift + letter of group = switch to & move focused window to group
#             Key(
#                 [mod, "shift"],
#                 i.name,
#                 lazy.window.togroup(i.name, switch_group=True),
#                 desc="Switch to & move focused window to group {}".format(i.name),
#             ),
#             # Or, use below if you prefer not to switch to that group.
#             # # mod1 + shift + letter of group = move focused window to group
#             # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#             #     desc="move focused window to group {}".format(i.name)),
#         ]
#     )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="FreeMono Regular, Symbols Nerd Font Regular",
    fontsize=14,
    padding=4,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper = '/home/administrator/fondos/fondo3.jpg',
        wallpaper_mode = 'fill',
        bottom=bar.Bar(
            [
                # widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("Arch Linux"),
                widget.TextBox("This is Sempiternal  ?/",foreground = "#d75f5f"),
                # widget.TextBox("Administrator"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                # widget.Systray(),
                # Spotify(),
                widget.Clock(format="%d-%m-%Y %a %H:%M"),
                widget.QuickExit(default_text=''),
            ],
            24
	        # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    Screen(
        wallpaper = '/home/administrator/fondos/fondo4.jpg',
        wallpaper_mode = 'fill',
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

autostart = [
    'xrandr --output HDMI-1 --off --output VGA-1 --mode 1280x1024 --pos 0x0 --rotate left --output DP-1 --off --output DVI-D-1-1 --off --output HDMI-1-2 --primary --mode 1366x768 --pos 1024x256 --rotate normal --output DP-1-2 --off'
]

for x in autostart:
    os.system(x )

