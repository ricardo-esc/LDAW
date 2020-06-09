# Dolarick

I. Introducción  
II. Pre-requisitos    
III. Iniciar Dolarick      
IV. Migraciones  
V. API Endpoints  
VI. Licencia


## I. Introducción

Dolarick es una API REST diseñada para la venta de boletos en línea para eventos. Dolarick fue diseñada y creada por Huachipato, un equipo conformado por:  

* Ricardo Escobar Gouyonnet 
* Doménica Rentería Berrospe
* Eduardo Gonzalez Melgoza


## II. Pre-requisitos
1) Python   
2) Virtual Environment

#### 1. Python

Para hacer uso de esta API REST, es necesario contar con una versión de **Python >  3.6.9.**  

Con el siguiente comando, se puede verificar la versión de Python con la que se cuenta:
 
```python
$ python3 --version
```
#### 2. Vitual Environment

Para correr la API REST, es necesario crear un Virtual Environment.

   Con el siguiente comando, se crea uno con el nombre de ___dolarick___:
```python
$ python3 -m venv dolarick
```
Para activar el Virtual Environment, use el siguiente comando:

```python
$ source dolarick/bin/activate
```
## III. Iniciar Dolarick
Vas a hacer uso de dos terminales.  

En la primera terminal, posicíonate en el carpeta de API.    

Para correr dolarick, usar el siguiente comando:
```python
(dolarick) $ python run.py

 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 255-376-821
```
En la segunda terminal, posicíonate en el carpeta de Cliente y corre el siguiente comando:

```python
(dolarick) $ python run.py
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 255-376-821
```

