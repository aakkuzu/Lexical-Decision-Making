import time



with open('Words', 'r') as Words:
  for line in Words:
    time.sleep(0.5)
    print(line)
    if(line == '\n'):
      print(line)
      time.sleep(2)
