#utiliza la imagen base de apache 2.4.12
FROM httpd:2.4.12

#copia los archivos del proyecto a la ruta especificada
COPY . /usr/local/apache2/htdocs/

#expone el puerto de conexion para el servicio de apache 
EXPOSE 80

CMD [ "httpd", "-D", "FOREGROUND" ]