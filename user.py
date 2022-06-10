temp = open("user_data.txt", "w")


def data_user():
    user_name = input("Name: ")
    user_size = input("Size: ")
    print(user_name + " with size " + user_size)
    write_to_user_data(user_name, user_size)


def write_to_user_data(name, size):
    # remove overwriting issue
    temp.write(name + " " + size + "\n")


data_user()
temp.close()
