# Biblioteca Alkemy 📚🚀
## Introducción:
Proyecto "WebApp" de Bootcamp Django - Alkemy 2023 basado en el caso de negocio N°2: "Biblioteca App".
## Tabla de contenidos:
- [Autores](#autores👀)
- [Tecnologias](#tecnologias-👨‍💻)
- [Entornos Compatibles](#entornos-compatibles-💻)
- [Instalación](#instalación🤖)
- [Modulos](#modulos-🚨)


## Autores👀
- [Pablo Sandoval](https://github.com/SPablo2191)
- [Ana Mechaca](https://github.com/analidia27)
- [Dario Heredia](https://github.com/deheredia)

## Tecnologias 👨‍💻
![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Django](https://img.shields.io/badge/Django-4.0-brightgreen.svg)
![Jinja2](https://img.shields.io/badge/Jinja2-3.0-brightgreen.svg)

## Entornos Compatibles 💻
![macOS](https://img.shields.io/badge/macOS-compatible-green)
![Linux](https://img.shields.io/badge/Linux-compatible-green)
![Windows](https://img.shields.io/badge/Windows-compatible-green)

## Instalación🤖
Para hacer uso del proyecto de manera local es necesario realizar los siguientes pasos:

1) Ingresar los siguiente comandos en consola:

```cmd
python3 -m venv [nombreDelEntornoVirtual]
```

este comando les creara un entorno virtual para para poder importar posteriormente los paquetes ahi.Para activarlo se emplea el siguiente comando:

```cmd
source nombreDelEntornoVirtual/bin/activate
```
NOTA: en caso de trabajar con windows el entorno virtual se genera con scripts para activar el entorno virtual por ende se tiene que acceder de la siguiente forma:
```cmd
nombreDelEntornoVirtual\Scripts\activate.bat
```
y para apagarlo (en ambos casos) es:

```cmd
deactivate
```

2) despues correr el siguiente comando para obtener los paquetes empleados en la API:

```cmd
pip install -r requirements.txt
```

3) Una vez los paquetes fueron instalados con exito, se debe realizar las migraciones:
```cmd
python manage.py migrate
```
4) Crear un superusuario para acceder al modulo admin:
```cmd
python manage.py createsuperuser
```
5) Levantar el servidor:
```cmd
python manage.py runserver
```
6) ¡Listo! ya puede visitar la pagina web en este [enlace](http://127.0.0.1:8000/). 

## Modulos 🚨
- [socios](#socios)
- [API](#api)
### Socios

| Método | Path | Descripción |
| ------ | -------- | ----------- |
| POST    | [socios/nuevo](#registrar-y-editar-un-socio) | Registrar un nuevo socio |
| GET   | [socios/listado](#listado-de-socios) | Recuperar el listado de socios |
| POST    | [socios/editar/<int:id>](#registrar-y-editar-un-socio) | Editar un socio por su id |
| POST    | [socios/estado/<int:id>](#cambiar-estado-de-socio) | Cambiar el estado de un socio de activo a inactivo o viceversa |

#### **Registrar y Editar un socio**:
Al acceder a esta vista, se da la posilibidad al usuario para registrar un nuevo socio empleando un formulario. En caso de acceder pasando el id de un socio registrado, se carga la información actual de ese socio para poder ser modificada.

**Registrar:**

![Registrar Socio](screenshots/partner_create_update.png)

**Editar:**

![Editar Socio](screenshots/partner_update.png)

**Código:**
```python
def create_update_partner(request, id=None):
    if(id):
        """ Si se envia el id del socio se obtiene el objeto y se crea el formulario con datos, 
        sino se crea el formulario vacio"""
        try: 
            requested_partner = Partner.objects.get(id=id)
            form = PartnerForm(instance=requested_partner) 
        except Exception:
            return render(request, 'error.html')
    else:
        form = PartnerForm()
        
    if request.method == "POST":
        if(id):
            form = PartnerForm(request.POST,instance=requested_partner) 
        else:
            form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/socios/listado')

        else:
            return HttpResponseRedirect('create_partner/')
        
    context = {'form': form,'is_update': id != None}
    
    return render(request, 'create_partner.html', context)
```
#### **Listado de socios**:
Al acceder a esta vista se cargan todos los socios (activos como inactivos) en una tabla:

![Listado de socios](screenshots/partner_list.png)

**Código**:
```python
def list_partners(request):

    partners = Partner.objects.all()

    context = {
        'partners' : partners
    }
    
    return render(request, 'list_partners.html', context=context)
```
#### **Cambiar estado de socio**:
 Si el socio esta en estado activo pasa a estar inactivo y viceversa. Se realiza desde la vista de listado por medio de la tabla, tomando el id de ese socio puntualmente.

 ![Cambiar estado](screenshots/partner_list.png)
 **Código**:
 ```python
 def change_status_partner(request,id):
    partner = Partner.objects.get(id=id)
    if partner.is_active:
        partner.is_active = False
    else:
        partner.is_active = True
    partner.save()
    return redirect('list_partners') 
 ```
 ### API
 | Método | Endpoint | Descripción |
| ------ | -------- | ----------- |
| GET    | [api/libros](#listado-de-libros) | Recuperar todos los libros registrados |
| GET   | [api/libros/<int:id>](#socio-registro) | Recuperar un libro por su ID |
#### **Listado de libros**:
Se recupera el listado de libros y se retorna en formato JSON.

 ![Listado de libros](screenshots/api_books.png)

**Código:**
```python
def list_books_json(request):
    books = Book.objects.all().values('id', 'title','author')
    if(books):
        list_books = list()
        for book in books:  
            item = list(book.values())
            temp_book = {}
            temp_book['id'] = item[0]
            temp_book['titulo'] = item[1]
            temp_book['autor'] = str(Author.objects.get(id=item[2]))
            list_books.append(temp_book)

    else:
        list_books = list()
    data = {
        'libros': list_books
    }
    return HttpResponse(json.dumps(data, ensure_ascii=False).encode('utf-8'), content_type="application/json") 
```
#### **Libro por su ID**:
Se recupera un libro por su ID y se retorna en formato JSON. En caso de no existir se retorna un array vacio.

![libro por ID](screenshots/api_book_id.png)
**Código:**
```python
def book_json(request, id):

    if request.method == 'GET':
        try:

            book = Book.objects.get(id = id)

            data = {
                'Libro': {
                    'id' : id,
                    'titulo' : book.title,
                    'descripcion' : book.description,
                    'autor' : str(book.author)
                    }
            }

            return JsonResponse(data)
        
        except:
            msj = {
                'Libro' : []
                }

            return JsonResponse(msj)
```