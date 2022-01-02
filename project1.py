#getting area of circle by taking input from user
R= input ("Enter Radius of Circle : ")
float(R)
area = float(3.14) *(float(R)*float(R))
float(area)
print("The area of circle with radius " +R+" is")
print(area)
# by taking input from user extension of file name
file_name = input("Input the filename:")
file_extension = file_name.split(".")
print("The extention of the file is : " + repr(file_extension[1]))
