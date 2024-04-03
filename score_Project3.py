def count_students_above_80(avg_list):
    count = sum(avg >= 80 for avg in avg_list)
    return count

def insert(id_list, name_list, eng_list, c_list, python_list, max_students):
    num_students = min(max_students - len(id_list), int(input("삽입할 학생 수를 입력하세요: ")))
    for _ in range(num_students):
        id_list.append(input("학번: "))
        name_list.append(input("이름: "))
        eng_list.append(int(input("영어: ")))  # 입력된 점수를 정수형으로 변환하여 저장
        c_list.append(int(input("C언어: ")))    # 입력된 점수를 정수형으로 변환하여 저장
        python_list.append(int(input("파이썬: ")))  # 입력된 점수를 정수형으로 변환하여 저장
        print(" ")

def delete(id_list, name_list, eng_list, c_list, python_list, student_id):
    if student_id in id_list:
        index = id_list.index(student_id)
        id_list.pop(index)
        name_list.pop(index)
        eng_list.pop(index)
        c_list.pop(index)
        python_list.pop(index)
        print(f"학번이 {student_id}인 학생의 정보가 삭제되었습니다.")
    else:
        print(f"학번이 {student_id}인 학생이 존재하지 않습니다.")

def search_student_by_id(id_list, student_id, name_list, eng_list, c_list, python_list):
    if student_id in id_list:
        index = id_list.index(student_id)
        print_student_info(index, id_list, name_list, eng_list, c_list, python_list)
    else:
        print(f"학번 {student_id}에 해당하는 학생이 존재하지 않습니다.")

def print_student_info(index, id_list, name_list, eng_list, c_list, python_list):
    student_id = id_list[index]
    student_name = name_list[index]
    eng_score = eng_list[index]
    c_score = c_list[index]
    python_score = python_list[index]
    sum_score = eng_score + c_score + python_score
    avg_score = sum_score / 3
    grade = calculate_grade(avg_score)

    print("\n학생 정보")
    print("학번:", student_id)
    print("이름:", student_name)
    print("영어 점수:", eng_score)
    print("C언어 점수:", c_score)
    print("파이썬 점수:", python_score)
    print("총점:", sum_score)
    print("평균 점수:", "{:.2f}".format(avg_score))
    print("학점:", grade)

def calculate_grade(avg_score):
    if avg_score >= 90:
        return 'A'
    elif avg_score >= 80:
        return 'B'
    elif avg_score >= 70:
        return 'C'
    elif avg_score >= 60:
        return 'D'
    else:
        return 'F'

def sum_avg(eng_list, c_list, python_list):
    sum_list = [eng_list[i] + c_list[i] + python_list[i] for i in range(len(eng_list))]
    avg_list = [sum_list[i] / 3 for i in range(len(eng_list))]
    return sum_list, avg_list  # 결과 반환

def calculate_rank(sum_list):
    # 총점을 기준으로 등수를 계산
    sorted_indices = sorted(range(len(sum_list)), key=lambda i: sum_list[i], reverse=True)
    rank_list = [0] * len(sum_list)
    for rank, index in enumerate(sorted_indices, start=1):
        rank_list[index] = rank
    return rank_list

def count_students_above_80(avg_list):
    count = sum(avg >= 80 for avg in avg_list)
    return count

def print_result(id_list, name_list, eng_list, c_list, python_list):
    # 총점과 평균 리스트 계산
    sum_list, avg_list = sum_avg(eng_list, c_list, python_list)
    # 등수 계산
    rank_list = calculate_rank(sum_list)
    # 학점 리스트 계산
    grade_list = [calculate_grade(avg) for avg in avg_list]

    print("                             성적관리 프로그램")
    print("=========================================================================")
    print("학번     ", "이름     ", "영어    ", "C언어   ", "파이썬   ", "총점  ", "평균  ", "학점  ", "등수")
    print("=========================================================================")
    for i in range(len(id_list)):
        print(f"{id_list[i]}    {name_list[i]}     {eng_list[i]}    {c_list[i]}    {python_list[i]}    {sum_list[i]}    {avg_list[i]:.2f}    {grade_list[i]}    {rank_list[i]}")

    # 평균 80점 이상 학생 수 출력
    students_above_80 = count_students_above_80(avg_list)
    print("\n평균 80점 이상의 학생 수:", students_above_80)

# 학생 정보를 저장할 리스트들
student_id = []
student_name = []
score_eng = []
score_c = []
score_python = []
max_students = 5

# 메인 로직
while True:
    print("-----메뉴-----")
    print("1. 학생 삽입")
    print("2. 학생 검색")
    print("3. 학생 삭제")
    print("4. 전체 출력")
    print("5. 종료")

    choice = input("메뉴를 선택하세요: ")

    if choice == "1":
        insert(student_id, student_name, score_eng, score_c, score_python, max_students)
    elif choice == "2":
        student_id_to_search = input("검색할 학생의 학번을 입력하세요: ")
        search_student_by_id(student_id, student_id_to_search, student_name, score_eng, score_c, score_python)
    elif choice == "3":
        student_id_to_delete = input("삭제할 학생의 학번을 입력하세요: ")
        delete(student_id, student_name, score_eng, score_c, score_python, student_id_to_delete)
    elif choice == "4":
        if student_id:  # 학생 정보가 존재할 때만 출력
            print_result(student_id, student_name, score_eng, score_c, score_python)
        else:
            print("학생 정보가 없습니다.")
    elif choice == "5":
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 메뉴를 선택해주세요.")