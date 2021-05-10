# Early Lists Project - Creating Gradebook
# List for Subjects
subjects = ["Physics", "Calculus", "Poetry", "History"]

# List for Grades
grades = ["98", "97", "85", "88"]

# 2D List combining subjects & grades
gradebook = [["Physics", 98], ["Calculus", 97], ["Poetry", 85], ["History", 88]]
print(gradebook)

# appending ["computer science", 100] to gradebook
gradebook.append(["computer science", 100])
# appending ["visual arts", 93] to gradebook
gradebook.append(["visual arts", 93])

# modifying visual arts, making it 5 points greater
# minus values pull from last entry of the list and sublist (convenience)
gradebook[-1][-1] = 93 + 5

# switching out a numerical grade to pass/fail using .remove() and amending a pass
gradebook[2].remove(85)
gradebook[2].append("Pass")

# joining lists of old and new grades
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
