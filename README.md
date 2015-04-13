# flask-example

A simple Flask-based Python HTTP server and command-line tool used to parse Playstation 3 game data from http://www.metacritic.com/game/playstation-3

- games.py: a Python program to retrieve information about Playstation games in Metacritic. Run it without arguments, and it will fetch and parse data from the Metacritic web site at http://www.metacritic.com/game/playstation-3 and will print the top three PS3 games. Output is a JSON string.

- games_server.py: a Python Web server that runs on localhost and provides a REST API for retrieving and parsing Metacritic web site data. It supports: /game end-point used to retrieve the top three PS3 games, and /game/TITLE_NAME used to retrieve information about an specific game. Output is a JSON string.

- games_lib.py: a Python library that encapsulates the logic used by the stand-alone program and HTTP server.

- games_lib_test.py: Python unit-tests for game_lib.py.
