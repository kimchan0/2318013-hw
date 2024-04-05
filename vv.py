score = input("성적을 입력하세요: ")
hum_score = int(score)

if 71 <= hum_score <= 100:
    grade = "A"
elif 41 <= hum_score <= 70:
    grade = "B"
elif 11 <= hum_score <= 40:
    grade = "C"
else :
    grade = "D"
print("당신의 학점은 "+ grade)