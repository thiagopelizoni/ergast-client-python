# Formula 1 open API client

This is a simple client for [Ergast Developer API ](http://ergast.com/mrd/).



# Drivers

```
from ergast import Driver

driver = Driver()

driver.drivers()
driver.drivers(season="current")
driver.drivers(season=2019)
driver.drivers(season="current", round=1)
driver.drivers(season=2019, round=1)

driver.driver("hamilton")
driver.driver("senna")
```
