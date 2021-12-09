from imports import *

def RandomMatch(n):
    """
    This function would assign a random preferance set for a person
    """

    # setting random seed
    random.seed(datetime.now())

    dict = {}

    # creating a random dict of preferance
    for i in range(n):
        temp = random.randint(1,n)

        if temp in dict:
            dict[temp].append(i)

        else:
            dict[temp] = [i]

    # converting the dict to LinkedList
    flag = True
    for i in sorted(dict.keys()):

        # assigning the first element as the start of linked list
        if flag:
            flag = False
            lis = LinkedList(dict[i])

        # adding element in linked list
        else:
            lis.add(dict[i])

    return lis
