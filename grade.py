score = int(input("enter your score: "))

if score >= 101:
    print("enter a valid score")
    exit()

if score >= 90:
    grade ="A"
elif score >= 80:
    grade ="B"
elif score >= 70:
    grade ="C"
elif score >= 60:
    grade ="D"
elif score >= 50:
    grade ="E"
else:
    grade ="F"

print("Your grade according to your score is",grade)    
