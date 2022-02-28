import a_PlantClass as pc

primrose = pc.Plant("Green")

sunflower = pc.Flower("Yellow",12)

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())

#Doesn't work bc primrose is supperclass and its trying to use a subclass
#print(primrose.get_petals())
