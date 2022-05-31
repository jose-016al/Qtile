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
gtk-icon-theme-name=Papirus  
gtk-theme-name=Material  
gtk-font-name=Cantarell 11  
gtk-cursor-theme-name=Breeze  
gtk-cursor-theme-size=0  
gtk-toolbar-style=GTK_TOOLBAR_BOTH  
gtk-toolbar-icon-size=GTK_ICON_SIZE_LARGE_TOOLBAR  
gtk-button-images=1  
gtk-menu-images=1  
gtk-enable-event-sounds=1  
gtk-enable-input-feedback-sounds=1  
gtk-xft-antialias=1  
gtk-xft-hinting=1  
gtk-xft-hintstyle=hintfull  

Tambien podemos instalar la aplicacion 
```bash

```