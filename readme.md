# COIN IDENTIFIER!
## with keras!

Choose an image of a coin and let the app make a prediction. It will tell you the value of the coin, type of currency and country of origin.

# OPTION 1. Download Docker image and run

## Option A. Download working image from Docker Hub.

1. Pull the image `docker pull wanderdust/coin-docker`

2. Run `docker run --network="host" wanderdust/coin-docker` and find the app at `localhost:5000`

The image is around 5 gb, so be patient with the download.


## Option B. Build image using Dockerfile

1. Install docker

2. Run `docker build -t coin-app .` from app's root directory.

3. After build run `docker run --network="host" coin-app` and the app will show up in `localhost:5000`


____________________________


# Option 2. Create virtual environment and install dependencies.

Please contact me to get the pre-trained weights and model. They are too big for this repo. To avoid this use pytorch from branch master or use docker image.

## Installation
This app is built with Javascript and Python, so make sure you have `pip` and `node.js` installed. Here is an [installation guide for pip](https://pip.pypa.io/en/stable/installing/).

```
$ git clone https://github.com/wanderdust/coin-cnn-webapp.git
$ cd coin-cnn-webapp
```

## Create a virtual environment (optional)

Create the virtual environment using [virtualenv](https://virtualenv.pypa.io/en/latest/) or [anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) and activate it (I'll use conda):

```
$ conda create --name myenv
```
Activate the environment:

```
$ conda activate myenv
```

To deactivate the virtual environment:
```
$ conda deactivate
```

## Install dependencies

Install all the dependencies for both javascript and python:
```
$ npm install                               # javascript dependencies
$ pip install -r requirements.txt           # python dependencies
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

# Installation instructions for windows

Mostly the same installation but with a few differences. Before you start make sure you have `node.js` and `conda` or `miniconda` installed.

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

Install the python dependencies with pip:

```
$ pip install -r requirements.txt
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