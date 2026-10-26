for i in range(5):
    print(i)

scores = [70, 85, 60, 90, 45]

for score in scores:
    print("score",score)

count = 1
while count <= 5:
    print(count)
    count +=2

scores = [70, 85, 60, 90, 45]

total = 0

for score in scores:
    total  += score

average = total / len(scores)

print("total:", total)
print("Average:", average)



def greet_student(name):
     print(f"Hello, {name}!")

greet_student("Aung Aung")
greet_student("Su Su")


def calculate_total(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

scores = [70, 80, 90]
result = calculate_total(scores)
print(result)



def calculate_total(scorces):
   return sum(scores)
print(calculate_total([80,70,90]))

def calculate_average(scorces):
   return sum(scores) / len(scores)
print(calculate_average([80,70,90]))

def calculate_grade(scorces):
    if score < 0 or score > 100:
      return "Invalid"
    elif score >= 80:
     return "Excellent"
    elif score >= 60:
     return "Good"
    elif score >= 40:
     return "Pass"
    else:
     return "Fail"

print(calculate_grade([80,70,90]))

def calculate_count(scorces):
   count = 0
   for scorce in scorces:
      if score >= 40:
         count +=1
         return count
print(calculate_count([80,70,90]))

scores = [55, 80, 35, 90,65]
scores.append(75)
print(scores)

scores[1] = 85
print(scores)


print( max(scores))
print(min(scores))

print(sum(scores)/len(scores))

for scorce in scores:
   if (scorce >= 80):
      print(scorce)

student = {
"name": "Su Su",
"age": 20,
"score": 88,
"passed": True
}

print(student["name"])
print(student["score"])

students = [
    {"name": "Aung Aung", "score": 85},
    {"name": "Su Su", "score": 92},
    {"name": "Mg Mg", "score": 35}
]

for student in students:
    print(student["name"], student["score"])