coordinates = [(4, 5), (2, 4), (3, 7)]
# tuple is immutable, cant be changed after registered
# tuple is similar to list but different a bit used for data that wouldnt be changed
coordinates[0] = (3, 2)

print(coordinates[0])