import argparse
import sys

#parser = argparse.ArgumentParser(description = "Takes in ROC and Mirror Diameter")
#parser.add_argument("-m","--mirror_diameter", help = "Input mirror diameter in microns", required = False,default = "100")
#parser.add_argument("-r","--radius_of_curvature", help = "Input radius of curvature in microns", required = False,default = "1000")
#parser.add_argument("-s","--save",help = "1st efficiency, 2nd finesse, 3rd cross_section, 4th F/A and 5th cooperativity, y means savefig", required = False,default = "n,n,n,n,n")

def raman_range(pump=None,stokes=None):
    if pump == None and stokes == None:
        parser = argparse.ArgumentParser(description = "Takes in Stokes and Pump Ranges")
        parser.add_argument("-s","--stokes", help = "Stokes wavelengths as comma separated string", required = False,default = "761,785")
        parser.add_argument("-p","--pump", help = "Pump wavelengths as comma separated string", required = False,default = "635,638")
        argument = parser.parse_args()
        if argument.stokes:
            stokes = list(map(int,argument.stokes.split(',')))
        if argument.pump:
            pump = list(map(int,argument.pump.split(',')))
    if (len(pump) == 1) and (len(stokes) == 1):
        ramanTransition = round(((1/pump[0])-(1/stokes[0]))*10**7,1)
        print(f"Raman Line at {ramanTransition} cm^-1")
        return
    elif (len(pump) == 1) and (len(stokes) == 2):
        lowerLimit = round(((1/pump[0])-(1/stokes[0]))*10**7,1)
        upperLimit = round(((1/pump[0])-(1/stokes[1]))*10**7,1)
    elif (len(pump) == 2) and (len(stokes) == 1):
        lowerLimit = round(((1/pump[1])-(1/stokes[0]))*10**7,1)
        upperLimit = round(((1/pump[0])-(1/stokes[0]))*10**7,1)
    else:
        lowerLimit = round(((1/pump[1])-(1/stokes[0]))*10**7,1)
        upperLimit = round(((1/pump[0])-(1/stokes[1]))*10**7,1)
    if lowerLimit < 0:
        lowerLimit = 0
    print(f"Lower Limit is {lowerLimit} and Upper Limit is {upperLimit}") 
if __name__ == '__main__':
    raman_range()
    
