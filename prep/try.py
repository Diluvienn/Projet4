def bypass_function(func):

    def wrapper():

        print("Your function did not run!")


    return wrapper



def say_aaa():

    print("aaa")



bypass_function(say_aaa)()