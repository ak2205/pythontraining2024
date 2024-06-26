#StringSlicingExercise
a = "I_love_india"
print(a)

print(a[3:8])
print(a[5:-5])
print(a[-12:-7])
print(a[-10:12])
print(a[:6])
print(a[:-7])
print(a[5:])
print(a[-10:])
print(a[:])
print(a[4:100])
print(a[12:5])
print("-------------------------------------------------")

b = "python_compiler_interpreter"
print(b)

print(b[3:8])
print(b[5:-5])
print(b[-12:-7])
print(b[-10:12])
print(b[:6])
print(b[:-7])
print(b[5:])
print(b[-10:])
print(b[:])
print(b[4:100])
print(b[12:5])
print("-------------------------------------------------")

c = "w3schools_program_assignment"
print(c)

print(c[3:8])
print(c[5:-5])
print(c[-12:-7])
print(c[-10:12])
print(c[:6])
print(c[:-7])
print(c[5:])
print(c[-10:])
print(c[:])
print(c[4:100])
print(c[12:5])
print("-------------------------------------------------")

d = "idle_python_four"
print(d)

print(d[3:8])
print(d[5:-5])
print(d[-12:-7])
print(d[-10:12])
print(d[:6])
print(d[:-7])
print(d[5:])
print(d[-10:])
print(d[:])
print(d[4:100])
print(d[12:5])
print("-------------------------------------------------")

var = "python_interpreter_made_easy"
print(var)

print(var[1:3])
print(var[0:5])
print(var[-5:-2])
print(var[:3])
print(var[3:])
print(var[:])
print(var[3:10])
print(var[2:5])
print(var[0:10])
print(var[5:-5])
print(var[2:8])
print(var[:8])
print(var[5:])
print(var[8:12])
print(var[12:5])
print("-------------------------------------------------")

#areaExercises - Program to calculate perimeter of the circle

pi = 3.14
r = float(input("Enter a hue for radius: "))
areaCircle = 2 * pi * r
print(f"The area of circle with constant {pi} and radius {r} is {int(areaCircle)}")

#Program to calculate area of a cone

constantPi = 3.14159
radius = float(input("Enter a hue for radius: "))
height = float(input("Enter a hue for height: "))
areaCone = 0.33 * constantPi * radius * radius * height
print(f"The area of a cone with radius {radius} and height {height} is: {int(areaCone)}")  #error while using format()

print("-------------------------------------------------------------", end="/n")

#Program for string slicing Type 2 and Type 1
#String in focus: "go_kubernetes_laptop" and Type 2(String Slicing)
print("String Slicing Type 2")
h = "go_kubernetes_laptop"
print("String provided is: ", h)
print(h[3:10:1])
print(h[3:10:2])
print(h[3:10:3])
print(h[5:-5:1])
print(h[5:-5:2])
print(h[5:-5:5])
print(h[:8:4])
print(h[5::3])
print(h[::2])
print(h[12:5:3])

print("-------------------------------------------------------------", end="/n")

# Type 1(String Slicing)

print("String Slicing Type 1", end="/n")

print(h[3:8])
print(h[5:-5])
print(h[-12:-7])
print(h[-10:15])
print(h[:6])
print(h[:-7])
print(h[5:])
print(h[-10:])
print(h[:])
print(h[4:100])
print(h[12:5])

print("-------------------------------------------------------------", end="/n")

#String in focus: "stop_share_screen" and Type 2(String Slicing)

y = "stop_share_screen"
print("String Slicing Type 2")
print("String in focus is: ", y, end="/n")
print(y[3:10:1])
print(y[3:10:2])
print(y[3:10:3])
print(y[5:-5:1])
print(y[5:-5:2])
print(y[5:-5:5])
print(y[:8:4])
print(y[5::3])
print(y[::2])
print(y[12:5:3])

print("-------------------------------------------------------------", end="/n")

# Type 1(String Slicing)

print("String Slicing Type 1", end="/n")

print(y[3:8])
print(y[5:-5])
print(y[-12:-7])
print(y[-10:15])
print(y[:6])
print(y[:-7])
print(y[5:])
print(y[-10:])
print(y[:])
print(y[4:100])
print(y[12:5])



