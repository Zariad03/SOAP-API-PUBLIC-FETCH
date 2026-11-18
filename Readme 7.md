
# SOAP API Public Fetch

## What This Program Does

This program connects to a public SOAP web service using Python. It uses a calculator service to add two numbers and return the result.

The program uses Flask to create GET and POST requests. It also checks the numbers entered by the user to make sure they are whole numbers between 0 and 10,000. If something is entered incorrectly, the program displays an error message.

## How to Run

Install the required packages:

pip install flask zeep

Run the program:

python app.py

The service will run at http://127.0.0.1:5000.

## Assignment Reflection

For this assignment, I created a Python program that connects to a public SOAP web service. I chose a calculator service because it allows users to enter two numbers and receive an answer. I used Zeep to connect to the SOAP service and Flask to create GET and POST requests.

I also added checks to make sure the numbers entered were within the allowed range. If the user enters something incorrectly, the program returns an error message.

One thing that surprised me was how SOAP uses XML to communicate with other systems. I also learned how a WSDL helps Python understand how to connect to a web service. As I worked on the program, I became more familiar with connecting services and checking the information being sent. I would like to learn more about how SOAP and REST work together.
