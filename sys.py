
  
 
import sys
#check if correct number of arguments a
if len(sys.argv)>5:
  print("usage")
  sys.exit(1)
#sys.argv[0] is always the program name
name=sys.argv[1]
id=sys.argv[2]
salary=sys.argv[3]
exp=sys.argv[4]

print("name of the employee", name)
print("id of the employee", id)
print("salary of the employee", salary)
print("exp of the employee", exp)
