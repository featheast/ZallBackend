from google.appengine.ext import ndb

class Match(ndb.Model):
    homeTeam = ndb.StringProperty()
    awayTeam = ndb.StringProperty()
    matchCity = ndb.StringProperty()
    time = ndb.DateTimeProperty()
    stadium = ndb.StringProperty()
    homeScore = ndb.IntegerProperty()
    awayScore = ndb.IntegerProperty()