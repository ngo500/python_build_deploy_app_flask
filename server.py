from flask import Flask, render_template, request
from Math.math import summation, subtraction, multiplcation

app = Flask("Mathematics Problem Solver")

@app.route("/sum", methods=['GET'])
def sum_route():
    """
    Get 2 float arguments from request, then return their sum as a string
    Returns:
    String result of sum of 2 given floats
    """
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = summation(num1, num2)
    return str(result)

@app.route("/sub", methods=['GET'])
def sub_route():
    """
    Get 2 float arguments from request, then return their difference as a string
    Returns:
    String result of difference of 2 given floats
    """
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = subtraction(num1, num2)
    return str(result)

@app.route("/mul", methods=['GET'])
def mul_route():
    """
    Get 2 float arguments from request, then return their product as a string
    Returns:
    String result of product of 2 given floats
    """
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = multiplcation(num1, num2)
    return str(result)

@app.route("/", methods=['GET'])
def render_index_page():
    """
    Render the index.html page
    Return:
    Always renders the index.html page
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
