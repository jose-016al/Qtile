# Docker ![Docker](.docker.png)

## Tabla de contenidos
- [Instalacion de Docker en Arch Linux](#instalacion-de-Docker-en-arch-linux)
- [DockerHub](#dockerhub)
- [Comandos basicos de Docker](#comandos-basicos-de-docker)
  - [Contenedores](#contenedores)
  - [Imagenes](#imagenes)
  - [Persistencia](#persistencia)
  - [Generar imagenes](#generar-imagenes)
- [Contenedor SSH](#contenedor-ssh)
- [Contenedor Apache](#contenedor-apache)
- [Contenedor Mariadb](#contenedor-mariadb)
 
# Instalacion de Docker en Arch Llnux
Habilitamos el modulo loop
```bash
tee /etc/modules-load.d/loop.conf <<< "loop"
```
```bash
modprobe loop
```
```bash
lsmod | grep loop
```
Procedemos a la instalacion de Docker
```bash
sudo pacman -S docker
```
Para poder ejecutar contenedores de docker sin tener permisos root 
```bash
sudo groupadd docker
```
```bash
sudo usermod -aG docker $USER
```
```bash
newgrp docker
```
Para habilitar el servicio usamos start o enable para que este siempre iniciado
```bash
sudo systemctl start docker
```

# DockerHub
Hacer login en **[DockerHub](https://hub.docker.com/))**
```bash
docker login
```
O hacer logout
```bash
docker logout
```

# Comandos basicos de Docker

## Contenedores
Lanzar un contenedor, seria conveniente ponerle un nombre con "--name"
```bash
docker run --name ubuntu -it ubuntu /bin/bash
```
Ver los contenedores que estan en ejecucion
```bash
docker ps
```
Ver todos los contenedores, ya esten en ejecucion o parados 
```bash
docker ps -a
```
Iniciar o parar un contenedor
```bash
docker start "nombre_contenedor"
```
```bash
docker stop "nombre_contenedor"
```
Obtener una terminal en un contenedor 
```bash
docker exec -it server /bin/bash
```
Copiar ficheros desde nuestra sistema al contenedor de docker
```bash
docker cp prueba.html server:/usr/local/apache2/htdocs/index.html
```
```bash
docker cp server:/usr/local/apache2/htdocs/index.html $HOME/test.html
```

## Imagenes
Descargar una imagen, al final especificamos la version, si no especificamos nada descarga la ultima version
```bash
docker pull ubuntu:18.04
```
Ver las imagenes descargadas
```bash
docker images
```
Borrar imagenes, con "-a" borramos todas las imagenes sin usar
```bash
docker rmi ubuntu
```
```bash
docker image prune -a
```

## Persistencia
Los bind mount nos permite enlazar una directorio del host con un directorio del contenedor
```bash
docker run --name server -v /home/usuario/web:/usr/local/apache2/htdocs -p 80:80 httpd
```
```bash
docker run --name server -p 80:80 --mount type=bind,src=/home/usuario/web,dst=/usr/local/apache2/htdocs httpd
```

## Generar imagenes
Creacion de una imagen a partir del contenedor, podemos especificar versiones con ":"
```bash
docker commit server jose016al/ubuntu
```
Subir la imagen creada a dockerhub 
```bash
docker push jose016al/ubuntu
```

# Contenedor SSH
Lanzamos un contenedor de ubuntu, con el puerto 22 para poder comunicarnos 
```bash
docker run --name server -it-p 2222:22 ubuntu
```
Actualizamos el contenedor 
```bash
apt update
```
```bash
apt upgrade
```
Instalamos los paquetes necesarios
```bash
apt install iproute2
```
```bash
apt install openssh-server
```
```bash
apt install sudo
```
```bash
apt install nano
```
Creacion de un usuario
```bash
useradd -m jose
```
```bash
passwd jose
```
```bash
usermod -aG sudo jose
```
Reiniar el servicio ssh
```bash
service ssh restart
```

# Contenedor Apache
Partimos del contenedor anterior, esta vez con persistencia y abriendo los puertos 22 y 80
```bash
docker run --name server -it -v ~/github/Docker/Web:/var/www/html -p 2222:22 -p 8080:80 jose016al/ssh
```
Actualizar el contenedor 
```bash
apt update
```
```bash
apt upgrade
```
Instalamos los paquetes necesarios
```bash
apt install apache2 
```
```bash
apt install php
```
Reiniar los servicios
```bash
service ssh restart
```
```bash
service apache2 restart
```

# Contenedor Mariadb
Partimos del contenedor anterior, con persistencia y abriendo los puertos 22, 80 y 3306  
_(Hay que tener en cuenta que mysql entre en conflicto se hacemos la persistencia en un repositorio o en onedrive)_
```bash
docker run --name server -it -v ~/github/Docker/Web:/var/www/html -v ~/.BD:/var/lib/mysql -p 2222:22 -p 8080:80 -p 3306:3306 jose016al/apache2
```
Actualizar el contenedor
```bash
apt update
```
```bash
apt upgrade
```
Instalacion de los paquetes necesarios
```bash
apt install dialog
```
```bash
apt install apt-utils
```
```bash
apt install mariadb-server
```
Configuramos la seguridad
```bash
mysql_secure_installation
```
> ENTER, N, Y, Y. Y Y

Inicializamos el directorio raiz y reiniciamos el servicio, si fuese neceario
```bash
usermod -d /var/lib/mysql/ mysql
```
```bash
service mysql restart
```
Creamos un usuario admin y uno remoto
```bash
GRANT ALL ON *.* TO 'admin'@'localhost' IDENTIFIED BY '211099' WITH GRANT OPTION;
```
```bash
FLUSH PRIVILEGES;
```
Creamos el usuario remoto
```bash
GRANT ALL ON *.* TO 'jose'@'%' IDENTIFIED BY '211099' WITH GRANT OPTION;
```
```bash
FLUSH PRIVILEGES;
```
Instalacion de phpmyamdin
```bash
apt install phpmyadmin
```
Modificamos el fichero de configuracion de mysql para permitir aceso al usuario remoto
```
nano /etc/mysql/mysql.conf.d/mysqld.cnf
```
```
#bind-address = 127.0.0.1  
```