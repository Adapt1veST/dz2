class Grandfather:
    eyes = 2
    print("Blue eyes")
class Grandmother(Grandfather):
    arms = 2
    print("Normal arms")  
class Father(Grandmother):
    legs = 2
    print("Normal legs")
class Mother(Father):
    height = 170
    print("Black hair")
class Son(Mother):
    weight = 40
    print("Strong")  
class Daughter(Son):
    pretty = 100
    print("Pretty") 

vika = Daughter()
print(vika)
print(vika.eyes)
print(vika.arms)
print(vika.legs)
print(vika.height)
print(vika.weight)
print(vika.pretty)

print("Next dz")

class Max:
  weight1 = 50
  height1 = 170
  def __init__(self):
      self.weight2 = 40
      self.height2 = 160
  def maxik(self):
      print(self.weight1)
      print(self.height1)
class Vika(Max):
  def viko(self):
      print(self.weight2)
      print(self.height2)
max1 = Max()
max1.maxik()
vika1 = Vika()
vika1.viko()