import sqlite3

class Company:
    def __init__(self,dbname):
            self.conn=sqlite3.connect(dbname)
            self.c=self.conn.cursor()
    def create_table(self):
        self.c.execute('Create table employee(employee_id integer,employee_name text,employee_designation text)')
        print 'Employee table created'
    def select_employee(self):
	for row in self.c.execute('select * from employee'):
		print row
    def insert_employee(self,employee_id,employee_name,employee_designation):
        
        self.c.execute('''Insert into employee values("'''+str(employee_id)+'''","'''+str(employee_name)+'''","'''+employee_designation+'''")''')
        self.conn.commit()
    
        

i=Company('/Users/Narendra/Downloads/LearningPython/Company.db')




i.insert_employee(4,'Lei','Project Manager')
print i.select_employee()


