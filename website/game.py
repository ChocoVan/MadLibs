from flask import Blueprint, render_template

game = Blueprint('game', __name__)

# prompt users to enter in words based on what that
# certain madlibs require 

@game.route('/play')
def play():
    return render_template("game.html")