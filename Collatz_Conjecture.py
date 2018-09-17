# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import time
startTime = time.time()

results = []
def main():
    
    maxChainLength = 0
    numMaxChainLength = 0
    x = 1
    numUpTo = 1000001

    while(x < numUpTo):
        currentNum = x
        chainLength = 1
        # Peform operation on current number up until number 1 (sequence terminates at 1)
        while(currentNum != 1):
            #reassign result to new current number
            currentNum = collatz(currentNum)
            #print(currentNum)
            chainLength += 1
       
        if chainLength > maxChainLength:
            maxChainLength = chainLength
            numMaxChainLength = x
        # Print status of each integer
        if x % 1000 == 0:
            print('Integer {}: Sequence length: {}'.format(x,chainLength))
            sys.stdout.write("\033[F") # Cursor up one line
            time.sleep(1)
        #chainLength = 1
        x += 1
    #print(maxChainLength, numMaxChainLength)
    endTime = time.time()
    totalTime = endTime - startTime
    print('The longest chain has length {}, the number that produced this chain was {}, and this took {} seconds to find'.format(maxChainLength, numMaxChainLength,totalTime))
    
    
def collatz(n):
    n = n // 2 if n % 2 == 0 else 3*n + 1
    #print(n)
    return(n)
    
#if __name__ == '__main__': 
#main()
