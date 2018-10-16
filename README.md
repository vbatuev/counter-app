# counter-app
Simple python flask application that counts page visits and adds records to the mongodb database.

###  To build app:

`docker build -t counter-app .`

###  To run container:
`docker run --name counter-app -p 5000:5000 -e MONGODB_URL=mongodb://host:port counter-app`

###  Or you just can use:
`docker-compose up -d` 

Then open in your favourite browser http://localhost:5000

You can also find this image on [docker hub](https://hub.docker.com/r/vbatuev/counter-app/).

To deploy in google cloud please check [this repo](https://github.com/vbatuev/gce-counter-app)

## TODO:
- Add tests
- Add CI
