# Dolarick

I. Introducción  
II. Pre-requisitos    
III. Iniciar Dolarick      
IV. Migraciones


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

Ingrese al [localhost:80](http://127.0.0.1:80/) para ver la API  

Ingrese al [localhost:5000](http://127.0.0.1:5000/events) para ver la vista cliente

## Migraciones
Cada vez que el modelo de la base de datos cambia, es necesario hacer los siguientes comandos:
```python
(dolarick) $ flask db migrate -m "Nombre de la migration"
(dolarick) $ flask db upgrade
```
## Licencia
huachipato 2020 salu2
