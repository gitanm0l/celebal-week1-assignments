n = int(input())
student_marks = {}
for _ in range(n):
    name, *scores = input().split()
    scores = list(map(float, scores))
    student_marks[name] = scores
query_name = input()

average = sum(student_marks[query_name]) / 3
print(f"{average:.2f}")
