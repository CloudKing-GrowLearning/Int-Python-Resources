#So here im going to introduce the concept of needing a function by working out a number squared plus eight

x = 16
squared_x = x * x
squared_x_plus_eight = squared_x + 8

#Or I could rewrite as follows

x = 16
squared_x_plus_eight = (x * x) + 8

#However this could be a pain to do again and again so could we do it more simply as a function

def squared_plus_eight(x):
    """
    :param x: This needs to be a float or integer
    :return: A float or integer
    """
    res = x * x
    res += 8
    return res

#This will all be done in the terminal and so ill then create the same again in a script and have something like below
#Ill then show how we can run this in pycharm and then via the terminal using python name_of_script.py

def squared_plus_eight(x):
    """
    :param x: This needs to be a float or integer
    :return: A float or integer
    """
    res = x * x
    res += 8
    return res


res = squared_plus_eight(24)
print(res)

#We could also do the same thing as a lambda function as shown below?

squared_plus_eight = lambda x: (x * x) + 8

print(squared_plus_eight(8.4))
