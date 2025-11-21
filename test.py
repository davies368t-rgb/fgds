test = {'t1':'cool','t2':'kool','t3':'sool','t4':'mool','t5':'cool','t6':'rool'}
test1= {}

for key,value in test.items():
    if value not in test1.values():
        test1[key]=value
print(test1)