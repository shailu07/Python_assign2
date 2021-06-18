salary= int(input())
year=int(input())
if year>5:
    bonus=int(salary*(0.05))
    print(f"Bonus is {bonus}")
else:
    print("No Bonus")