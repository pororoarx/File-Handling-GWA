# A Python program that read a file containing the name of 20 students together with their GWA. The program will outputs the name of the student who got the highest GWA (including the GWA).

# import pyfiglet
import pyfiglet

# Set and print the title of the activity in color and different font
title_of_assign = "Module 2 - Prob 1"
font = "slant"
print("\033[38;5;93m", pyfiglet.figlet_format(title_of_assign, font=font))

# Start

# define a function called students_gwa_reader
def student_gwa_reader():
    # open students_gwa.txt (read)
    with open("students_gwa.txt", "r") as file_1:
        # create empty dictionary
        student_gwa = {}
        # loop through each line in students_gwa.txt
        for line in file_1:
            # split the line into name and gwa and convert gwa to float
            name, gwa = line.strip().split(",")
            student_gwa[name] = float(gwa)
        # find the key with the lowest value (lowest value = highest gwa) in student_gwa dictionary
        highest_gwa_name = min(student_gwa, key=student_gwa.get)
        # get the key with the lowest value in student_gwa dictionary
        highest_gwa = student_gwa[highest_gwa_name]
    # print the result
    print("\033[38;5;27mStudent with highest GWA: " + highest_gwa_name)
    print("GWA: " + str(highest_gwa) + "\033[0m")


# call the function
student_gwa_reader()