# Sistema de Visualización de Proyectos

Este es el repositorio de una API RESTful que se encarga de mostrar en un mapa proyectos inmobiliarios. Esta cuenta con una API RESTful en el backend y un frontend en React TypeScript.

Este repositorio incluye un diagrama hecho en Draw.io para ver en detalle cómo fue planteada la API REST. Todo el código está bien documentado para entender qué hace cada función.

Los tests de la API fueron realizados mediante ThunderClient.

## Tecnologías utilizadas

- **Backend**: 
- Python == 3.9-slim
    - flask == 2.0.2
    - flask-restful == 0.3.9
    - flask-cors == 4.0.0
    - mysql-connector-python == 8.0.28
    - Werkzeug == 2.0.2

- **Frontend**:
- React:
  - "@react-leaflet/core": "^2.1.0"
  - "@testing-library/jest-dom": "^5.17.0"
  - "@testing-library/react": "^13.4.0"
  - "@testing-library/user-event": "^13.5.0"
  - "@types/jest": "^27.5.2"
  - "@types/node": "^16.18.91"
  - "@types/react": "^18.2.69"
  - "@types/react-dom": "^18.2.22"
  - "axios": "^1.6.8"
  - "http-proxy-middleware": "^2.0.6"
  - "leaflet": "^1.9.4"
  - "react": "^18.2.0"
  - "react-dom": "^18.2.0"
  - "react-leaflet": "^4.2.1"
  - "react-scripts": "^5.0.1"
  - "typescript": "^4.9.5"
  - "web-vitals": "^2.1.4"

- **Base de datos**
- MySQL Server: 8.3.0

- **Gestor de contendores**
- Docker Desktop

## Como ejecutar el programa

## 1. Ejecutar la base de datos

 Primero, dentro del repositorio principal, ya sea mediante el cmd/terminal o en Windows 11 haciendo clic derecho y seleccionando "Abrir terminal", debemos acceder al directorio de la base de datos.

**En windows y linux:**

```bash
cd base-de-datos
``` 


Una vez en el directorio con la terminal escribimos:
**en windows y linux:**
```bash
docker build -t svpi-mysql .
``` 
y luego 
```bash
docker run --name mysql-container -d svpi-mysql.
``` 
con eso tendria que estar funcionando correctamente

## 2. Ejecutar la apiRest

ya sea que desde la termina hagamos ```cd ../``` o volvamos para el repositorio principal y abramos alli una terminal, tenemos que ahora con la terminal entrar al backend para esto.

**En windows y linux:**
```bash
cd backend
``` 

una vez en el backend ingresamos en la linea de comandos

```bash
docker build -t backend.
```
y luego
```bash
docker run --name backend-container -d backend
```
una vez inicializado el container en la linea de comandos escribimos
```bash
python app.py
```
para que se ejecute el servidor de python con flask

## 3. Ejecutar el frontend
Ya en ultima instancia queda iniciar el frontend, para esto precisamos de volver al repositorio principal e ingresar en el terminal:

**En windows y linux:**

```bash
cd frontend/svpi-frontend
``` 
una vez ahi ingresamos
 ```bash
docker build -t frontend.
```
y luego
```bash
docker run --name frontend-container -d frontend
```

por ultimo dentro del mismo directorio ingresamos
```
npm start
```

asi se inicia el frontend y con esto tenemos andado todas las partes de la pagina.