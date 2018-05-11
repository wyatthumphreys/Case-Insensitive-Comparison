def casecompare(string):
    comp="Hello"
    comp=comp.lower()
    string=string.lower()
    if(string == comp):
        return(True)
    else:
        return(False)

try:
    print(casecompare("hEllo"))
    print(casecompare("Anything Else"))
except NameError as e:
    print(e)
except ValueError as e:
    print(e)