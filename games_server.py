#!/usr/bin/python

import games_lib
from flask import Flask

app = Flask(__name__)

@app.route('/games', methods=['GET'])
def get_top_games():
  return games_lib.get_top_games()

@app.route('/games/<string:title>', methods=['GET'])
def get_top_games_num(title):
  return games_lib.get_game(title=title)


if __name__ == '__main__':
  app.run(debug=True)
