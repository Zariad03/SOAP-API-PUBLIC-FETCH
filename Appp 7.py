from flask import Flask, request, jsonify
from zeep import Client
from zeep.exceptions import Fault

app = Flask(__name__)

# Public SOAP service
WSDL_URL = "http://www.dneonline.com/calculator.asmx?WSDL"


# Check the numbers entered by the user
def check_number(value, name):
    if isinstance(value, bool):
        raise ValueError(name + " must be a whole number.")

    if isinstance(value, float):
        raise ValueError(name + " must be a whole number.")

    try:
        number = int(value)
    except (ValueError, TypeError):
        raise ValueError(name + " must be a whole number.")

    if number < 0 or number > 10000:
        raise ValueError(name + " must be between 0 and 10,000.")

    return number


# Connect to the SOAP service and add the numbers
def calculate(number1, number2):
    try:
        number1 = check_number(number1, "Number 1")
        number2 = check_number(number2, "Number 2")

        client = Client(WSDL_URL)

        result = client.service.Add(number1, number2)

        return number1, number2, result

    except ValueError as exc:
        raise ValueError("Input error: " + str(exc))

    except Fault as exc:
        raise Exception("SOAP service error: " + str(exc))

    except Exception as exc:
        raise Exception("Connection error: " + str(exc))


# GET request
@app.route("/calculate", methods=["GET"])
def get_calculation():
    number1 = request.args.get("number1")
    number2 = request.args.get("number2")

    if number1 is None or number2 is None:
        return jsonify({"error": "Please enter both numbers."}), 400

    try:
        number1, number2, result = calculate(number1, number2)

        return jsonify({"number1": number1, "number2": number2, "result": result})

    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    except Exception as exc:
        return jsonify({"error": str(exc)}), 502


# POST request
@app.route("/calculate", methods=["POST"])
def post_calculation():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Please send a valid JSON request."}), 400

    number1 = data.get("number1")
    number2 = data.get("number2")

    if number1 is None or number2 is None:
        return jsonify({"error": "Both numbers are required."}), 400

    try:
        number1, number2, result = calculate(number1, number2)

        return jsonify({"number1": number1, "number2": number2, "result": result})

    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    except Exception as exc:
        return jsonify({"error": str(exc)}), 502


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
