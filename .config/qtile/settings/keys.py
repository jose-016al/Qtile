# Qtile keybindings
from libqtile.config import Key
from libqtile.command import lazy

mod = "mod4"

keys = [
    # ------------ Window Configs ------------

    # Alternar entre ventanas en la ventana actual.
    Key([mod], "j", lazy.layout.down(), desc="Move focus dwown"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    
    # Cambiar tamaños de ventana (MonadTall)
    Key([mod, "shift"], "l", lazy.layout.grow()),
    Key([mod, "shift"], "h", lazy.layout.shrink()),

    # Alternar ventana flotante
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Mover las ventanas hacia arriba o hacia abajo en la pila actual
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Alternar entre diferentes disposiciones según se define a continuación
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "Tab", lazy.prev_layout()),

    # Cerrar ventana
    Key([mod], "w", lazy.window.kill()),
    
    # Cambiar el enfoque de los monitores
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),

    # Reiniciar Qtile
    Key([mod, "control"], "r", lazy.restart()),

    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    Key([mod], "m", lazy.spawn("rofi -show drun")),

    # Menu bar
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    Key([mod], "b", lazy.spawn("brave")),

    # Terminal
    Key([mod], "Return", lazy.spawn("kitty")),

    # File Explorer
    Key([mod], "e", lazy.spawn("thunar")),

    # Screenshot
    Key([mod], "s", lazy.spawn("scrot")),
    Key([mod, "shift"], "s", lazy.spawn("scrot -s")),

    # ------------ Hardware Configs ------------

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

]