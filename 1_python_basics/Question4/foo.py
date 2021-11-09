import check50 # import the check50 module
import check50.py
import re

def sep_num(num):
    # regex that matches `num` not surrounded by any other numbers
    # (so coins(2) won't match e.g. 123)
    return fr"(?<!\d){num}(?!\d)"

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Question4.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases(exists):
    """Program prints correct number of points for organizer """
    check50.include("Question4_Sol.py")
    check50.py.append_code("Question4.py", "Question4_Sol.py")
    
    actual = check50.run("python3 Question4.py").stdout()
    expected1 = "25\n"
    expected2 = "5\n"
    expected3 = "55\n"
    expected4 = "35\n"
    
    if not re.search(sep_num(25), actual):
        help = r"Your code does not print the correct result for 'Johannes'."
        raise check50.Mismatch(expected1, actual, help=help)
    if not re.search(sep_num(5), actual):
        help = r"Your code does not work for 'John'.  Your code is being checked against several different cases."
        raise check50.Mismatch(expected2, actual, help=help)
    if not re.search(sep_num(55), actual):
        help = r"Your code does not work for other dictionaries.  Your code is being checked against several different dictionaries."
        raise check50.Mismatch(expected3, actual, help=help)
    if not re.search(sep_num(35), actual):
        help = r"Your code does not work for other dictionaries.  Your code is being checked against several different dictionaries."
        raise check50.Mismatch(expected4, actual, help=help)