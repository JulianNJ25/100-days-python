student_scores = [180, 124, 165, 173, 189, 169, 146]

prev = 0
for score in student_scores:
    if score > prev:
        max =  score
    prev = score

print(max)