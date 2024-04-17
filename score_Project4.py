class StudentManager:
    def __init__(self, max_students=5):
        self.student_id = []
        self.student_name = []
        self.score_eng = []
        self.score_c = []
        self.score_python = []
        self.max_students = max_students

    def insert(self):
        num_students = min(self.max_students - len(self.student_id), int(input("삽입할 학생 수를 입력하세요: ")))
        for _ in range(num_students):
            self.student_id.append(input("학번: "))
            self.student_name.append(input("이름: "))
            self.score_eng.append(int(input("영어: ")))
            self.score_c.append(int(input("C언어: ")))
            self.score_python.append(int(input("파이썬: ")))
            print(" ")

    def delete(self, student_id):
        if student_id in self.student_id:
            index = self.student_id.index(student_id)
            self.student_id.pop(index)
            self.student_name.pop(index)
            self.score_eng.pop(index)
            self.score_c.pop(index)
            self.score_python.pop(index)
            print(f"학번이 {student_id}인 학생의 정보가 삭제되었습니다.")
        else:
            print(f"학번이 {student_id}인 학생이 존재하지 않습니다.")

    def search_student_by_id(self, student_id):
        if student_id in self.student_id:
            index = self.student_id.index(student_id)
            self.print_student_info(index)
        else:
            print(f"학번 {student_id}에 해당하는 학생이 존재하지 않습니다.")

    def print_student_info(self, index):
        student_info = {
            '학번': self.student_id[index],
            '이름': self.student_name[index],
            '영어 점수': self.score_eng[index],
            'C언어 점수': self.score_c[index],
            '파이썬 점수': self.score_python[index],
            '총점': self.score_eng[index] + self.score_c[index] + self.score_python[index],
            '평균 점수': (self.score_eng[index] + self.score_c[index] + self.score_python[index]) / 3
        }
        student_info['학점'] = self.calculate_grade(student_info['평균 점수'])

        print("\n학생 정보")
        for key, value in student_info.items():
            if key in ['총점', '평균 점수']:
                print(f"{key}: {value:.2f}")
            else:
                print(f"{key}: {value}")

    def calculate_grade(self, avg_score):
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

    def sum_avg(self):
        sum_list = [self.score_eng[i] + self.score_c[i] + self.score_python[i] for i in range(len(self.score_eng))]
        avg_list = [sum_list[i] / 3 for i in range(len(self.score_eng))]
        return sum_list, avg_list

    def calculate_rank(self, sum_list):
        sorted_indices = sorted(range(len(sum_list)), key=lambda i: sum_list[i], reverse=True)
        rank_list = [0] * len(sum_list)
        for rank, index in enumerate(sorted_indices, start=1):
            rank_list[index] = rank
        return rank_list

    def count_students_above_80(self, avg_list):
        return sum(avg >= 80 for avg in avg_list)

    def print_result(self):
        if self.student_id:
            sum_list, avg_list = self.sum_avg()
            rank_list = self.calculate_rank(sum_list)
            grade_list = [self.calculate_grade(avg) for avg in avg_list]

            print("                             성적관리 프로그램")
            print("=========================================================================")
            print("학번     ", "이름     ", "영어    ", "C언어   ", "파이썬   ", "총점  ", "평균  ", "학점  ", "등수")
            print("=========================================================================")
            for i in range(len(self.student_id)):
                print(f"{self.student_id[i]}    {self.student_name[i]}     {self.score_eng[i]}    {self.score_c[i]}    {self.score_python[i]}    {sum_list[i]}    {avg_list[i]:.2f}    {grade_list[i]}    {rank_list[i]}")

            students_above_80 = self.count_students_above_80(avg_list)
            print("\n평균 80점 이상의 학생 수:", students_above_80)
        else:
            print("학생 정보가 없습니다.")

# 메인 실행 부분
manager = StudentManager()

while True:
    print("-----메뉴-----")
    print("1. 학생 삽입")
    print("2. 학생 검색")
    print("3. 학생 삭제")
    print("4. 전체 출력")
    print("5. 종료")

    choice = input("메뉴를 선택하세요: ")

    if choice == "1":
        manager.insert()
    elif choice == "2":
        student_id_to_search = input("검색할 학생의 학번을 입력하세요: ")
        manager.search_student_by_id(student_id_to_search)
    elif choice == "3":
        student_id_to_delete = input("삭제할 학생의 학번을 입력하세요: ")
        manager.delete(student_id_to_delete)
    elif choice == "4":
        manager.print_result()
    elif choice == "5":
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 메뉴를 선택해주세요.")