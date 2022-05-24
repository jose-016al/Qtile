# Mis configuraciones de Qtile

![Qtile](.screenshots/qtile.png)

# Índice

- [Instalacion de Arch Linux](#instalacion-de-arch-linux)

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
Formateamos las particiones
```bash
mkfs.ext4 /dev/sda3
```
``bash
mkfs.ext4 /dev/sda4
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

