# -*- coding: utf-8 -*-
subjects = ["Maths","Physics", "Geography","English","Hindi","Chemistry"]

marks = [96,81,68,79,82,98]

highest = max(marks)
lowest = min(marks)

max_index = marks.index(highest)
min_index = marks.index(lowest)
highest_subject = subjects[max_index]
lowest_subject = subjects[min_index]

print("Marks Tuple:", marks)
print("Highest Mark:", highest, "The highest subject:", highest_subject)
print("Lowest Mark:", lowest, "The lowest subject:", lowest_subject)

print("------------------------------")




