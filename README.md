# fibonacci-series-RESTful-service-with-Flask-and-mongodb
Simple Fibonacci series using Flask framework


# Requirements:

flask == 1.1.2\
flask-restful == 0.3.8\
mongoengine == 0.20.0\
flask-mongoengine == 0.9.5\
flask-cors == 3.0.8\
py-healthcheck == 1.10.1


# Description
the Framework used is Flask and MongoDB as database to store and retrieve from it the list of Fibonacci sequences\. I have additionally made a health check that checks if the application is successfully running.

RESTful service in Python that features the following endpoints (this can be used as a larger application).

• GET /fib/<number>: Given a number, I find all combinations of fibonacci number that add up to
that particular number.


• GET /health: Return health information of the service.
  
• Framework: Flask.

• Database: MongoDB
 
• Dockerized!
  
# Side note

A fibonacci sequence is being calculated as follows: fn = fn−1 +fn−28n > 2;\
with the first two numbers being f1 = f2 = 1 are excluded from the sequence, therefore f1 = 2.\
For instance »/fib/11« the response is a list of all possible combinations with a status code 200.
[ [2, 2, 2, 2, 3], [2, 2, 2, 5], [2, 3, 3, 3], [3, 3, 5], [8, 3] ]

  
