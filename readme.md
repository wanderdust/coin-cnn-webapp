# COIN IDENTIFIER!

Choose an image of a coin and let the app make a prediction. It will tell you the value of the coin, type of currency and country of origin.

# Installation
This app is built with Javascript and Python, so make sure you have `pip` and `node.js` installed. Here is an [installation guide for pip](https://pip.pypa.io/en/stable/installing/).

```
$ git clone https://github.com/wanderdust/coin-cnn-webapp.git
$ cd coin-cnn-webapp
```

## Create a virtual environment

Create the [virtual environment ](https://virtualenv.pypa.io/en/latest/) and activate it:

```
$ virtualenv venv
```
Activate the environment:

* Activate on linux
```
$ venv/bin/activate
```

* Activate on windows
```
$ venv/Scripts/activate
```

Install all the dependencies for both javascript and python:
```
$ npm install
$ pip install -r requirements.txt
```

To deactivate the virtual environment:
```
$ deactivate
```
## Starting the app

1. Run build:
```
$ npm run build:prod
```

2. Get the server up and running in `localhost:5000`
```
$ npm start
```

## Development mode

Get the dev server up and running in `localhost:8080`
```
$ npm run dev-server
```

Run the test suite

```
$ npm run test
```

************

# Installation instructions for windows users

Pytorch library will be difficult to install via `pip` using windows, that's why windows users might prefer using `conda` as their environment manager. Before you start make sure you have `node.js` and `conda` or `miniconda` installed.

```
$ git clone https://github.com/wanderdust/coin-cnn-webapp.git
$ cd coin-cnn-webapp
```
## Create a virtual environment

Create the [virtual environment ](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) and activate it:

```
$ conda create --name condaenv
$ conda activate condaenv
```

To deactivate the environment:
```
$ conda deactivate
```

## Install dependencies

Install the javascript dependencies with npm:
```
$ npm install
```

Install the python dependencies with conda:

* Install pytorch (cpu):
```
$ conda install pytorch-cpu torchvision-cpu -c pytorch
```

* Install rest of dependencies:

```
$ conda install flask flask-cors numpy pillow
```

## Starting the app

1. Set the environment variables for flask. You only need to run this once:

```
$ npm run start-windows
```

2. Build the app:
```
$ npm run build:prod
```

3. Start the app:
```
$ python server.py
```

## Development mode

Get the dev server up and running in `localhost:8080`
```
$ npm run dev-server
```

Run the test suite
```
$ npm run test
```
