# Python class that is able to return the flight distance between two citites given their
# longitude and latitude co-ordinates.
from math import radians,cos,sin,asin,sqrt


class CityDistance:
    """
    Calculates the distance between two provided longitude and latitude points.
    Uses haversine formula as inner class.
    :method
    :process_cordinates : Provides the latitude and latitude on the provided string input.
    """
    
    def __init__(self,city_1,city_2):
        self.city_1 = city_1
        self.city_2 = city_2
        self.lat1,self.lon1 = self.process_cordinates(self.city_1)
        self.lat2,self.lon2 = self.process_cordinates(self.city_2)
        self.distance = self.HaversineFormula(self.lat1,self.lon1,self.lat2,self.lon2).haversine_formula()
     
    def process_cordinates(self,city):
        co_list = []
        for x in city.split(","):
            co_list.append(x.strip())
        lat1_p = float(co_list[0].split(" ")[0].strip())
        lat1_d = co_list[0].split(" ")[1]
        lat1_p = (-1)*lat1_p if lat1_d in ['W','S'] else lat1_p
        lon1_p = float(co_list[1].split(" ")[0].strip())
        lon1_d = co_list[1].split(" ")[1]
        lon1_p = (-1)*lon1_p if lon1_d in ['W','S'] else lon1_p 
        
        self.lat = lat1_p
        self.lon = lon1_p
        return self.lat,self.lon
        
            
    class HaversineFormula:
        """
        Calculates the distance on the basis of provided longitude and latitide of two points.j
        : param lat1 : latitude of point1
        : param lon1 : longitude of point1
        : param lat2 : latitude of point2
        : param lon2 : latitude of point2
        : method:
        : haversine_formula : Calculates the distance between two points on the basis of provided parameters.
        """
        def __init__(self,lat1,lon1,lat2,lon2):
            self.lat1 = radians(lat1)
            self.lon1 = radians(lon1)
            self.lat2 = radians(lat2)
            self.lon2 = radians(lon2)
    
        def haversine_formula(self):
            self.dlon = self.lon2 - self.lon1
            self.dlat = self.lat2 - self.lat1
            a = sin(self.dlat/2)**2 + cos(self.lat1)*cos(self.lat2)*sin(self.dlon/2)**2
            c = 2*asin(sqrt(a))
            r = 6731
            self.distance = c * r
            return self.distance


# # Driver Program # #
city1 = str(input("City 1:"))
# city1 = "51.5074 N, 0.1278 W"
city2 = str(input("City 2:"))
# city2 = "48.8566 N, 2.3522 E"
obj = CityDistance(city1,city2)
print("Output : City 1 and City 2 are {0} km apart.".format(str(obj.distance)))