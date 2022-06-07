# Configuracion kitty
Si tenemos problemas con el teclado en español
```bash
localectl set-x11-keymap es
```
Cambiamos la shell
```bash
usermod --shell /bin/bash/zsh jose 
```
Creamos un directorio en la ruta
```bash
sudo mkdir /usr/share/zsh-sudo
```
```bash
cp -r sudo.plugin.zsh /usr/share/zsh-sudo
```
Clonamos el repositorio de powerlevel10k
```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
```
```bash
zsh 
```
```bash
cp -r .p10k.zsh ~/
```