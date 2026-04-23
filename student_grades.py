from itertools import count


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self,index):

        body = self.scores[index]

        if body in range(90,101):
            return "A"
        elif body in range(80,90):
            return "B"
        elif body in range(70,80):
            return "C"
        elif body in range(60,70):
            return "D"
        elif body in range(50,60):
            return "E"
        elif body in range(0,50):
            return "F"


    def find(self,body):
        indexy = []
        scores = self.scores
        for i in range(len(scores)-1):
            if scores[i] == body:
                indexy.append(i)
        return indexy

    def get_sorted(self,):
        scores = list(self.scores)

        for x in range(len(scores)):
            for i in range(len(scores) - 1):
                if scores[i] > scores[i + 1]:
                    scores[i], scores[i + 1] = scores[i + 1], scores[i]

        return scores

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    pocet_studentu = results.count()

    for i in range(pocet_studentu):
        body = results.get_by_index(i)
        znamka = results.get_grade(i)
        print(f"Student {i}: {body} points – {znamka}")
        if body == 100:
            print(i)
    vysledky = results.get_sorted(body)






if __name__ == "__main__":
        results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

        print(results.count())  # 9
        print(results.get_by_index(2))  # 91
        print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]

        print(results.get_grade(2))  # A (91 bodů)
        print(results.get_grade(6))  # A (100 bodů)
        print(results.get_grade(7))  # F (38 bodů)

        print(results.find(100))  # [6]
        print(results.find(50))  # [4]
        print(results.find(77))  # []

        print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
        print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny

        main()