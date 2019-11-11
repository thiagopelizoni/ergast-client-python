# Formula 1 open API client

This is a simple client for [Ergast Developer API](http://ergast.com/mrd/).

Because of Ergast API is public, sometimes happens timeouts.

The delay for the informations sometimes is great after the finish of a racing for example.

# Trying out

There's a list below that contains all options available to use this library.

There'll be a same method be invoked using others params just in order to show you another way to use it.

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

# Circuits

```
from ergast import Circuit

circuit = Circuit()

circuit.circuits()
circuit.circuits(season=2019)
circuit.circuits(season=2019, round=1)

circuit.find("monaco")
```

# Standings

```
from ergast import Standings

standings = Standings()
standings = Standings(season=2019)

standings.drivers()
standings.constructors()
```

# Races

```
from ergast import Race()

race = Race() # set the season as actual
race = Race(season=2019)

race.races() # All races from a specific season
race.result(round=1) # Results for the round 1
race.results() # All results for all races given a season
```
