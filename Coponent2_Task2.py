# Declaring the lists that will be used in the program.
E_value = []
E2_value = []
U_value = []
U2_value = []

print("\nSwallow Speed Analysis: Version 1.0\n")
read = input("Enter the Next Reading: ")
# If statement to decide where to sort the readings entered and what message to display the user.
if any("E" in x for x in read):
    E_value.append(float(read[1:]))
    print("Reading saved.")
elif any("U" in x for x in read):
    U_value.append(float(read[1:]))
    print("Reading saved.")
elif read == '':
    print("No readings entered. Nothing to do.")
    exit()

# While loop built to execute the previous sequences of if statement till the user is done entering readings.
while read != '':
    read = input("Enter the Next Reading: ")
    if any("E" in x for x in read):
        E_value.append(float(read[1:]))
        print("Reading saved.")
    elif any("U" in x for x in read):
        U_value.append(float(read[1:]))
        print("Reading saved.")

U2_value.extend(U_value.copy())
E2_value.extend(E_value.copy())

# Converts kph(E) to mph(U).
for x in E_value:
    U2_value.append(x * 0.62)
# Converts mph(U) to kph(E).
for x in U_value:
    E2_value.append(x * 1.609)

U2_value.sort()
E2_value.sort()

# Print out the results of the entered readings.
print("\nResults Summary\n")
print(len(U2_value), "Readings Analysed.\n")
print("Max Speed:", round(U2_value[-1], 1), "MPH", round(E2_value[-1], 1), "KPH.")
print("Min Speed:", round(U2_value[0], 1), "MPH", round(E2_value[0], 1), "KPH.")
print("Avg Speed:", round(sum(U2_value) / len(U2_value), 1), "MPH", round(sum(E2_value) / len(E2_value), 1), "KPH.")
