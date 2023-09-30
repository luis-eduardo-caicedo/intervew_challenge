
# Take-Home Interview Challenge

El proyecto se centra en la creación y gestión de usuarios con información de dirección, y la capacidad de listar usuarios según el país al que pertenecen.


## Pre-requisitos 📋

### Activar el entorno virtual 📍

Verificaremos que estamos en la ruta donde se encuentra la carpeta "env", luego de saber esto, pegamos este siguiente comando para activar el entorno virtual

source env/bin/activate
```
 > source env/bin/activate

```

### Instalar Dependencias 📍
Instalar las dependencias mediante el archivo requirements.txt, copie el siguiente comando y lo pega en la terminal.

<!--sec data-title="Current directory: OS X and Linux" data-id="OSX_Linux_pwd" data-collapse=true ces-->

{% filename %}command-line{% endfilename %}

    pip install -r requirements.txt
    

> Nota: Este comando instala los requerimientos necesarios para el funcionamineto del proyecto.

<!--endsec-->

<!--sec data-title="Current directory: Windows" data-id="windows_cd" data-collapse=true ces-->

Verifique antes que usted se ubique en la ruta del proyecto donde este el archivo.


## Poner en funcionamiento el proyecto 💻

Primero que todo utilizamos el siguiente comando que nos ayuda a crear la base de datos si no esta creada y crea las tablas que estan registradas, luego de esto, el servicio queda activo automaticamente y listo para su uso.

<!--sec data-title="Current directory: OS X and Linux" data-id="OSX_Linux_pwd" data-collapse=true ces-->

{% filename %}command-line{% endfilename %}

    uvicorn main:app --reload

> Nota: Este comando inicia el proyecto

<!--endsec-->

<!--sec data-title="Current directory: Windows" data-id="windows_cd" data-collapse=true ces-->


## Como utilizar las API's

### Por medio de la terminal 📍

Abrimos la terminal y luego pegamos los siguientes comandos que podemos usar para listar y crear registros...

* Con este comando vamos a crear los usuarios... 🟢

<!--sec data-title="Current directory: OS X and Linux" data-id="OSX_Linux_pwd" data-collapse=true ces-->

{% filename %}command-line{% endfilename %}

    curl -X POST -H "Content-Type: application/json" -d '{"first_name": "string","last_name": "string","email": "string","password": "string","address_1": "string","address_2": "string","city": "string","state": "string","zip": 0,"country": "string"}' "http://localhost:8000/api/v1/create/user"

> Nota: Este comando tiene datos de ejemplo, tiene que poner los datos que desea en las variables

<!--endsec-->

<!--sec data-title="Current directory: Windows" data-id="windows_cd" data-collapse=true ces-->


* Listar paises... 🟢

<!--sec data-title="Current directory: OS X and Linux" data-id="OSX_Linux_pwd" data-collapse=true ces-->

{% filename %}command-line{% endfilename %}

    curl http://localhost:8000/api/v1/list/countrys

<!--endsec-->

<!--sec data-title="Current directory: Windows" data-id="windows_cd" data-collapse=true ces-->

* Buscar todos los usuarios por pais... 🟢

<!--sec data-title="Current directory: OS X and Linux" data-id="OSX_Linux_pwd" data-collapse=true ces-->

{% filename %}command-line{% endfilename %}

    curl -X POST -H "Content-Type: application/json" -d '{"country": "Colombia"}' "http://localhost:8000/api/v1/list/user_country/"

> Nota: Este comando tiene datos de ejemplo, tiene que poner los datos que desea en las variables

<!--endsec-->

<!--sec data-title="Current directory: Windows" data-id="windows_cd" data-collapse=true ces-->

* Listar todos los usuarios... 🟢

<!--sec data-title="Current directory: OS X and Linux" data-id="OSX_Linux_pwd" data-collapse=true ces-->

{% filename %}command-line{% endfilename %}

    curl http://localhost:8000/api/v1/list/user

<!--endsec-->

<!--sec data-title="Current directory: Windows" data-id="windows_cd" data-collapse=true ces-->


### Por medio de la Documentacion 📍

Podemos utilizar el Docs, que trae el proyecto, para acceder a él tenemos que entrar en la ruta.

```
 > http://localhost:8000/docs#/
```

Estando en la documentacion podemos observas los servicios,para probarlos accedemos a ellos y le damos en el boton de "Try it out".

> Nota: En la documentacion observamos un ejemplo de el body, y los codigos de respuesta que tiene el servicio


## Correr las pruebas unitarias 🖥️
Verifique que este en la ruta del proyecto donde este ubicado el archivo "test_main.py"

```
 > python -m pytest
```


## ¿Listo?
¡Vamos a bucear en Python!