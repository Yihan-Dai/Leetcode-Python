
cities={'CA': 'San Francisco', 'MI':'Detroit', 'FL':'Jacksonville'}
cities['NY']='New York'
cities['OR']='Portland'



list=[1,2,3,4]
print len(list)
list_cities=cities.items()

print list_cities
for i in range(0,5):
    print "State? (ENTER to quit)",
    state=raw_input(">")
    if not state:break
    Trigger=False
    for j in list_cities:
        if state==j[0]:
            Trigger=True
            print j[1]
        else:
            continue
    if Trigger==False:
        print "NOT FOUND"

    