import argparse
import requests

class Driver():
    # http://ergast.com/mrd/methods/drivers
    def drivers(self, season=None, round=None):
        url = "http://ergast.com/api/f1/drivers.json?limit=1000"
        if season:
            url = "http://ergast.com/api/f1/{}/drivers.json?limit=1000".format(season)
        if season and round:
            url = "http://ergast.com/api/f1/{}/{}/drivers.json?limit=1000".format(season, round)
        response = requests.get(url)
        if response.status_code != 200:
            return False
        return response.json()["MRData"]["DriverTable"]["Drivers"]

    def driver(self, driver_id):
        url = "http://ergast.com/api/f1/drivers/{}.json".format(driver_id)
        response = requests.get(url)
        if response.status_code != 200:
            return False
        return response.json()["MRData"]["DriverTable"]["Drivers"][0]

class Race():
    def __init__(self, season="current"):
        self.season = season

    # http://ergast.com/mrd/methods/schedule
    def races(self):
        url = "http://ergast.com/api/f1/{}.json".format(self.season)
        response = requests.get(url)
        if response.status_code != 200:
            return False
        return response.json()["MRData"]["RaceTable"]["Races"]

    # http://ergast.com/mrd/methods/results
    def result(self, round):
        url = "http://ergast.com/api/f1/{}/{}/results.json?limit=100".format(self.season, round)
        response = requests.get(url)
        if response.status_code != 200:
            return False
        result = response.json()["MRData"]["RaceTable"]["Races"]
        if result != []:
            return result[0]["Results"]
        return []

    # All results for all races
    def results(self):
        return [self.result(race["round"]) for race in self.races()]

class Season():
    def __init__(self, season="current"):
        self.season = season

    def driver_standings(self):
        url = "http://ergast.com/api/f1/{}/driverStandings.json".format(self.season)
        response = requests.get(url)
        if response.status_code != 200:
            return False
        return response.json()["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]

    def constructor_standings(self):
        url = "http://ergast.com/api/f1/{}/constructorStandings.json".format(self.season)
        response = requests.get(url)
        if response.status_code != 200:
            return False
        return response.json()["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"]

def main():
    pass

if __name__ == "__main__":
    main()
