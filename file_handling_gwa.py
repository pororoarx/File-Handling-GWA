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


# call the function