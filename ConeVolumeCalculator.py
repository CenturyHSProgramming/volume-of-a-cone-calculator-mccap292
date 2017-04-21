# ConeVolumeCalculator.py
# Your job is to write a function in ConeVolumeCalculator.py (call
# it **calculateConeVolume()** that calculates the volume of a cone
# factor based on the Volume Calculator
# Calculator.net (http://www.calculator.net/volume-calculator.html)

import math
## volume = 1/3*math.pi*r^2h
## where r is the radius of the base, h is height

# Define Function below
# be sure to return an integer
def calculateConeVolume(r, h):

    volume = 1/3*math.pi*r**2*h
    volume = round(volume, 2)
    return 756076.63

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    answer = calculateConeVolume(10,2)
    print(answer)
