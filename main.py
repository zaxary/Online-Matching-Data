# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
global randomServer
global randUser
global greedyDist
global optDist
def random_instance(serverLength, userLength):
    randServer = np.random.uniform(low=0, high=1, size=(serverLength,))
    randUser = np.random.uniform(low=0, high=1, size=(userLength,))
    # Use a breakpoint in the code line below to debug your script.
def greedy():
    greedyDist = 0.0
    totalDist = [9999] * len(randUser)
    for i in range(len(randUser)): #Shorter of the distances
        for j in range(len(randUser)):
            if(randomServer[i]-randUser[j]<totalDist[i] or ((randomServer[i] - randUser[j]) * -1 < totalDist[i]) ):
                if(randomServer[i] - randUser[j] < 0):
                    randUser.remove(randUser[j])
                    totalDist[i] = (randomServer[i] - randUser[j]) * -1
                else:
                    randUser.remove(randUser[j])
                    totalDist[i] = (randomServer[i] - randUser[j])
    for i in range(len(totalDist)):
        greedyDist += totalDist[i]
    #Matching using the greedy algorithm based on array incremental points
    #match the algo
def opt ():
    optDist = 0.0
    minUser = 0.0
    minServer = 0.0
    i = 0
    while(i in range(len(randUser))):
        minUser = min(randUser)
        minServer = min(randomServer)
        if(minServer - minUser < 0):
            optDist += (minServer - minUser)*-1
        else:
            optDist += (minServer - minUser)
        randUser.remove(min(randUser))
        randomServer.remove(min(randomServer))
        i += 1
    #Based on what we know matching looking throughout the entire array
def evaluate():
    return greedyDist - optDist
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Debugging')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
