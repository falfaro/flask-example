#!/usr/bin/python

import unittest
import games_lib

class TestStringMethods(unittest.TestCase):

    TEST_DATA = """<html xmlns:og="http://opengraphprotocol.org/schema/"
xmlns:fb="http://ogp.me/ns/fb#">
<head>
<title>Playstation 3 Game Reviews, Articles, Trailers and more at Metacritic - Metacritic</title>
</head>
<body>
<ol class="list_products list_product_summaries">
<li class="product has_small_image first_product"><div class="wrap product_wrap"><div class="product_basics stats"><div class="basic_stats has_score"><div class="main_stats"><div class="basic_stat product_title"><h3 class="product_title"><a href="/game/playstation-3/under-night-in-birth-exelate">Under Night In-Birth Exe:Late</a></h3></div><a class="basic_stat product_score" href="/game/playstation-3/under-night-in-birth-exelate"><span class="metascore_w medium game positive">80</span></li>

<li class="product has_small_image alt"><div class="wrap product_wrap"><div class="product_basics stats"><div class="basic_stats has_score"><div class="main_stats"><div class="basic_stat product_title"><h3 class="product_title"><a href="/game/playstation-3/atelier-shallie-alchemists-of-the-dusk-sea">Atelier Shallie: Alchemists of the Dusk Sea</a></h3></div><a class="basic_stat product_score" href="/game/playstation-3/atelier-shallie-alchemists-of-the-dusk-sea"><span class="metascore_w medium game positive">75</span></li>
</body>
</html>"""

    def test_get_games(self):
        actual_result = games_lib._get_games(self.TEST_DATA, num_matches=3)
        expected_result = [
            {
                'score': '80',
                'title': 'Under Night In-Birth Exe:Late'
            },
            {
                'score': '75',
                'title': 'Atelier Shallie: Alchemists of the Dusk Sea'
            },
        ]
        self.assertEqual(expected_result, actual_result)

    def test_get_game(self):
        expected_result = [
            {
                'score': '75',
                'title': 'Atelier Shallie: Alchemists of the Dusk Sea'
            },
        ]
        actual_result = games_lib._get_games(
            self.TEST_DATA, title=expected_result[0]['title'])
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
