from flask import render_template
from . import main

@main.app.errorhandler(404)
def four_w_four(error):
    """
    Function to render the 404 error page
    """
    
    return render_template("four0four.html"), 404