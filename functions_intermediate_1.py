#Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#1
x[1][0] = 15
print(x)
print("              ")
#2
students[0]['last_name'] = "Bryant"
print(students)
print("              ")
#3
sports_directory['soccer'][0] = "Andres"
print(sports_directory)
print("              ")
#4
z[0]['y']=30
print(z)

print("-----------------------")

#Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(par):
    for x in range(len(par)):
        first = par[x]['first_name']
        last = par[x]['last_name']
        key = list(par[x].keys())
        print(key[0] + " - " + first + ", "  + key[1] + " - "  + last)

iterateDictionary(students)

print("-----------------------")

#Get Values From a List of Dictionaries
def iterateDictionary2(key, list):
    if key == 'first_name':
        for x in range(len(list)):
            first = list[x]['first_name']
            print(first)
        print("              ")
    elif key == 'last_name':
        for x in range(len(list)):
            last = list[x]['last_name']
            print(last)

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

print("-----------------------")

#Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(par):
    key = list(par.keys())
    countOne = len(par['locations'])
    countTwo = len(par['instructors'])
    print(str(countOne) + " " + key[0].upper())
    for x in range(countOne):
        print(par['locations'][x])
    print("              ")
    print(str(countTwo) + " " + key[1].upper())
    for x in range(countTwo):
        print(par['instructors'][x])

printInfo(dojo)