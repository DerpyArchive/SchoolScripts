#Import stuff. It is built into Python so installation of it via pip is not needed
import time

#Data
name = "Bob"
age = "99"
favfood = "cheese"


#Stuff to print to console
print ("My name is " + name)
time.sleep(2.5)	#This is used so the computer waits
print ("I am " + age + " years old and am nearly 100!")
time.sleep(2.5)
print ("My favourite food is " + favfood)	
time.sleep(2.5)
print ("The time will appear below in 2.5 seconds")
time.sleep(2.5)
print (time.strftime("%I:%M:%S")) #Experimental Code using the time module.
time.sleep(2.5)
print ("The program will close in 5 seconds")
time.sleep(1)
print ("5")
time.sleep(1)
print ("4")
time.sleep(1)
print ("3")
time.sleep(1)
print ("2")
time.sleep(1)
print ("1")
print ("BOOM!")
