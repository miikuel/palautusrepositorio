from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or, QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)


    query = QueryBuilder()

    # matcher = query.plays_in("NYR").has_at_least(10, "goals").has_fewer_than(20, "goals").build()


    # m1 = (
    # query
    #     .plays_in("PHI")
    #     .has_at_least(10, "assists")
    #     .has_fewer_than(10, "goals")
    #     .build()
    # )

    # m2 = (
    # query
    #     .plays_in("EDM")
    #     .has_at_least(50, "points")
    #     .build()
    # )

    # matcher = query.one_of(m1, m2).build()

    matcher = (
    query
        .one_of(
        query.plays_in("PHI")
            .has_at_least(10, "assists")
            .has_fewer_than(10, "goals")
            .build(),
        query.plays_in("EDM")
            .has_at_least(50, "points")
            .build()
        )
        .build()
    )
        
    print()
    for player in stats.matches(matcher):
        print(player)



if __name__ == "__main__":
    main()
