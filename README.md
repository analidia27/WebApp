# WebApp
## Introducción
Para hacer uso del proyecto de manera local es necesario realizar los siguientes pasos:

1) Ingresar los siguiente comandos en consola:

```python
python3 -m venv [nombreDelEntornoVirtual]
```

este comando les creara un entorno virtual para para poder importar posteriormente los paquetes ahi.Para activarlo se emplea el siguiente comando:

```python
source nombreDelEntornoVirtual/bin/activate
```
NOTA: en caso de trabajar con windows el entorno virtual se genera con scripts para activar el entorno virtual por ende se tiene que acceder de la siguiente forma:
```python
nombreDelEntornoVirtual\Scripts\activate.bat
```
y para apagarlo (en ambos casos) es:

```python
deactivate
```

2) despues correr el siguiente comando para obtener los paquetes empleados en la API:

```python
pip install -r requirements.txt
```

