import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_oikean_pelaajan_etsiminen(self):
        self.assertAlmostEqual(str(self.stats.search("Semenko")), str(Player("Semenko", "EDM", 4, 12)))

    def test_vaaran_pelaajan_etsiminen(self):
        self.assertAlmostEqual(self.stats.search("Litmanen"), None)

    def test_joukkueen_pelaajat(self):
        edmonton_pelaajat = [
            Player("Semenko", "EDM", 4, 12),
            Player("Kurri",   "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89)
            ]

        self.assertAlmostEqual(str(self.stats.team("EDM")[0]), str(edmonton_pelaajat[0]))
        self.assertAlmostEqual(str(self.stats.team("EDM")[1]), str(edmonton_pelaajat[1]))
        self.assertAlmostEqual(str(self.stats.team("EDM")[2]), str(edmonton_pelaajat[2]))
        self.assertAlmostEqual(len(self.stats.team("EDM")), 3)
    
    def test_eniten_pisteitä(self):
        self.assertAlmostEqual(str(self.stats.top(0)[0]), str(Player("Gretzky", "EDM", 35, 89)))
        self.assertAlmostEqual(len(self.stats.top(0)), 1)

    def test_tilastojen_sorttausperuste(self):
        self.assertAlmostEqual(str(self.stats.top(0)[0]), str(Player("Gretzky", "EDM", 35, 89)))
        self.assertAlmostEqual(str(self.stats.top(0, SortBy.POINTS)[0]), str(Player("Gretzky", "EDM", 35, 89)))
        self.assertAlmostEqual(str(self.stats.top(0, SortBy.GOALS)[0]), str(Player("Lemieux", "PIT", 45, 54)))
        self.assertAlmostEqual(str(self.stats.top(0, SortBy.ASSISTS)[0]), str(Player("Gretzky", "EDM", 35, 89)))