class TrainSystem:

    def __init__(self):
        self.customers = {}
        self.placesAvgTime = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.customers.keys():
            self.customers[id].append([stationName, t])
        else:
            self.customers[id] = [[stationName, t]]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin = self.customers[id][0]
        del self.customers[id][0]
        destination = tuple([checkin[0], stationName])
        if destination in self.placesAvgTime.keys():
            totalTrips = self.placesAvgTime[destination][1]
            averageTime = self.placesAvgTime[destination][0]
            self.placesAvgTime[destination] = [((t-checkin[1])+averageTime*totalTrips)/(totalTrips+1), totalTrips+1]
        else:
            self.placesAvgTime[destination] = [t-checkin[1], 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = tuple([startStation, endStation])
        if route in self.placesAvgTime.keys():
            return self.placesAvgTime[route][0]
        return -1

# Your TrainSystem object will be instantiated and called as such:
# obj = TrainSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
