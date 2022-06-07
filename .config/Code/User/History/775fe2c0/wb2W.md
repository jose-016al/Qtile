# Mis configuraciones de Qtile

![Qtile](.screenshots/qtile.png)

# Enlaces a consultar
- **[Gnome-Look](https://www.gnome-look.org/s/Gnome/browse/))**
- **[Qtile docs](http://docs.qtile.org/en/stable/))**

# Índice

- [Instalacion de Arch Linux](#instalacion-de-arch-linux)
- [Tras la instalacion de Arch Linux](#tras-la-instalacion-de-arch-Linux)
- [Instalacion Qtile](#instalacion-qtile)
- [Instalacion paquetes necesarios para Qtile](#instalacion-paquetes-necesarios-para-qtile)
- [Configuracion kitty](#configuracion-kitty)
- [Configuracion Qtile](#configuracion-qtile)


# Instalacion de Arch Linux

Para la instalacion de Arch Linux es recomendable tener a mano la **[Wiki de Arch](https://wiki.archlinux.org/title/Installation_guide_(Espa%C3%B1ol))**

Cambiamos la distribucion del teclado 
```bash
loadkeys es
```
Nos aseguramos de tener acceso a internet, ya sea por LAN, si no es el caso ejecutamos los siguientes comandos
```bash
iwctl...
```
Listamos el contenido del directorio efivars, para comprobar la modalidad de arranque del sistema, UEFI o BIOS
```bash
ls /sys/firmware/efi/efivars
```
Actualizamos el reloj del sistema
```bash
timedatectl set-ntp true
```
Particionamos el disco usando cfdisk  
    - 150MB - EFI SYSTEM  
    - 15GB - SWAP  
    - 50GB - /  
    - RESTO - HOME  
```bash
cfdisk
```
Podemos ver el estado de nuestras particiones
```bash
lsblk
```
Formateamos las particiones: / y home
```bash
mkfs.ext4 /dev/sda3
```
``bash
mkfs.ext4 /dev/sda4
```
Formateamos la particion swap
```bash
mkswap /dev/sda2
```
```bash
swapon /dev/sda2
```
Montamos los sistemas de archivos
```bash
mount /dev/sda3 /mnt
```
```bash
mkdir /mnt/home
```
```bash
mount /dev/sda4 /mnt/home
```
```bash
mkdir /mnt/boot
```
```bash
mount /dev/sda1 /mnt/boot
```
Instalamos los paquetes necesarios
```bash
pacstrap /mnt base linux linux-firmware networkmanager sudo grub efibootmgr nano kitty firefox
```
Generamos el archivo fstab
```bash
genfstab -U /mnt >> /mnt/etc/fstab
```
Cambiamos la raiz al nuevo sistema
```bash
arch-chroot /mnt
```
Definimos la zona horaria
```bash
ln -sf /usr/share/zoneinfo/Europe/Madrid /etc/localtime
```
```bash
hwclock --systohc
```
Idioma del sistema y teclado
```bash
nano /etc/locale.gen
```
```bash
locale.gen
```
```bash
echo "LANG=es_ES.UTF-8" > /etc/locale.conf
```
```bash
echo "KEYMAP=es" > /etc/vconsole.conf
```
Configuracion de red
```bash
echo "ArhLinux" > /etc/hostname
```
Editamos el archivo hosts
```bash
nano /etc/hosts
```
> 127.0.0.1	localhost  
> ::1		    localhost  
> 127.0.1.1	ArchLinux.localhost	ArchLinux    

Le asignamos contraseña al root
```bash
passwd
```
Creamos un usuario
```bash
useradd -m jose
```
```bash
passwd jose
```
```bash
usermod -aG wheel,video,audio,storage
```
tendremos que configurar el archivo sudoers para poder ser root
```bash
nano /etc/sudoers
```
Iniciamos el servicio de internet
```bash
systemctl enable NetworkManager
```
COnfiguramos el grub
```bash
grub-install -target=x86_64-efi --efi-directory=/boot
```
```bash
grub-mkconfig -o /boot/grub/grub.cfg
```
Salimos de la instalacion
```bash
exit
```
```bash
umount -R /mnt
```
Y reiniciamos el sistema, si nos sale el grub de Arch habra salido todo bien
```bash
reboot
```

# Tras la instalacion de Arch Linux

Instalamos xorg
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

# Instalacion Qtile

Instalamos Qtile y el logging manager
```bash
sudo pacman -S qtile lightdm lightdm-gtk-greeter
```
```bash
systemctl enable lightdm
```

# Instalacion paquetes necesarios para Qtile

Instalamos paquetes todos los paquetes 
```bash
sudo pacman -S git base-devel rofi feh picom pulseaudio pavucontrol bridghtnessctl xorg-xinit volumeicon cbatticon udisks2 udiskie ttf-dejavu ttf-liberation noto-fonts ntfs-3g arandr vlc imv scrot unzip lxappearance wget network-manager-applet notification-daemon libnotify python-pip pacman-contrib bat exa
```
Instalamos yay
```bash 
git clone https://aur.archlinux.org/yay.git
```
```bash
cd yay
```
```bash
makepkg -si
```
Instalamos paquetes con yay
```bash
yay -S visual-studio-code-bin autofirma configuradorfnmt evince nautilus nerd-fonts-ubuntu-mono netflix-bin onedriver spotify telegram-desktop-bin whatsapp-for-linux xfce4-power-manager transmission-gtk apache-netbeans
```

# Configuracion kitty

# Configuracion Qtile

Copiamos la configuracion de Qtile de github
```bash
git clone git@github.com:jose-016al/dotfiles.git
```
```bash
cd dotfiles
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