#number
num1 = int(2.7)
print(num1)  
print(type(num1))  
num2 = int(-32.8)
print(num2) 
print(type(num2))
num3 = float(5)
print(num3)
print(type(num3))
num4 = complex("3+5j")
print(num4)
print(type(num4))

a = 6 + 4j
b = 3 + 2j

print("a * 2 = ", a * 2)
print("a / 2 = ", a / 2)
print("a ** 2 = ", a ** 2)
print("a + b = ", a + b)
print("a - b = ", a - b)

import random
print(random.randrange(20, 200))
print(random.randint(20, 200))
print(random.uniform(20, 200))
print(random.random())

a = abs(-5.25)
b = pow(4, 3)
print(a)
print(b)
x = min(6, 36, 256)
y = max(4, 12, 144)
print(x)
print(y)

import math
k = math.sqrt(361)
x = math.ceil(25.4)
y = math.floor(25.4)
z = math.pi
print(k)
print(x)
print(y)
print(z)

#strings
book_name = "Crime And Punishment"
print(book_name)
print(book_name[2:-6])
print(book_name[::])
print(book_name[::-1])
print(len(book_name))
print(book_name.upper())
print(book_name.lower())
print(book_name.title())
print(book_name.capitalize())
print(book_name.isupper())
print(book_name.islower())
print(book_name.istitle())
date = "1866"
x = date.isalnum()
print(x)
x = date.isalpha()
print(x)
print(book_name.split())
print(book_name.replace("And", "Or"))
print(book_name.count("Crime"))
x = "Crime"
y = "And"
z = "Punishment"
print(x + " " + y + " " + z)
print(x, y, z)
sentence = "{} published in {}"
print(sentence.format(book_name, date))
book_name = "Crime \nAnd \tPunishment"
print(book_name)

#booleans
print(100 < 99)
print(25 > 20)
print(18 == 18)
print(40 != 90)
print(9 * 8 == 70)
print(6 > 5 and 20 == 5 * 4)
print(18 == 18 and 70 < 66)
print(15 % 3 == 1 and 16 + 20 > 40)
print(30 > 33 and 15 == 3 + 12)
print(80 > 5 or 30 == 30)
print(9 != 11 or 70 < 66)
print(15 // 3 == 6 or 16 + 20 > 40)
print(80 > 93 or 68 < 69)
print(bool("book"))
print(bool(210904))
print(bool(0))
print(bool(True))
print(bool(False))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
a = 210
print(isinstance(a, float))
print(int(True))
print(int(False))
print(type(False))
print(type(True))

#lists
planets = ["Mercury", "Venus", "Earth", "Mars"]
print(len(planets))
print(type(planets))
print(planets[-3])
print(planets[2:4])
x = planets.index("Earth")
print(x)
others = ["Jupiter", "Saturn"]
planets.extend(others)
print(planets)
planets.append("Uranus")
print(planets)
planets.insert(6, "Pluto")
print(planets)
planets[2] = "Neptune" 
print(planets)
planets.remove("Pluto")
print(planets)
planets.sort()
print(planets)
planets.reverse()
print(planets)
num = [17, 18, 19]
list1 = planets + num
print(list1)
print(planets.pop(4))
planets.clear()
print(planets)

#tuples
mix = ("abc", 21, True)
print(mix)
brands = ("Vans", "Nike", "Puma", "Amazon", "Ford")
print(len(brands))
print(type(brands))
print(brands.count("Sony"))
print(brands.index("Nike"))
print(brands[0])
print(brands[:4])
(*shoes, platform, car) = brands
print(shoes)
print(car)
print(platform)
double = brands * 2
print(double)
new = brands + ("Microsoft", "Youtube")
print(new)
brands += ("Casio",)
print(brands)
b = list(brands)
b.append("Adidas")
brands = tuple(b)
print(brands)
b = list(brands)
b.insert(2, "Twitter")
brands = tuple(b)
print(brands)
b.remove("Ford")
brands = tuple(b)
print(brands)

#dictionary
university = {
    "name" : "Princeton",
    "place" : "New Jersey",
    "year" : 1746,
    "world_rank" : 7,
    "rector" : "Christopher Eisgruber"
}
print(university)
print(university["year"])
print(len(university))
print("year" in university)
print("place" not in university)
print(type(university))
x = university.keys()
print(x)
y = university.values()
print(y)
z = university.get("world_rank")
print(z)
university["Students"] = 8700
print(university)
university.update({"year" : 1747})
print(university)
university.pop("rector")
print(university)
university.popitem()
print(university)
del university["place"]
print(university)
university.clear()
print(university)

#sets
games = {"Roblox", "Pubg", "Clash of Clans", "Minecraft"}
print(games)
print(len(games))
print(type(games))
print("Pubg" in games)
games.add("Valorant")
print(games)
set1 = {"GTA", "Among us"}
games.update(set1)
print(games)
games.remove("Pubg")
print(games)
games.discard("Minecraft")
print(games)
x = games.pop()
print(x)
print(games)
set2 = set1.union(games)
print(set2)
set3 = games.difference(set1)
print(set3)
set3 = set1.intersection(games)
print(set3)
set3 = games.intersection(set1)
print(set3)
set3 = games.symmetric_difference(set1)
print(set3)
games.clear()
print(games)