
value = []
nvalue = []

print("Swallow Speed Analysis: Version 1.0\n")
read = input("Enter the Next Reading: ")
value.append(read)
print("Reading saved.")

while read != '':
    read = input("Enter the Next Reading: ")
    print("Reading saved.")
    mph = [x for x in value if x == 'e']
    print(mph)