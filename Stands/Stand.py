from pydub import AudioSegment
from pydub.playback import play
class Stand():

    def __init__(self, name, power, speed, standRange, precision, developmentPotential, health):
        self.name = name
        self.power = power
        self.speed = speed
        self.standRange = standRange
        self.precision = precision
        self.developmentPotential = developmentPotential
        self.health = health

    def Barrage(self, battleCry):
        print(f"{self.name} {battleCry} barraged you!")

    def Punch(self):
        print(f"{self.name} has punched you!")


class GoldExperience(Stand):

    def Heal(self):
        self.health += 10
        song = AudioSegment.from_mp3("C:/Python/Stands/7PageMuda.mp3")
        play(song)
        print(f"{self.name} has healed him self!")

class TheWorld(Stand):

    def ThrowKnife(self, enemy):
        enemy.health -= 10
        print(f"{enemy.name} is hurt by knife that {self.name} Throwed")