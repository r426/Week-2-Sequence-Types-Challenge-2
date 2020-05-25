myList=[2,True,0.25,"Let\'s dance!"]
print(myList)
myList.append("Life is beautiful")
print(myList)
myList.insert(2,"What if?")
print(myList)
myList.remove(2)
print(myList)
myList.pop(2)
print(myList)
myList.pop()
print(myList)
del myList[2]
print(myList)
myList.clear()
print(myList)
myList=[2,32,0.25,25.3,4]
print(myList)
print(max(myList))
print(min(myList))
myList.sort()
print(myList)
myList.sort(reverse=True)
print(myList)

myCountries = ['Angola', 'Belgium', 'Cyprus']
myCountries.append('Denmark')
print(myCountries)
myCountries.pop(1)
print(myCountries)
myCountries.insert(1, 'Brazil')
print(myCountries)

countriesSet = {'England', 'France', 'Greece'}
print(countriesSet)
countriesSet.add('Hungary')
print(countriesSet)
countriesSet.update({'India', 'Japan'})
print(countriesSet)
countriesSet.remove('France')
print(countriesSet)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[-5:-3])
print(a[:] is a)
print(a[4::-2])
