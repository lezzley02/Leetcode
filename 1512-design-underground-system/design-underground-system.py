class UndergroundSystem(object):

     def __init__(self):
         self.customer={}
         self.station={}



     def checkIn(self, id, stationName, t):
         self.customer[id]=(stationName,t) 
        

     def checkOut(self, id, stationName, t):
         startStation,startTime=self.customer.pop(id)

         trip = startStation, stationName

         if trip in self.station:
             self.station[trip][0] += (t - startTime)
             self.station[trip][1] += 1
         else:
             self.station[trip]=[ t- startTime, 1]
        

     def getAverageTime(self, startStation, endStation):
         trip=(startStation,endStation)
         return float(self.station[trip][0]) / self.station[trip][1]


