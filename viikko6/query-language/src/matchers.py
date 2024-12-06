class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value
    
class Not:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return False
        return True
    
class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value
    
class All:
    def __init__(self):
        pass
        
    def test(self, player):
        return True

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True
        return False

class QueryBuilder:
    def __init__(self, matchers=None):
        if not matchers:
            self.matchers = list()
        else:
            self.matchers = matchers

    def plays_in(self, team):
        self.matchers.append(PlaysIn(team))
        return QueryBuilder(self.matchers)
    
    def has_at_least(self, value, attr):
        self.matchers.append(HasAtLeast(value, attr))
        return QueryBuilder(self.matchers)
    
    def has_fewer_than(self, value, attr):
        self.matchers.append(HasFewerThan(value, attr))
        return QueryBuilder(self.matchers)
    
    def one_of(self, *matchers):
        self.matchers.append(Or(*matchers))
        return self

    def build(self):
        if len(self.matchers) == 0:
            return All()
        else:
            result = And(*self.matchers)
            self.matchers.clear()
            return result

