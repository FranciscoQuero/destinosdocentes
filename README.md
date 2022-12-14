# API de Destinos Docentes

## Setup

### Local database (Docker)

Run the following command to build the Docker Compose image:

`docker-compose build`

And just run the Docker Compose daemon:

`docker-compose up`

### Remote DB (Python server)

On a Linux based machine, make sure that you have Python 3.9 and Pip 3.9 installed:

```
python --version
python -m pip --version
```

If you don't have them installed or you have a different version, install it with your package manager:

```
sudo apt update
sudo apt upgrade
sudo apt install python3.9 python-pip
```

Clone the repo and install the Python dependencies:

```
git clone https://github.com/FranciscoQuero/destinosdocentes.git
pip install -r requirements.txt
```

Run the app:

`python manage.py`

## Usage

Visit http://localhost:8000/docs to see the API docs auto generated by Fast API.
