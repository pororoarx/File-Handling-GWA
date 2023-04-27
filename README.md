FILE HANDLING GWA

A python program that read a file containing the name of 20 students together with their GWA. The program will output the name of the student who got the highest GWA (including the GWA).

=============================================================================================================

Table of Contents

•	Installation

•	Usage

•	Contributing

•	Conclusion

=============================================================================================================

•	Installation
1.	Clone the repository to your local machine: ‘git clone ‘git@github.com:pororoarx/File-Handling-GWA.git’
2.	Install the required ‘pyfiglet’ module: ‘pip install pyfiglet’
3.	Save the student records in a text file named 'students_gwa.txt' in the project directory.

•	Usage
1.	Open Git Bash and go to the project directory.
2.	Run the program: ‘file_handling_gwa.py’
3.	The program will output the name of the student who got the highest GWA along with their GWA.


•	Formulation:
The program stores each student's name and their corresponding GWA in a dictionary from the 'students_gwa.txt' file. Then, it finds the name of the student with the highest GWA by using the min() function to get the key with the lowest value in the dictionary. Finally, it prints the name of the student with the highest GWA and their GWA to the console.


•	Conclusion:
The program demonstrates how to read and process data from a text file in Python using file handling techniques. This README.md file provides clear instructions for installing and running the program, so feel free to contribute to its development.
