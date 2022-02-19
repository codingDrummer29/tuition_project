for i in range(20):
    pan=int(input("enter pan number:"))
    name=input("enter name of employee:")
    salary=int(input("enter the annual salary:"))
    surchg=0
    if salary >= 250000 and salary < 500000:
        tax = (salary * 0.05)
    elif salary >= 500000 and salary < 1000000:
        tax = (salary * 0.2)
    elif salary >= 1000000 and salary < 10000000:
        tax = (salary * 0.3)
        if salary > 5000000 and salary <= 10000000:
            surchg = (tax * 0.1)
        else:
            surchg = (tax * 0.15)
    else:
        tax = 0
    cess = (tax * 0.04)
    print("Pan No.\t\tName\t\tAnnual Salary\t\tTax\t\tCess\t\tSurcharge\tTotal Tax")
    print(str(pan)+"\t\t"+str(name)+"\t\t"+str(salary)+"\t\t\t"+str(tax)+"\t"+str(cess)+"\t\t"+str(surchg)+"\t\t"+str(tax+cess+surchg))
