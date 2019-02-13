# DJango Boilerplate

Requisitos de software previamente instalado:

+ Python 3.5
+ Python PIP

### Descipción

En caso de usar el servicio en python:

    $ sudo pip install virtualenv
    $ virtualenv -p python3 <<nombre_ambiente>>
    $ cd <<nombre_ambiente>>
    $ source bin/activate

Arrancar aplicación:

    $ cd <<carpeta-proyecto>>
    $ pip install -r requirements.txt
    $ python app.py

### Comandos de DJango

    $ python manage.py startapp polls # crear aplicación
    $ pip install -r requirements.txt
    $ python manage.py runserver 192.168.1.9:8080
    $ python manage.py runserver localhost:8080
    $ python manage.py runserver

Ejecuar DJango con acceso a static con error404:

    $  python manage.py runserver localhost:8080 --insecure

### PyLint

    $ pylint <archivo>.py --reports=yes
    $ pylint **/*.py --reports=yes

---

Fuentes:

+ https://github.com/pepeul1191/django-pp
+ https://github.com/pepeul1191/django-boilerplate-v2
