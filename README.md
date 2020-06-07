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
Para correr dolarick, usar los siguientes 3 comandos:
```python
(dolarick) $ export FLASK_APP=run.py
(dolarick) $ export FLASK_ENV=development
(dolarick) $ flask run

 * Serving Flask app "run.py" 
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 157-644-835
```
Ingrese al [localhost:500](http://127.0.0.1:5000/) para ver la API

## Migraciones
Cada vez que el modelo de la base de datos cambia, es necesario hacer los siguientes comandos:
```python
$ flask db migrate -m "Nombre de la migration"
$ flask db upgrade
```
## Licencia
huachipato 2020 salu2
