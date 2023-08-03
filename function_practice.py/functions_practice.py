def hello():
  print("hello")
hello()

def pack(argument1, argument2, argument3):
  return(argument1, argument2, argument3)

pack("h", "y", "l")

def eat_lunch(my_list):
  if len(my_list) == 0:
    print("my lunch box is empty!")
  else:
    for i in range(len(my_list)):
      if i == 0:
        print(f"first I eat {my_list[0]}")
      else:
        print(f"next I eat {my_list[i]}")

eat_lunch(["chicken", "rice", "potatoe"])