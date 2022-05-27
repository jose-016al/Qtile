# Mis configuraciones de Qtile

![Qtile](.screenshots/qtile.png)

# Índice

- [Instalacion de Arch Linux](#instalacion-de-arch-linux)
- [Tras la instalacion](#tras-la-instalacion)

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

# Tras la instalacion


```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```


# Tras la instalacion de Arch Linux

#### paquetes necesarios
```bash
sudo pacman -S 
```


#### Ahora para nuestras carpetas personales básicas (Escritorio, Descargas, Música, Etc.).
#### Para esto instalamos la herramienta xdg-user-dirs:
```bash
sudo pacman -S xdg-user-dirs
```
#### Por ultimo lo ejecutamos para que nos genere nuestras carpetas.
```bash
xdg-user-dirs-update
```

