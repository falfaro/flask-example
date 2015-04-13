#!/usr/bin/python

import re
import json
import urllib2

# Regular expression used to match game entries and extracting title and score
# using Python named groups.
title_re = re.compile(r"""
<div\ class="basic_stat\ product_title">
\s*
<h3\ class="product_title">
\s*
<a\ href="/game/playstation-3/[^"]*">
\s*
(?P<title>[^<]+)                                     # Title name
</a>
\s*
</h3>\s*</div>
\s*
<a\ class="basic_stat\ product_score"\ href="[^"]*">
\s*
<span\ class="[^"]*">
\s*
(?P<score>\d+)                                        # Score
\s*
</span>""", re.VERBOSE)


def _get_games(data, num_matches=None, title=None):
  """Retrieve game data.

  Args:
    data: str, HTML contents as retrieved from the Metacritics web site
    num_matches: optional int, number of matches to return
    title: optional str, game title to retrieve. If no game titlte is
           specified all game titles (up to num_matches) are retrieved

  Returns:
    A Python list where each item is a dict of 'title' and 'score'
  """
  matches = title_re.finditer(data)
  if num_matches:
    matches = list(matches)[:num_matches]
  games = []
  for match in matches:
    if title and title != match.group('title'):
      continue
    games.append({
      'title': match.group('title'),
      'score': match.group('score'),
      })
  return games

def _get_games_data():
  req = urllib2.Request('http://www.metacritic.com/game/playstation-3',
                        headers={'User-Agent' : "Firefox"})
  con = urllib2.urlopen( req )
  return con.read()

def get_top_games():
  data = _get_games_data()
  games = _get_games(data, num_matches=3)
  return json.dumps(
    games,
    sort_keys=True,
    indent=4, separators=(',', ': '))

def get_game(title):
  data = _get_games_data()
  games = _get_games(data, title=title)
  return json.dumps(
    games,
    sort_keys=True,
    indent=4, separators=(',', ': '))
