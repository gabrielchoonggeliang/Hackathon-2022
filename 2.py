def make_3sg_form(string):
    condition_1 = "y"
    solution_1 = "ies"
    condition_2 = tuple(["o", "ch", "s", "sh", "x", "z"])
    solution_2 = "es"
    default_solution = "s"

    if string.endswith(condition_1):
        change = string.replace(condition_1, solution_1)
    elif string.endswith(condition_2):
        change = string + solution_2
    else:
        change = string + default_solution

    print("The change is", change)


verb = input("Please enter a string\n>>>")
make_3sg_form(verb)
