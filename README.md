# Formula 1 open API client

This is a simple client for [Ergast Developer API](http://ergast.com/mrd/).



# Drivers

```
from ergast import Driver

driver = Driver()

driver.drivers()
driver.drivers(season="current")
driver.drivers(season="current", round=1)
driver.drivers(season=2019)
driver.drivers(season=2019, round=1)

driver.find("hamilton")
driver.find("senna")
```

# Constructors

```
from ergast import Constructor

constructor = Constructor()

constructor.constructors()
constructor.constructors(season="current")
constructor.constructors(season="current", round=1)
constructor.constructors(season=2019)
constructor.constructors(season=2019, round=1)

constructor.find("williams")
constructor.find("ferrari")
```

# Races

```
from ergast import Race()

race = Race()

race.races()
race.result(round=1)
race.results() # All results for all races
```
