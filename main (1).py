nums = list()
while True :
  inp = input("Enter a number/done: ")
  if inp == "done" : break
  value = float(inp)
  nums.append(value)
  
choices = ["length", "biggest", "smallest", "sum", "average"]
choice = input(f"{choices} \n choise: ").rstrip()

if choice == "length" :
  print(len(nums))
if choice == "biggest" :
  print(max(nums))
if choice == "smallest" :
  print(min(nums))
if choice == "sum" :
  print(sum(nums))
if choice == "average" :
  print(sum(nums)/len(nums))
  