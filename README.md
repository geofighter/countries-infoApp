# Countries Info App

Es una aplicaci贸n CLI de python que consume datos de la API https://restcountries.com/, crea un DataFrame con ayuda de Pandas y vac铆a el resultado en una DB sqlite y en un archivo JSON


### Pre-requisitos 馃搵

* Se necesita tener instalado Python 3.x, para mayor informaci贸n consulta: https://www.python.org/downloads/
* Se necesita tener instalado SQLite3, para mayor informaci贸n consulta: https://www.sqlite.org/download.html
* Se necesita tener instalado pip, para mayor informaci贸n consulta: https://pip.pypa.io/en/stable/getting-started/
* Se necesita tener instalado virtualenv, para mayor informaci贸n consulta: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment

### Instalaci贸n 馃敡
* Es necesario ubicarse dentro de la carpeta principal del proyecto
* Una vez ubicados se debe crear un entorno virtual para poder instalar las dependencias necesarias del proyecto, ejecutando:
```
python -m venv env
```
* Una vez creado el entorno virtual, es necesario activarlo con la siguiente l铆nea:
```
source env/bin/activate
```
* Posteriormente se deben instalar las dependencias necesarias para la correcta ejecuci贸n de la aplicaci贸n, para ello se ejecuta la siguiente l铆nea:
```
pip install -r requirements.txt
```
* Despu茅s de tener instaladas las dependencias necesarias, se podr谩 ejecutar la aplicaci贸n, ejecutando:
```
python main.py
```
_NOTA: Si la aplicaci贸n retorna un error al crear la DB se deben dar permisos de administrador o root a la carpeta para que la aplicaci贸n pueda crear la DB sin problemas, ejemplo:_

```
chmod +x carpeta_del_proyecto
```

## Ejecutando las pruebas 鈿欙笍

Para ejecutar las pruebas de la aplicaci贸n se ejecuta la siguiente linea:
```
pytest test.py
```

### 驴Qu茅 verifican las pruebas? 馃敥

_Las pruebas realizadas en esta aplicaci贸n verifican la correcta conexion a la DB y que la petici贸n a la API consumida, retorne una respuesta exitosa_

## Desarrollado con la ayuda de: 馃洜锔?

* [python](https://www.python.org/) - Lenguaje utilzado en el proyecto
* [pip](https://pip.pypa.io/en/stable/) - Administrador de dependencias
* [virtualenv](https://virtualenv.pypa.io/en/latest/) - Herramienta para crear entornos virtuales con python
* [pandas](https://pandas.pydata.org/) - Librer铆a usada para la creaci贸n de DataFrame

## Autor 鉁掞笍

* **Marcos Geovanny Esteban Mendieta** - [geofighter](https://github.com/geofighter)

## Licencia 馃搫

Este proyecto est谩 bajo la Licencia (MIT) - Para mayor informaci贸n, consulta: https://opensource.org/licenses/MIT

---
