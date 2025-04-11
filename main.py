import random
from abc import ABC, abstractmethod

class TargetUAV(ABC):
    def __init__(self, speed, altitude):
        self.speed = speed
        self.altitude = altitude
        self.status = "Активен"

    @abstractmethod
    def decision_pattern(self):
        pass

    def simulate(self):
        print(f"Полет БПЛА ({self.__class__.__name__}): "
              f"скорость={self.speed} м/с, высота={self.altitude} м")
        self.decision_pattern()

class ManeuveringTarget(TargetUAV):
    def decision_pattern(self):
        maneuver = random.choice(["Пикирование", "Разворот", "Зигзаг"])
        print(f"Маневр: {maneuver}")
        self.altitude += random.randint(-50, 50) 

class JammingTarget(TargetUAV):
    def __init__(self, speed, altitude, jamming_power):
        super().__init__(speed, altitude)
        self.jamming_power = jamming_power

    def decision_pattern(self):
        # Имитация постановки помех
        if random.random() < 0.7:
            print(f"Активные помехи мощностью {self.jamming_power} Вт")
        else:
            print("Имитация РЛС-сигнатуры")



if __name__ == "__main__":
    targets = [
        ManeuveringTarget(200, 1000),
        JammingTarget(250, 800, 500),
        ConstructionTarget(30, 500)
    ]
    
    for target in targets:
        target.simulate()
        print("-" * 40)
