import sqlite3 as sql


# Class for DataBase
class sqldb(object):
    '''
    def __init__(self, Website_Name, User_Input, Password_Input):
        self.connnection = sql.connect('DataBase.db')
        self.cursor = self.connnection.cursor()
        self.Website_Name = Website_Name
        self.User_Input = User_Input
        self.Password_Input = Password_Input
        try:
            self.cursor.execute('CREATE TABLE DataBase (Website TEXT, Username TEXT, Password TEXT)')
            self.connnection.commit()
        except sql.OperationalError:
            pass
            '''

    def __init__(self, Website_Name):
        self.Website_Name = Website_Name
        self.connnection = sql.connect('DataBase.db')
        self.cursor = self.connnection.cursor()
        try:
            self.cursor.execute('CREATE TABLE DataBase (Website TEXT, Username TEXT, Password TEXT)')
            self.connnection.commit()
        except sql.OperationalError:
            pass
    '''
    def __addData__(self):
        self.cursor.execute('INSERT INTO DataBase VALUES(?,?,?)', (self.Website_Name, self.User_Input, self.Password_Input))
        self.connnection.commit()
        '''
    def __FetchData__(self):
        self.cursor.execute('SELECT * FROM DataBase WHERE Website=?', (self.Website_Name, ))
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)



    # Taking Input From the User

#Website_Input = input("WebSite Name: ")
'''
User_value, Password_value = input(
    f"What is the Username and Password for {Website_Input} (Ex. Username , Password format): ").split(",")
'''
sqldb("Hello.com").__FetchData__()

##############################################
''''
THis is the fake version of DataBsae module
'''