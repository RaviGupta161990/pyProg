L = ['name', 'gender', 'age', 'address']
D = {'name':'sophie', 'gender': 'female', 'age' : 6, 'address': 'Hyderabad'}

for item in L:
    if item in D.keys():
        print(f'key:{item}, value:{D[item]}')
    else:
        print(f'{item} is not in list D')

empExp = {'Hema': 1, 'Manoj': 1, 'Vidya': 2, 'Jyothsna': 3, 'Ravi': 4, 'Karthik': 6, 'Yashaswini': 1.2, 'Harini': 2.1, 'Prashanth': 4.4}
empDept = { 'Hema': 'B&I', 'Manoj': 'QA', 'Vidya': 'QA', 'Jyothsna': 'QA', 'Ravi': 'DEV', 'Karthik': 'QA', 'Yashaswini': 'QA', 'Harini': 'B&I',  'Prashanth': 'QA'}


# function to print Name with 1-3 of experience.
# returns list of name with experience b/w 1-3.
def getempdataexp(dic, min, max):
    return [k for k,v in dic.items() if (v>=min) and (v<=max+1) ]


# funtion takes dictionary with name as key and department as value along with name of employee
# Returns department of employee if found other wise 'on bench' if name is not present in the dictionary
def getempdatadept(dic, name):
    return dic.get(name, "on bench")

#function print name and role of employee with given experience
def getempnamewithdept(expdic, roledic,exp):
    for k,v in expdic.items():
        if v == 1:
            print(f"{k} has 1 year experience in {roledic.get(k,'on bench')}")

def getempnamewithmoreexp(expdic, empdic, min, max, dep):
    empl = getempdataexp(expdic, min, max)
    for k in empl:
        if empdic.get(k,'on bench') == dep:
            print(f'{k} is in QA dept with exp {empExp[k]}')


def main():
    print(getempdataexp(empExp,1,3))
    print(getempdatadept(empDept,'Ravi'))
    getempnamewithdept(empExp, empDept, 3)
    getempnamewithmoreexp(empExp, empDept,2,3,'QA')

if __name__ == '__main__':
    main()