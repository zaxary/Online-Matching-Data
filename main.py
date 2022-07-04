# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

import numpy as np
import matplotlib.pyplot as plt

def random_instance(serverLength, userLength):
    randUsers = np.random.uniform(low=0, high=1, size=(userLength,))
    randServers = np.random.uniform(low=0, high=1, size=(serverLength,))
    # Use a breakpoint in the code line below to debug your script.
    return randUsers, randServers
def two_dimensional_random(serverLength, userLength):
    twoDimensionUsers_x = np.random.randint(0, 10, userLength)
    twoDimensionUsers_y = np.random.randint(0, 10, userLength)
    twoDimensionServers_x = np.random.randint(0, 10, serverLength)
    twoDimensionServers_y = np.random.randint(0, 10, serverLength)
    twoDimensionServers_x = (twoDimensionServers_x/10.0)
    twoDimensionServers_y = (twoDimensionServers_y / 10.0)
    twoDimensionUsers_x = (twoDimensionUsers_x / 10.0)
    twoDimensionUsers_y = (twoDimensionUsers_y / 10.0)
    plt.scatter(twoDimensionUsers_x, twoDimensionUsers_y)
    plt.show()
    plt.scatter(twoDimensionServers_x, twoDimensionServers_y)
    plt.show()
    return twoDimensionUsers_x, twoDimensionUsers_y, twoDimensionServers_x, twoDimensionServers_y

def two_dimensional_greedy(users_x, users_y, servers_x, servers_y):
    totalDist = [9999] * len(users_x)
    removeVar = 0
    greedyDist = 0.0
    servers_x_list = servers_x.tolist()
    servers_y_list = servers_y.tolist()
    users_x_list = users_x.tolist()
    users_y_list = users_y.tolist()
    for i in range(len(users_x)):
        for j in range(len(servers_x_list)):
            distUsers = math.sqrt( ((users_x_list[i]-servers_x_list[j])**2)+((users_y_list[i]-servers_y_list[j])**2) )
            if (abs(distUsers) < totalDist[i]):
                totalDist[i] = abs(distUsers)
                removeVar = j  # Using removevar to be the last one until i increments
        # print(serversList[removeVar])
        servers_x_list.remove(servers_x_list[removeVar])
        servers_y_list.remove(servers_y_list[removeVar])
        # print(usersList)
        # print(totalDist[i])
        # print(totalDist[i])
        # print(serversList)
    for i in range(len(totalDist)):
        greedyDist += totalDist[i]
    return greedyDist
    # Matching using the greedy algorithm based on array incremental points
    # match the algo

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
def two_dimensional_opt (users_x, users_y, servers_x, servers_y):
    totalDist = [9999] * len(users_x)
    removeVar = 0
    optDist = 0.0
    servers_x_list = servers_x.tolist()
    servers_y_list = servers_y.tolist()
    users_x_list = users_x.tolist()
    users_y_list = users_y.tolist()

    for i in range(len(users_x_list)):
        minUser_x = min(users_x_list)
        minUser_y = min(users_y_list)
        minServer_x = min(servers_x_list)
        minServer_y = min(servers_y_list)
        # print("This is min user: " + str(minUser))
        # print("This is minServer: " + str(minServer))
        optDist += abs(math.sqrt(((minUser_x - minServer_x) ** 2) + ((minUser_y - minServer_y) ** 2)))
        users_x_list.remove(minUser_x)
        users_y_list.remove(minUser_y)
        servers_x_list.remove(minServer_x)
        servers_y_list.remove(minServer_y)
        # print(usersList)
        # print(optDist)
        # print(serversList)
    return optDist
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
    print('Here is the ratio in one dimension: ' + str(evaluate(greedy_dist, opt_dist)))
    totalSum = 0
    trials = 100
    for i in range(trials):
        result = random_instance(10, 10)
        users = result[0]
        servers = result[1]
        greedy_dist = greedy(users, servers)
        opt_dist = opt(users, servers)
        totalSum += evaluate(greedy_dist, opt_dist)
    print('Here is the ratio in one dimension: ' + str(totalSum/(trials)) + ' for ' + str(trials) + ' trials')
    two_dimensional_result = two_dimensional_random(10, 10)
    users_x = two_dimensional_result[0]
    users_y = two_dimensional_result[1]
    servers_x = two_dimensional_result[2]
    servers_y = two_dimensional_result[3]
    greedy_two_dist = two_dimensional_greedy(users_x, users_y, servers_x, servers_y)
    print('Debugging greedy_dist in two dimensions ' + str(greedy_two_dist))
    opt_two_dist = two_dimensional_opt(users_x, users_y, servers_x, servers_y)
    print('Debugging opt_dist in two dimensions ' + str(opt_two_dist))
    print('Here is the ratio in two dimension: ' + str(evaluate(greedy_two_dist, opt_two_dist)))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
