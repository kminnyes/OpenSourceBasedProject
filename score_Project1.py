def sort(score, subject):
    a = score
    sorted_score = sorted(a, reverse=True)

    for k in range(len(score)):
        print("과목: ", subject, ", ", k+1, "등 : ", sorted_score[k], "점")
    print(" ")


student_name = []
score_eng = []
score_C = []
score_python = []
scoreList = []

subject = ["영어", "C언어", "파이썬"]

for i in range(5):
        student_name.append(input("학생의 이름을 입력하세요:"))

        for j in subject:
            print(student_name[i], "학생의", j, "성적을 입력하세요:")
            temp = int(input())
            if j == "영어":
                (score_eng.append(temp))
            elif j == "C언어":
                score_C.append(temp)
            else:
                score_python.append(temp)
        print(" ")

sum =0
k = 0
for i in student_name:
    print(i, "학생의 영어 점수 : ", score_eng[k])
    print(i, "학생의 C언어 점수 : ", score_C[k])
    print(i, "학생의 파이썬 점수 : ", score_python[k])

    sum = score_eng[k] + score_C[k] + score_python[k]
    avg = sum / 3
    print(i, "학생의 총점 : ", sum)
    print(i, "학생의 평균 :", avg)
    scoreList.append(avg)


    if avg >= 90:
        print("A학점 입니다.")
    elif avg >= 80:
        print("B학점 입니다.")
    elif avg >= 70:
        print("C학점 입니다.")
    elif avg >= 60:
        print("D학점 입니다.")
    else:
        print("F학점 입니다.")
    print(" ")
    k += 1

sort(score_eng, "영어")
sort(score_C, "C언어")
sort(score_python, "파이썬")