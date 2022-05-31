# Nested List

if __name__ == '__main__':
    l = []
    scoreL = []
    for _ in range(int(input('Enter the number of students: '))):
        name = input('Enter the name of the student: ')
        score = float(input('Enter the score of the student: '))
        scoreL.append(score)
        subL = [score,name]
        l.append(subL)
        scoreL.sort()
        l.sort()
    for i in range(len(scoreL)):
        if scoreL[i] > scoreL[0]:
            sg = scoreL[i]
            break
    for p in l:
        if sg in p:
            print(p[1])
