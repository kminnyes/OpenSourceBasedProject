def insert(id_list, name_list, eng_list, c_list, python_list):
    for _ in range(5):
        id_list.append(input("학번: "))
        name_list.append(input("이름: "))
        eng_list.append(int(input("영어: ")))  # 입력된 점수를 정수형으로 변환하여 저장
        c_list.append(int(input("C언어: ")))    # 입력된 점수를 정수형으로 변환하여 저장
        python_list.append(int(input("파이썬: ")))  # 입력된 점수를 정수형으로 변환하여 저장
        print(" ")


def sum_avg(eng_list, c_list, python_list):
    sum_list = [eng_list[i] + c_list[i] + python_list[i] for i in range(5)]
    avg_list = [sum_list[i] / 3 for i in range(5)]
    return sum_list, avg_list  # 결과 반환


def calculator_grade(avg_list):
    grade_list = []
    for avg in avg_list:
        if avg >= 90:
            grade_list.append('A')
        elif avg >= 80:
            grade_list.append('B')
        elif avg >= 70:
            grade_list.append('C')
        elif avg >= 60:
            grade_list.append('D')
        else:
            grade_list.append('F')
    return grade_list  # 결과 반환


def sort(rate_list):
    sorted_rate = sorted(rate_list, reverse=True)
    rank_dict = {}
    for idx, rate in enumerate(sorted_rate):
        if rate not in rank_dict:
            rank_dict[rate] = idx + 1
    return [rank_dict[rate] for rate in rate_list]  # 결과 반환


def print_result(id_list, name_list, eng_list, c_list, python_list, sum_list, avg_list, grade_list, rate_list):
    print("                             성적관리 프로그램")
    print("=========================================================================")
    print("학번     ", "이름     ", "영어    ", "C언어   ", "파이썬   ", "총점  ", "평균  ", "학점  ", "등수")
    print("=========================================================================")
    for i in range(5):
        print(id_list[i], "    ", name_list[i], "     ", eng_list[i], "    ", c_list[i], "    ", python_list[i], "    ", sum_list[i], "    ", avg_list[i], "    ", grade_list[i], "    ", rate_list[i])


student_id = []
student_name = []
score_c = []
score_eng = []
score_python = []

insert(student_id, student_name, score_eng, score_c, score_python)
sum_score, avg_score = sum_avg(score_eng, score_c, score_python)
grade_score = calculator_grade(avg_score)
rate_score = sort(avg_score)
print_result(student_id, student_name, score_eng, score_c, score_python, sum_score, avg_score, grade_score, rate_score)