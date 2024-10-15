import csv
#Convert employee data to dictionary
def read_employees(csv_file_location):
        csv.register_dialect('empDialect', skipinitialspace=True, strict = True) #remove any leading spaces while parsing the CSV file
        employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')#Opening the csv 
        employee_list = [] #Creating one empty list of employees
        for data in employee_file: #iterate over the csv file 
                employee_list.append(dict(data)) #each iteration produce a dictionary from strings (key) to strings (value).
        return employee_list
employee_list = read_employees("/home/student/data/employees.csv")
#print(employee_list)

#Process employee data
def process_data(employee_list): #use generated list as paramete to the function
        department_list = [] #naming new intermediate listthat contain all the mentions of department o$
        for employee_data in employee_list: #defining iteration variables over list elements 
                department_list.append(employee_data['Department']) #Generating the list of mentions of$
        department_data = {} #creating the directory variable to save the number of mentions on departm$
        for department_name in set(department_list): #set() method converts iterable elements to dustin$
                department_data[department_name] = department_list.count(department_name) #adding each $
        return department_data 
dictionary = process_data(employee_list) 
#print(dictionary)

#Generating the report
def write_report(dictionary, report_file):
        with open(report_file, "w+") as f:
                for k in sorted(dictionary):
                        f.write(str(k) + ':' + str(dictionary[k]) + '\n')
                f.close()
write_report(dictionary, '/home/student/test_report.txt')
