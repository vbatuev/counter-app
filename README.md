# counter-app
Simple python flask application that counts page visits and adds recotdb to mongodb database.

###  To build app:

`docker build -t counter-app .`

###  To run container:
`docker run --name counter-app -p 5000:5000 -e MONGODB_URL=mongodb://host:port counter-app`

###  Or you just can use:
`docker-compose up -d` 

Then open in your favourite browser http://localhost:5000
