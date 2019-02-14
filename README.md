# DJango Boilerplate

Requisitos de software previamente instalado:

+ Python 3.5
+ Python PIP

### Descipción

En caso de usar el servicio en python (Linux):

    $ sudo pip install virtualenv
    $ virtualenv -p python3 <<nombre_ambiente>>
    $ cd <<nombre_ambiente>>
    $ source bin/activate

En caso de usar el servicio en python (Windows):

    > python -m venv <<nombre_ambiente>>
    > cd <<nombre_ambiente>>/Scripts
    > activate.bat

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

### Ejeuctar Pruebas Unitarias

Run all the tests in the animals.tests module

    $ ./manage.py test animals.tests

Run all the tests found within the 'animals' package

    $ ./manage.py test animals

Run just one test case

    $ ./manage.py test animals.tests.AnimalTestCase

Run just one test method

    $ ./manage.py test animals.tests.AnimalTestCase.test_animals_can_speak


### PyLint

    $ pylint <archivo>.py --reports=yes
    $ pylint **/*.py --reports=yes

---

Fuentes:

+ https://github.com/pepeul1191/django-pp
+ https://github.com/pepeul1191/django-boilerplate-v2
+ https://docs.djangoproject.com/es/2.1/topics/testing/overview/
+ https://docs.python.org/3/library/unittest.html#unittest.TestCase
