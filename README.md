# Calculadora
Para poder utilizar la aplicación de la calculadora se necesita 

título, descripción, requisitos ,instrucciones de instalación y configuración , instrucciones de ejecución 



Título:
Calculadora Peke Estudia

Descripció:
Esta es una calculadora, que su finalidad y propósito sea que los estudiantes de alto nivel puedan llevar sus cuentas y operaciones desde su dispositivo , esto con la finalidad de poder llevar sus problemas más rápido y de una manera más consciente , sin temor y con la seguridad de no poder equivocarse.
Se pensó de esta manera ya que muchas veces alguien tiene todo su procedimiento bien pero a la hora de hacer las cuentas es lo que fallo y puede que tu rango de error en las cuentas sea muy grande y eso no es lo más correctos dependiendo del problema o situación que te encuentres entonces de esta manera les damos la seguridad de que estarán bien sus operaciones matematicas.

Requisitos:
Una computadora o Smartphone de las siguientes características
-2 Gb de RAM
-Cualquier Sistema Operativo es compatible con este programa
-Requiere Android 6.0 o superior
-Requiere Windows superior al XP


instrucciones de instalación y configuración:
Para poder ingresar al programa se necesita tener instalado el Docker , también se necesita tener el Visual Studio Code para poder tener acceso al programa


Instrucciones de ejecución:
Para poder tener una ejecución exitosa tienes que seguir las siguientes instrucciones e indicaciones, lo primero que debes de hacer es 

 
Creación de un contenedor en Docker 
Debemos tener en cuenta que ya tenemos debemos tener instalado el visual studio code e instalarle la extensión de docker

Después, tenemos que descargar e instalar el Docker desktop en nuestra computadora

Tenemos que tener los siguientes archivos en nuestro proyecto creado en visual studio

Con la siguiente información dentro de

version: '3'

services:
  web:
    build: 
      context: .
    ports:
      - "3000:80"
    volumes:
      - .:/usr/local/apache2/htdocs/
  mysql:
    image: mysql:latest
    environment:
      - MYSQL_ROOT_PASWORD=12345
      - MYSQL_DATABASE=demo
    volumes:
      - mysql_data:/var/lib/mysql
volumes:
  mysql_data:

#utiliza la imagen base de apache 2.4.12
FROM httpd:2.4.12

#copia los archivos del proyecto a la ruta especificada
COPY . /usr/local/apache2/htdocs/

#expone el puerto de conexion para el servicio de apache 
EXPOSE 80

CMD [ "httpd", "-D", "FOREGROUND" ]

También tendríamos que agregar nuestro archivo calculadora con la extensión del lenguaje que nosotros elegimos.