Ingrese al [localhost:80](http://127.0.0.1:80/) para ver la vista Cliente  

Ingrese al [localhost:5000](http://127.0.0.1:5000/events) para ver el JSON

## IV. Migraciones
Cada vez que el modelo de la base de datos cambia, es necesario hacer los siguientes comandos:
```python
(dolarick) $ flask db migrate -m "Nombre de la migration"
(dolarick) $ flask db upgrade
```
## V. API Endpoints

#### GET /events
Regresa la lista de eventos registrados en Dolarick      

Respuesta de ejemplo  [GET /events](http://127.0.0.1:5000/events)

```
[
  {
    "Costo": 123, 
    "Cupo": 100, 
    "Duracion": "123", 
    "Fecha": "2020-05-14T00:00:00", 
    "Lugar": "forfopij", 
    "Nombre": "Muse", 
    "Siglas": "qwe", 
    "idEvento": 1, 
    "imagen": "https://images.genius.com/d8414c555e7d8afd97f5ca206e546997.1000x1000x1.jpg", 
    "user_id": 4
  }, 
  {
    "Costo": 312, 
    "Cupo": 204, 
    "Duracion": "123", 
    "Fecha": "0042-04-23T00:00:00", 
    "Lugar": "Foro sol", 
    "Nombre": "One Direction", 
    "Siglas": "1D", 
    "idEvento": 2, 
    "imagen": "https://i.pinimg.com/originals/b9/1c/d8/b91cd8d98cfd89cb4556fd5cb8cdaec4.jpg", 
    "user_id": 4
  }, 
  {
    "Costo": 2000, 
    "Cupo": 20000, 
    "Duracion": "123 minutos", 
    "Fecha": "2020-05-06T00:00:00", 
    "Lugar": "Queretaro", 
    "Nombre": "Gorillaz", 
    "Siglas": "GZ", 
    "idEvento": 3, 
    "imagen": "https://images-na.ssl-images-amazon.com/images/I/71lix6%2BVfWL._SL1425_.jpg", 
    "user_id": 4
  }
]

```


#### GET /user
Regresa la lista de usuarios registrados en Dolarick      

Respuesta de ejemplo  [GET /user](http://127.0.0.1:5000/user)

```
[
  {
    "edad": null, 
    "email": "a@b.com", 
    "empresa": null, 
    "eventos": {}, 
    "id": 1, 
    "image_file": "default.jpg", 
    "nombreCompleto": null, 
    "numTelefono": null, 
    "password": "$2b$12$pMI14LmUJSVTBUsJmNEACuxXu1Itjy9vH6RgXug0VpeQQALPPSOxW", 
    "residencia": null, 
    "username": "ricardo.esc98"
  }, 
  {
    "edad": 22, 
    "email": "d@r.com", 
    "empresa": "tec", 
    "eventos": {}, 
    "id": 2, 
    "image_file": "default.jpg", 
    "nombreCompleto": "domenica rente", 
    "numTelefono": "1234566754", 
    "password": "$2b$12$AjNcjRY1enWkWUifhzCLJeTi/RCiYVyRzHL6WDbjDiPkYo5XktH82", 
    "residencia": "sma", 
    "username": "domerentss"
  }, 
  {
    "edad": 25, 
    "email": "erick@hotmail.com", 
    "empresa": "Tec", 
    "eventos": {}, 
    "id": 3, 
    "image_file": "default.jpg", 
    "nombreCompleto": "Erick Sanchez", 
    "numTelefono": "442-456-7890", 
    "password": "$2b$12$6Z67r5NZpLuHKuT7g02xruy.yeVEgOmDprHPLSGiOjNAPgWUU/UsW", 
    "residencia": "Queretaro", 
    "username": "Erick"
  }, 
  {
    "edad": 22, 
    "email": "new@mail.com", 
    "empresa": "itesm", 
    "eventos": {}, 
    "id": 4, 
    "image_file": "default.jpg", 
    "nombreCompleto": "nuevo usuario", 
    "numTelefono": "44212132123", 
    "password": "$2b$12$eE4jlDMOjwwmzIhecXPEHeW2hlWdqjy70HYgkhyGeGeZyQCe.C/Dq", 
    "residencia": "qro", 
    "username": "nuevo"
  }, 
  {
    "edad": 22, 
    "email": "bob@mail.com", 
    "empresa": "Crustaceo Cascarudo", 
    "eventos": {}, 
    "id": 5, 
    "image_file": "default.jpg", 
    "nombreCompleto": "Bob Esponja", 
    "numTelefono": "4423566120", 
    "password": "$2b$12$uIgAfnKSqhKwMMjoTo3v4uI.S95rriK.Uzo/u/c4o8PGQUEj/VJmu", 
    "residencia": "Fondo de Bikini", 
    "username": "Bob"
  }, 
  {
    "edad": 23, 
    "email": "crimal@crimal.com", 
    "empresa": "Tec", 
    "eventos": {}, 
    "id": 6, 
    "image_file": "default.jpg", 
    "nombreCompleto": "Crimal", 
    "numTelefono": "4445678909", 
    "password": "$2b$12$yDQLxcWlxvay2shpRwH50uL4jf1wU26BAg8F6uGhKbEF//A/1kWC2", 
    "residencia": "Queretaro", 
    "username": "crimal"
  }, 
  {
    "edad": 22, 
    "email": "do@me.com", 
    "empresa": "tec", 
    "eventos": {}, 
    "id": 7, 
    "image_file": "default.jpg", 
    "nombreCompleto": "domerents", 
    "numTelefono": "4151030187", 
    "password": "$2b$12$2KGvUnPN4U7DxULHnCaPdOpqZ2D2RCQIRT7b8WzsCGMO1U7O678o.", 
    "residencia": "san miguel", 
    "username": "dome"
  }
]

```


#### GET /evento/evento_id
Regresa el evento con el id enviado

Respuesta de ejemplo  [GET /evento/1](http://127.0.0.1:5000/evento/1)

```{
  "Costo": 123, 
  "Cupo": 100, 
  "Duracion": "123", 
  "Fecha": "2020-05-14T00:00:00", 
  "Lugar": "ForoSol", 
  "Nombre": "Muse", 
  "Siglas": "M", 
  "idEvento": 1, 
  "imagen": "https://images.genius.com/d8414c555e7d8afd97f5ca206e546997.1000x1000x1.jpg", 
  "user_id": 4
}

```


## V. Licencia
Huachipato, 2020.
