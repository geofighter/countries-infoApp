# Countries Info App

Es una aplicación CLI de python que consume datos de la API https://restcountries.com/, crea un DataFrame con ayuda de Pandas y vacía el resultado en una DB sqlite y en un archivo JSON


### Pre-requisitos 📋

* Se necesita tener instalado Python 3.x, para mayor información consulta: https://www.python.org/downloads/
* Se necesita tener instalado SQLite3, para mayor información consulta: https://www.sqlite.org/download.html
* Se necesita tener instalado pip, para mayor información consulta: https://pip.pypa.io/en/stable/getting-started/
* Se necesita tener instalado virtualenv, para mayor información consulta: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment

### Instalación 🔧

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_
* Es necesario ubicarse dentro de la carpeta principal del proyecto
* Una vez ubicados se debe crear un entorno virtual para poder instalar las dependencias necesarias del proyecto, ejecutando:
```
python -m venv env
```
* Una vez creado el entorno virtual, es necesario activarlo con la siguiente línea:
```
source env/bin/activate
```
* Posteriormente se deben instalar las dependencias necesarias para la correcta ejecución de la aplicación, para ello se ejecuta la siguiente línea:
```
pip install -r requirements.txt
```
* Después de tener instaladas las dependencias necesarias, se podrá ejecutar la aplicación, ejecutando:
```
python main.py
```
_NOTA: Si la aplicación retorna un error al crear la DB se deben dar permisos de administrador o root a la carpeta para que la aplicación pueda crear la DB sin problemas, ejemplo:_

```
chmod +x carpeta_del_proyecto
```

## Ejecutando las pruebas ⚙️

Para ejecutar las pruebas de la aplicación se ejecuta la siguiente linea:
```
pytest test.py
```

### ¿Qué verifican las pruebas? 🔩

_Las pruebas realizadas en esta aplicación verifican la correcta conexion a la DB y que la petición a la API consumida, retorne una respuesta exitosa_

## Desarrollado con la ayuda de: 🛠️

* [python](https://www.python.org/) - Lenguaje utilzado en el proyecto
* [pip](https://pip.pypa.io/en/stable/) - Administrador de dependencias
* [virtualenv](https://virtualenv.pypa.io/en/latest/) - Herramienta para crear entornos virtuales con python
* [pandas](https://pandas.pydata.org/) - Librería usada para la creación de DataFrame

## Autor ✒️

* **Marcos Geovanny Esteban Mendieta** - [geofighter](https://github.com/geofighter)

## Licencia 📄

Este proyecto está bajo la Licencia (MIT) - Para mayor información, consulta: https://opensource.org/licenses/MIT

---
