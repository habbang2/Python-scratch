# 점수
def grade(midterm, final):
    total = midterm + final
    if total > 90:
        print("You get an A.")
    elif 80 <= total:
        print("You get a B.")
    elif 70 <= total:
        print("You get a C.")
    elif 60 <= total:
        print("You get a D.")
    else :
        print("You get a F.")
    

grade(40, 45)
grade(23, 24)
grade(47, 72)