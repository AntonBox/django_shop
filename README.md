# Project Django Shop

## Prerequisites

- Python 3.5
- pip
- virtualenv (or pew)
- PostgreSQL

## Installation

### 1. Create virtualenv

#### If you are using pew:

```
    pew new -p python3.5 shop
    pew workon shop
```

#### If you are using virtualenv:

In the project directory:

```
    virtualenv .env
    source .env/bin/activate
```

### 2. Install dependencies

#### Install neccessary *-dev packages::

```
    sudo apt-get install python3-dev
```

#### Pillow package dependencies:

```
    sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
```

#### Django dependencies:

```
    pip install -r requirements-dev.txt
```

### 3. Create local_settings.py file

```
    cp root/local_settings.py.default root/local_settings.py
```

### 4. Database:

#### Install PostgreSQL.

#### Create database:

```
    sudo -i -u postgres
    createuser shop -P
    createdb shop -O shop
    exit
```

#### Migrate database:

```
    python manage.py migrate
```

### 5. Create super user so you can login to admin panel

```
    python manage.py createsuperuser
```


### 6. Run project:

```
    make run
```
