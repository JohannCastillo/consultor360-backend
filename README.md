- [Instrucciones para instalar y ejecutar el proyecto backend](#instrucciones-para-instalar-y-ejecutar-el-proyecto-backend)
  - [Requerimientos](#requerimientos)
  - [Variables de entorno](#variables-de-entorno)
  - [Instalación y ejecución](#instalación-y-ejecución)
- [Tecnologías y herramientas utilizadas](#tecnologías-y-herramientas-utilizadas)
- [Codificación con IA](#codificación-con-ia)
- [Notas](#notas)


# Instrucciones para instalar y ejecutar el proyecto backend

## Requerimientos

- Docker y Docker Compose

## Variables de entorno
Copiar el archivo `.env.example` a `.env` y modificar los valores de las variables de entorno.

Ejemplo:
```
ENVIRONMENT=development
SECRET_KEY='django-insecure-z^0mfzjnv11#ji6j3zyy)xm)6r$q0hogkptt)_=b169_67(u!0'

POSTGRES_USER=postgres
POSTGRES_PASSWORD=0000
POSTGRES_DB=consultor360
DATABASE_URL=postgres://postgres:0000@consultor360_db:5432/consultor360
```


## Instalación y ejecución

1. Abrir una terminal en la carpeta raíz del proyecto backend.

2. Asegurarse de que el archiv `dev.sh` sea ejecutable.
```bash
chmod +x dev.sh
```
   
3. Ejecutar el siguiente comando para instalar las dependencias y ejecutar el proyecto en modo de desarrollo de forma local:

```bash
docker compose up -d
```

Esto instalará las librerías necesarias y ejecutará las migraciones del proyecto. Una vez finalizada la ejecución, el servicio se encontrará disponible en [http://localhost:8000](http://localhost:8000).

> Para ver la documentación, acceder a [http://localhost:8000/docs](http://localhost:8000/docs).

# Tecnologías y herramientas utilizadas
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django](https://www.djangoproject.com/)
- [PostgreSQL 16](https://www.postgresql.org/)
- [drf_spectacular y Swagger UI](https://drf-spectacular.readthedocs.io/en/stable/) (Documentación de la API REST)
- [Rest Framework Auth Token]() (Autenticación de usuarios por JWT)
- [Render](https://render.com/docs/deploy-django) (Despliegue)

# Codificación con IA
Se utilizó IA para agilizar partes del desarrollo del proyecto backend. Utilizando `Github Copilot` y `ChatGPT`. Algunas de las principales utilidades que se aprovecharon

- Revisión del código
- Autocompletado
- Generación automática de documentación de API REST
- Solución de errores

# Notas
- Para probar las peticiones autenticadas desde Swagger UI, utilizar la opción `authorize` (ver las siguientes imágenes).

<img src="./docs/assets/swagger-auth.png" alt="Peticiones autenticadas en Swagger UI" width="500">

<img src="./docs/assets/image-2.png" alt="Autenticación de usuarios en Swagger UI" width="500">

En el campo TokenAuth (apiKey) debe ingresar el token que se obtiene en la petición de `login` y [decodificar](https://www.base64decode.org/) el token recibido en base64 .

Ejemplo:

<img src="./docs/assets/token.png" alt="Decodificar el token" width="500">

<img src="./docs/assets/decoder.png" alt="Decodificar el token" width="500">
