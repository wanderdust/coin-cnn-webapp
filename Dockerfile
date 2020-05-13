FROM python:3.7

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get install -y nodejs


# Create app directory
WORKDIR /app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package-lock.json ./package-lock.json
COPY package.json ./package.json
COPY ./requirements.txt /app/requirements.txt

RUN npm install
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD [ "npm", "start" ]

