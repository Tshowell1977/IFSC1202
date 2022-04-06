class Employee:
   
    def __init__(self, FirstName= "", LastName="", IDNumber = 0, HoursWorked=0, Wage=0):
         
        self.FirstName = FirstName
        self.LastName = LastName
        self.IDNumber = IDNumber
        self.HoursWorked = HoursWorked
        self.Wage = Wage 

    
    def WeeklyPay(self):
        weekly_pay = 0
        
        if(self.HoursWorked<=40):
            weekly_pay = self.HoursWorked*self.Wage
        else: 
         
            weekly_pay = (self.Wage*40)+(self.Wage*1.5*(self.HoursWorked-40))
        return weekly_pay

    
    def __str__(self):
        return self.FirstName+" "+self.LastName+" "+str(self.IDNumber)+" "+str(self.HoursWorked)+" "+str(self.Wage)+" "+str(self.WeeklyPay())

        

if "__main__"== __name__:
    
    file = open("/workspace/IFSC1202/10.06 Payroll.txt")
 
    print("First\tLast\tId\tHours\tHourly\tWeekly")
    print("Name\tName\tNumber\tWorked\tWage\tPay")
    for line in file.readlines():
        line = line.split(",")
        
        emp = Employee(line[0], line[1], int(line[2]), int(line[3]), float(line[4]))
        
        print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(emp.FirstName, emp.LastName, emp.IDNumber, emp.HoursWorked, emp.Wage, emp.WeeklyPay()))