def scoreToGrade(scores):
    grades = []

    for i in scores:
        if int(i) >= 90:
            grades.append('A')
        elif 80 <= int(i) < 90:
            grades.append('B')
        elif 70 <= int(i) < 80:
            grades.append('C')
        elif 60 <= int(i) < 70:
            grades.append('D')
        else:
            grades.append('F')

    return grades

def main():
    a=input("Enter the degree of students: ").split()
    print(scoreToGrade(a))
if __name__ == "__main__":
    main()
