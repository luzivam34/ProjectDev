from flask import Blueprint, render_template

materia_bp = Blueprint('materia', __name__)

@materia_bp.route("/python")
def python_materia():
    return render_template("materiapython.html")