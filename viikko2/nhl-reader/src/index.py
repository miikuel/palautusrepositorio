import requests
from player import Player

class PlayerReader():
    def __init__(self, url):
        self.url = url
        self.players = []

    def get_players(self):
        response = requests.get(self.url).json()

        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)
        

class PlayerStats():
    def __init__(self, reader):
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality):
        players_of_country = []
        for player in self.players:
            if player.nationality == nationality:
                players_of_country.append(player)
        return sorted(players_of_country, key=lambda player: player.goals + player.assists, reverse=True)


def main():

    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    reader.get_players()
    stats = PlayerStats(reader)
    players_by_nationality = stats.top_scorers_by_nationality('FIN')

    for player in players_by_nationality:
        print(player)

if __name__ == "__main__":
    main()
