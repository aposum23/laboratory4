import math


osn_one = int(input('Osnovanie 1:'))
osn_two = int(input('Osnovanie 2: '))
angle = int(input('Ugol: '))

print('Ploshad: ' + str(osn_one * osn_two * math.sin(angle)))
