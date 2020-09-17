
# Author: Cui Qiaoxu qfc5036@psu.edu
# Collaborator: John O'Toole Jbo5232@psu.edu
# Collaborator: Ching-Ju Chen cxc6001@psu.edu
# Section: 8
# Breakout: 11
def sum_n(n):
  if n==0:
    return n
  else:
    return n+sum_n(n-1)

def print_n(s,n):
  if n==0:
    return n
  else:
   print(s) 
   print_n(s,n-1)
def run():
  n = input ("Enter an int: ")
  n = int(n)
  n1 = sum_n(n)
  print(f"sum is {n1}.")

  s = input("Enter a string: ")
  s = str(s)
  s = print_n(s,n)

if __name__=="__main__":
    run()