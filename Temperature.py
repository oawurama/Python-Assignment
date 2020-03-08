
class Temperature:
    def __init__(self,temperature):
        self.temperature = temperature
    def Celsius_to_Fahrenheit(self):
        print ("{} degrees Celsius converted to Fahrenheit is {}".format (self.temperature,((9/5 * self.temperature )+ 32)))
    def Fahrenheit_to_Celsius(self):
        print ("{} Fahrenheit converted to degree Celsius is {}".format (self.temperature,((self.temperature-32)*5/9)))

               
temp = Temperature(100)
temp.Celsius_to_Fahrenheit()
temp.Fahrenheit_to_Celsius()
