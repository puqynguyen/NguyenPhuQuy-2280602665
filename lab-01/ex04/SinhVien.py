class Student:
    __counter = 0

    def __init__(self, name, gender, major, averageScore):
        Student.__counter += 1
        self.id = Student.__counter
        self.name = name
        self.gender = gender
        self.major = major
        self.averageScore = averageScore
        
        if self.averageScore > 8:
            self.rank = "Gioi"
        elif self.averageScore > 6.5:
            self.rank = "Kha"
        elif self.averageScore > 5:
            self.rank = "Trung binh"
        else:
            self.rank = "Yeu"

class StudentList:
    def __init__(self):
        self.students = []
    
    def addStudent(self, student):
        self.students.append(student)
    
    def updateStudent(self, id, name, gender, major, averageScore):
        for student in self.students:
            if student.id == id:
                student.name = name
                student.gender = gender
                student.major = major
                student.averageScore = averageScore
                if student.averageScore > 8:
                    student.rank = "Gioi"
                elif student.averageScore > 6.5:
                    student.rank = "Kha"
                elif student.averageScore > 5:
                    student.rank = "Trung binh"
                else:
                    student.rank = "Yeu"
                break
    
    def deleteStudent(self, id):
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                break
            
    def searchStudent(self, name):
        result = []
        for student in self.students:
            if name.lower() in student.name.lower():
                result.append(student)
        return result
    
    def sortByAverageScore(self):
        if not self.students:
            print("Danh sách sinh viên rỗng.")
            return
        self.students.sort(key=lambda x: x.averageScore)
        
    def sortByMajor(self):
        if not self.students:
            print("Danh sách sinh viên rỗng.")
            return
        self.students.sort(key=lambda x: x.major.lower() if isinstance(x.major, str) else "")
        
    def displayStudents(self):
        if not self.students:
            print("Danh sách sinh viên rỗng.")
            return
        print(f"{'ID'.ljust(5)}{'Tên'.ljust(15)}{'Giới tính'.ljust(12)}{'Chuyên ngành'.ljust(15)}{'Điểm TB'.ljust(12)}{'Xếp loại'}")
        for student in self.students:
            print(f"{str(student.id).ljust(5)}{student.name.ljust(15)}{student.gender.ljust(12)}{student.major.ljust(15)}{f'{student.averageScore:.2f}'.ljust(12)}{student.rank}")

def main():
    lst = StudentList()

    # Thêm sẵn 2 sinh viên để kiểm tra
    student1 = Student("Nguyen Van Quy", "nam", "cntt", 8.5)
    student2 = Student("Tran Thi An", "nu", "toan", 6.8)
    lst.addStudent(student1)
    lst.addStudent(student2)

    while True:
        print("1. Thêm sinh viên")
        print("2. Cập nhật thông tin sinh viên theo ID")
        print("3. Xóa sinh viên theo ID")
        print("4. Tìm kiếm sinh viên qua tên")
        print("5. Sắp xếp sinh viên theo điểm trung bình")
        print("6. Sắp xếp danh sách sinh viên theo chuyên ngành")
        print("7. Hiển thị danh sách sinh viên")
        print("0. Thoát")
        choice = int(input("Nhập lựa chọn của bạn: "))
        match choice:
            case 1:
                print("Nhập tên sinh viên: ")
                name = input()
                print("Nhập giới tính sinh viên (nam/nu): ")
                gender = input().lower()
                while gender not in ["nam", "nu"]:
                    print("Giới tính không hợp lệ, vui lòng nhập lại (nam/nu):")
                    gender = input().lower()
                print("Nhập chuyên ngành sinh viên: ")
                major = input()
                print("Nhập điểm trung bình sinh viên (0-10): ")
                while True:
                    try:
                        averageScore = float(input())
                        if 0 <= averageScore <= 10:
                            break
                        else:
                            print("Điểm trung bình phải từ 0 đến 10, vui lòng nhập lại:")
                    except ValueError:
                        print("Điểm không hợp lệ, vui lòng nhập lại (số từ 0-10):")
                student = Student(name, gender, major, averageScore)
                lst.addStudent(student)
                print("Thêm sinh viên thành công!")
                input("Nhấn Enter để tiếp tục...")
            case 2:
                print("Nhập ID sinh viên cần cập nhật: ")
                id = int(input())
                print("Nhập tên sinh viên mới: ")
                name = input()
                print("Nhập giới tính sinh viên mới (nam/nu): ")
                gender = input().lower()
                while gender not in ["nam", "nu"]:
                    print("Giới tính không hợp lệ, vui lòng nhập lại (nam/nu):")
                    gender = input().lower()
                print("Nhập chuyên ngành sinh viên mới: ")
                major = input()
                print("Nhập điểm trung bình sinh viên mới (0-10): ")
                while True:
                    try:
                        averageScore = float(input())
                        if 0 <= averageScore <= 10:
                            break
                        else:
                            print("Điểm trung bình phải từ 0 đến 10, vui lòng nhập lại:")
                    except ValueError:
                        print("Điểm không hợp lệ, vui lòng nhập lại (số từ 0-10):")
                lst.updateStudent(id, name, gender, major, averageScore)
                print("Cập nhật sinh viên thành công!")
                input("Nhấn Enter để tiếp tục...")
            case 3:
                print("Nhập ID sinh viên cần xóa: ")
                id = int(input())
                lst.deleteStudent(id)
                print("Xóa sinh viên thành công!")
                input("Nhấn Enter để tiếp tục...")
            case 4:
                print("Nhập tên sinh viên cần tìm: ")
                name = input()
                result = lst.searchStudent(name)
                if result:
                    print("Danh sách sinh viên tìm thấy:")
                    for student in result:
                        print(f"{student.id}\t{student.name}\t{student.major}\t{student.averageScore}\t{student.rank}")
                else:
                    print("Không tìm thấy sinh viên nào.")
                input("Nhấn Enter để tiếp tục...")
            case 5:
                lst.sortByAverageScore()
                print("Danh sách sinh viên đã được sắp xếp theo điểm trung bình:")
                lst.displayStudents()
                input("Nhấn Enter để tiếp tục...")
            case 6:
                lst.sortByMajor()
                print("Danh sách sinh viên đã được sắp xếp theo chuyên ngành:")
                lst.displayStudents()
                input("Nhấn Enter để tiếp tục...")
            case 7:
                lst.displayStudents()
                input("Nhấn Enter để tiếp tục...")
            case 0:
                print("Chương trình kết thúc.")
                break
        # Clear terminal
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()