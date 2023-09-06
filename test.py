import random
# hello from git

# par  num1, num2
def add(num1, num2):
  print(num1+num2)

def generateArray():
  array = []
  i = 0
  while i < 100:
    num = random.randint(0,100)
    array.append(num)
    i+=1
  print(array)

def intro():
  file = open("test.txt","a")
  file.write("Hello, hope you had a good weekend...\n\nBelow is the stock prices.\n\n")
  
'''
functions...
'''


'''
def testFunction():
  x = 6
  y = 10
  if x + y > 20:
    return True
  else:
    return False
'''
  
  

def generateDictionary():
  dictionary = {}
  i = 0
  while i < 500:
    num = random.randint(0,1000)
    dictionary[i] = num
    i+=1
  return dictionary

def body():
  '''
  Company 0: $50
  Company 1: $701
  Company 249: $204

  high, low, average...
  '''
  data = generateDictionary()
  print(data)
  file = open("test.txt","a")

  total = 0
  highest = 0
  
  for i in range(0,len(data)):
    if data[i] > highest:
      highest = data[i]
    # print("key: ",i)
    # print("value: ",data[i])
    total = total + data[i]
    file.write("    Company ")
    file.write(str(i))
    file.write(": $")
    file.write(str(data[i]))
    file.write("\n")

  average = total / len(data)
  file.write("\n    Average: $")
  file.write(str(average))
  file.write("\n    Highest: $")
  file.write(str(highest))
  

def main():
  generateDictionary()
  # print("hi from main")
  # generateArray()

  '''
  - arrays can store anything you want 
  - an index is a location of an element in that array
  - use square brackets -> []
  '''
  # for i in range(0,10):
  #   print("iteration: ",i)
  #   array.append(i)
  #   print(array)
    
  #print(array)
# arg, 10,10
  # add(10,10)

  # array = [1,2,3,4,5]
  # print(array)

  # students and grades

  
  '''
  Dictionaries...
  - curly brackets -> {}
  '''
  #key : value pair
  # array = ["Leo","B", "Jonah","B","Jeff","F"]

  # random elements that have no relation to each other
  
  # print(array)

  # each key UNIQUE key is mapped a specific value
  
  # dictionary = {
  #   "Leo":"B",
  #   "Jonah":"B",
  #   "Jeff":"F"
  # }
  
  
  

  
intro()
body()
main()
