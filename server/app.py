from flask import Flask

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# Print string route
@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # Output the string in the console
    return text  # Return only the string

# Count route
@app.route('/count/<int:number>')
def count(number):
    numbers_list = '\n'.join(str(i) for i in range(0, number))  # Join the numbers with newlines
    return numbers_list + '\n'  # Add a trailing newline for the test

# Math operations route
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero!"  # Handle division by zero
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation!"  # Handle invalid operations

    return str(result)  # Return only the result

if __name__ == '__main__':
    app.run(debug=True)