# Simple car Api

POST /cars
```
body : {
    make : string,
    model : string,
}
```
checked against  https://vpic.nhtsa.dot.gov/api/ if given car make and model exists

POST /rate
```
body : {
    make : string,
    model : string,
    rate : integer
}
```
if given car make and model exist in db create a rating for car


GET /cars
get all cars in database with average rate and rate count 

GET /popular
get TOP 5 cars from database with most rates


# Rest Api in Django
Libraries: 
- Django 3
- Django Rest Framework
- drf-yasg (swagger for DRF)
- Pandas

# Database
PostgreSQL
# Orchestrated by
Docker-compose
