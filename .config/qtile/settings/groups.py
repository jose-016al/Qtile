# Qtile workspaces
from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import mod, keys

# Icons: 
# nf-fa-chrome, 
# nf-md-microsoft_visual_studio_code, 
# nf-dev-terminal, 
# nf-oct-file_directory_fill,
# nf-oct-image, 
# nf-md-file_pdf_box,
# nf-fae-layers

groups = [Group(i) for i in [
    "   ", " 󰨞  ", "   ", "   ", "   ", " 󰈦  ", "   ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Cambiar al workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Envia la ventana al workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])