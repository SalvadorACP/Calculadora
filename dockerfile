#utiliza la imagen base de apache 2.4.12
FROM  python:latest

# Establece el directorio de trabajo en el contenedor
WORKDIR /app 

#copia los archivos del proyecto a la ruta especificada
COPY . /app

#expone el puerto de conexion para el servicio de apache 
EXPOSE 5000

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt


#inicia el servico httpd con argumentos -D FOREGROUND
CMD   ["python", "app.py"]