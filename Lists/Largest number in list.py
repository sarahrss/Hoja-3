import random
randomlist = random.sample(range(1, 1000), 100)
print(randomlist)

Max = randomlist[0]
Min = randomlist[0]
for i in range (len(randomlist)):
  if (randomlist[i]> Max):
    Max = randomlist[i]
  elif (randomlist[i]<Min):
    Min = randomlist[i]
print("El valor máximo de la lista es: " +str(Max)) 
print ("El valor minimo de la lista es: " +str(Min))