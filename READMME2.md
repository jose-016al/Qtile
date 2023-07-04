# Mi entorno de escriotiro Qtile con ArchLinux

# Tabla de contenidos
- [ArchLinux](#arch-linux)
  - [Instalacion de ArchLinux](#instalacion-de-archlinux)
    - [Conexion wifi](#conexion-wifi)
    - [Particiones y formato de disco](#particionar-y-formatear-el-disco)
    - [Instalar paquetes esenciales](#instalar-paquetes-esenciales)
    - [Instalacion del gestor de arranque](#instalacion-del-gestor-de-arranque)
    - [Antes de reiniciar](#antes-de-reiniar)
  - [Configuracion adicional de Arch Linux](#configuracion-adicional-de-arch-linux)
- [Qtile](#qtile)
  - [Instalacion de Qtile](#instalacion-de-qtile)
  - [Instalacion paquetes necesarios para Qtile](#instalacion-paquetes-necesarios-para-qtile)

# Arch Linux

## Instalacion de ArchLinux 
Como la instalacion puede cambiar, lo mejor seria diriginos directamente a la [guide installation](https://wiki.archlinux.org/title/Installation_guide_(Espa%C3%B1ol)) y seguir paso a paso la guia de instalacion de archlinux  

Es posible que nos salga el tamaño de fuente demasiado pequeño, por ahora podemos configurar esto con este comando
```bash
setfont ter-118n
```

### Conexion wifi
```bash
iwctl
```
```bash
station wlan0 scan       
```
```bash
station wlan0 get-networks
```
```bash
station wlan0 connect SSID
```

### Particionar y formatear el disco
Usaremos cfdisk por su comodidad
```bash
cfdisk
```
Particionamos el disco usando cfdisk  
    - 150 MB - EFI SYSTEM  
    - 15 GB - SWAP  
    - RESTO - /  
podemos ver las particiones fuera de cfdisk con
```bash
lsblk
```
Formateamos la particion swap
```bash
mkswap /dev/sda2
```
```bash
swapon /dev/sda2
```
Formateamos las particiones: /
```bash
mkfs.ext4 /dev/sda3
```
Montamos los sistemas de archivos
```bash
mount /dev/sda3 /mnt
```
Montamos la particion de EFI 
```bash
mount --mkdir /dev/sda1 /mnt/boot
```

### Instalar paquetes esenciales
Algunos paquetes quizas no sean esenciales pero podemos aprovechar e instalarlos ya
```bash
pacstrap /mnt base linux linux-firmware networkmanager sudo grub efibootmgr nano iwd
```

### Instalacion del gestor de arranque
Procedemos con la configuracion del grub
COnfiguramos el grub
```bash
grub-install --target=x86_64-efi --efi-directory=/boot
```
```bash
grub-mkconfig -o /boot/grub/grub.cfg
```

### Antes de reiniar
Asegurarse de habilitar el servicio networkManager
```bash
systemctl enable NetworkManager
```
Una vez hecho esto ya podemos salir de la instalacion
```bash
exit
```
```bash
umount -R /mnt
```
Y reiniciamos el sistema, si nos sale el gestor de arranque de Arch habra salido todo bien
```bash
reboot
```

## Configuracion adicional de Arch Linux
Editamos el archivo hosts
```bash
nano /etc/hosts

127.0.0.1	localhost   
::1		    localhost    
127.0.1.1	ArchLinux.localhost	ArchLinux      
```
Creacion de un nuevo usuario
```bash
useradd -m jose
```
```bash
passwd jose
```
```bash
usermod -aG wheel,video,audio,storage jose
```
tendremos que configurar el archivo sudoers para poder ser root
```bash
nano /etc/sudoers
```
Para poder instalar entornos de escritorio necesitamos instalar xorg
```bash
sudo pacman -S xorg xorg-server
```
Ahora generamos nuestras carpetas personales básicas (Escritorio, Descargas, Música, Etc.).
Para esto instalamos la herramienta xdg-user-dirs:
```bash
sudo pacman -S xdg-user-dirs
```
Por ultimo lo ejecutamos para que nos genere nuestras carpetas.
```bash
xdg-user-dirs-update
```

# Qtile

## Instalacion de Qtile
Instalamos Qtile y el logging manager
```bash
sudo pacman -S qtile lightdm lightdm-gtk-greeter
```
```bash
systemctl enable lightdm
```
Al ejecutar Qtile no podremos abrir una terminal, ya que Qtile usa xterm, tendremos que modificar en Keys la terminal  

## Instalacion paquetes necesarios para Qtile
Instalacion de algunos paquetes basicos para Qtile
```bash
sudo pacman -S git base-devel pulseaudio pavucontrol xorg-xinit arandr kitty rofi feh picom volumeicon cbatticon udisks2 udiskie ntfs-3g vlc imv scrot unzip lxappearance wget network-manager-applet spotify-launcher
```
```bash
sudo pacman -S ttf-dejavu ttf-liberation noto-fonts  notification-daemon libnotify python-pip pacman-contrib bat lsd zsh
```
Instalacion del paquete yay, que nos permitira instalar otros paquetes que noe esten en pacman
```bash 
git clone https://aur.archlinux.org/yay.git
```
```bash
cd yay
```
```bash
makepkg -si
```
Una vez tengamos instalado yay, podremos instalar el resto de paquetes
```bash
yay -S brave-bin telegram-desktop-bin visual-studio-code-bin autofirma configuradorfnmt onedriver xfce4-power-manager nautilus nerd-fonts-ubuntu-mono gnome-disk-utility zsh-syntax-highlighting zsh-autosuggestions
```
```bash
yay -S evince netflix-bin whatsapp-for-linux  transmission-gtk apache-netbeans prospect-mail-bin dbeaver  gcalctool-oldgui gnome-calendar brightnessctl-git ms-office-online lightdm-webkit-theme-osmos
```

# Mi configuracion
Si quereis tener la misma configuracion que uso
```bash
git clone git@github.com:jose-016al/Qtile.git
```
```bash
cd Qtile
```
Copiamos el directorio .config
```bash
cp -r .config ~/
```
Copiamos el archivo xsession para que los cambios sean permanentes
```bash
cp -r .xsession ~/
```
Le damos permisos de ejecicion en caso de que no los tenga
```bash
chmod u+x .xsession
```