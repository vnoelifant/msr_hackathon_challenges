#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This is a program to solver a light puzzler

import sys

def main():
   
    if (len(sys.argv) != 2):
        print("{} {}".format("USAGE:",sys.argv[0] + " " + "<Number of Lights>"))
    else:  
        # Accept command line parameter to represent number of lights
        numLights = int(sys.argv[1])
        # Set up the lights
        #numLights = 20000
        lights = range(1,numLights + 1)

        lightLimit = 10

        # Create list of lights that remain on
        onLights= []

        #Create initial light state
        lightState = [True]*numLights

    #with open('test.csv', 'w') as outFile:
        # Begin iterating over lights
        step = 2
        while step <= numLights:
            for light in lights:
                if light % step == 0:
                    lightState[light - 1] = not lightState[light - 1]
                    #outFile.write("{},{},{}\n".format(light,step,lightState[light-1]))
              
            step += 1
      
        # print to show which lights are on
        for light in lights:
            if lightState[light - 1] == True:
                 onLights.append(light)
            if light == lightLimit:
                break
        print('The following lights from light 1 to light number',lightLimit,'are on:',','.join(map(str, onLights)))

#main()
if __name__ == '__main__': 
    main()
        
       




