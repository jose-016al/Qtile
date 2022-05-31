Estos ridrectorios deben copiarse en la sigueintes rutas 
```bash
cp -r Material ~/github/dotfiles/gtk-theme 
```
```bash
cp -r Papirus ~/github/dotfiles/gtk-theme 
```
```bash
cp -r Breeze ~/github/dotfiles/gtk-theme 
```
Para que los temas se apliquen debemos modificar el archivo setting.ini de esta forma 
> [Settings]
   2   │ gtk-icon-theme-name=Papirus
   3   │ gtk-theme-name=Material
   4   │ gtk-font-name=Cantarell 11
   5   │ gtk-cursor-theme-name=Breeze
   6   │ gtk-cursor-theme-size=0
   7   │ gtk-toolbar-style=GTK_TOOLBAR_BOTH
   8   │ gtk-toolbar-icon-size=GTK_ICON_SIZE_LARGE_TOOLBAR
   9   │ gtk-button-images=1
  10   │ gtk-menu-images=1
  11   │ gtk-enable-event-sounds=1
  12   │ gtk-enable-input-feedback-sounds=1
  13   │ gtk-xft-antialias=1
  14   │ gtk-xft-hinting=1
  15   │ gtk-xft-hintstyle=hintfull


```bash

```