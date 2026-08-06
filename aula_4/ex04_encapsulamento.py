class Sensor:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    def set_temperatura(self, temperatura):
        if -50 <= temperatura <= 150:
            self.__temperatura = temperatura
        else:
            print("Erro: temperatura fora do limite fisico do sensor (-50 a 150)")

    def status(self):
        if -50 <= self.__temperatura <= 80:
            return "Normal"
        elif 81 <= self.__temperatura <= 120:
            return "Alerta"
        else:
            return "Critico"


sensor1 = Sensor(25)
print(sensor1.status())

sensor1.set_temperatura(95)
print(sensor1.status())

sensor1.set_temperatura(135)
print(sensor1.status())

sensor1.set_temperatura(-30)
print(sensor1.status())
