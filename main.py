# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
def random_instance(serverLength, userLength):
    randUsers = np.random.uniform(low=0, high=1, size=(userLength,))
    randServers = np.random.uniform(low=0, high=1, size=(serverLength,))
    # Use a breakpoint in the code line below to debug your script.
    return randUsers, randServers
def greedy(randUsers, randServers):
    greedyDist = 0.0
    totalDist = [9999] * len(randUsers)
    removeVar = 0
    usersList = randUsers.tolist()
    serversList = randServers.tolist()
    for i in range(len(usersList)):
        for j in range(len(serversList)):
            if(abs(usersList[i]-serversList[j])<totalDist[i]):
                    totalDist[i] = abs(usersList[i] - serversList[j])
                    removeUser = i
                    removeVar = j #Using removevar to be the last one until i increments
        #print(serversList[removeVar])
        serversList.remove(serversList[removeVar])
        #print(usersList)
        #print(totalDist[i])
        #print(totalDist[i])
        #print(serversList)
    for i in range(len(totalDist)):
        greedyDist += totalDist[i]
    return greedyDist
    #Matching using the greedy algorithm based on array incremental points
    #match the algo
def opt (randUsers, randServers):
    optDist = 0.0
    i = 0
    usersList = randUsers.tolist()
    serversList = randServers.tolist()

    for i in range(len(usersList)):
        minUser = min(usersList)
        #print("This is min user: " + str(minUser))
        minServer = min(serversList)
        #print("This is minServer: " + str(minServer))
        optDist += abs(minServer - minUser)
        usersList.remove(minUser)
        serversList.remove(minServer)
        #print(usersList)
        #print(optDist)
        #print(serversList)
    return optDist
    #Based on what we know matching looking throughout the entire array
def evaluate(greedyDist, optDist):
    return greedyDist/optDist
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = random_instance(10, 10)
    print('Debugging random_instance')
    users = result[0]
    print('Debugging return [0]')
    print(users)
    servers = result[1]
    print('Debugging return [1]')
    print(servers)
    greedy_dist = greedy(users, servers)
    print('Debugging greedy_dist ' + str(greedy_dist))
    opt_dist = opt(users, servers)
    print('Debugging opt_dist ' + str(opt_dist))
    print(evaluate(greedy_dist, opt_dist))
    totalSum = 0
    trials = 100
    for i in range(trials):
        result = random_instance(10, 10)
        users = result[0]
        servers = result[1]
        greedy_dist = greedy(users, servers)
        opt_dist = opt(users, servers)
        totalSum += evaluate(greedy_dist, opt_dist)
    print(totalSum/(trials))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
