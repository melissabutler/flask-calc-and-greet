# Put your app in here.
from flask import Flask, request

from flask_debug import Debug

from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def add_int():
    """Add a and b together"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a, b))


@app.route('/sub')
def sub_int():
    """Subtract a from b """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a, b))


@app.route('/mult')
def mult_int():
    """Multiply a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a, b))


@app.route('/div')
def div_int():
    """Divide a by b """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a, b))

operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<oper>')
def do_math(oper):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = operations[oper](a,b)

    return str(result)