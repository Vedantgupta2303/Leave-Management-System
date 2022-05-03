import mysql.connector

# def dashboard_faculty():
# 	cursor=connection.cursor()
# 	cursor.execute("SELECT * from faculty_member where faculty_id='"+request.user.username+"';")
# 	#data = cursor.fetchone()
# 	cursor.execute("SELECT leave_type, no_days_left from days_left where faculty_id='"+data[0]+"';")
# 	#days = cursor.fetchone()
# 	connection.close()
	
# 	return(data, days)

# # We will show only approved leaves to the faculty	
# def history_page():
# 	cursor=connection.cursor()
# 	cursor.execute("SELECT * from leave_checked where faculty_id='"+request.user.username+"';")
	


# def admin_hod():
#     cursor=connection.cursor()
# 	cursor.execute("SELECT * from leave_request where leave_type=Casual,Special Casual, Restricted;")

# def admin_director():
# 	cursor=connection.cursor()
# 	cursor.execute("SELECT * from leave_request where leave_type=Leave Not Due,Extraordinary, Maternity,Quarantine, Child Care, Sabbatical, FST;")

# def admin_DOFA():
# 	cursor=connection.cursor()
# 	cursor.execute("SELECT * from leave_request where leave_type=Earned,Vacation, Half Pay, Commuted, Paternity;")


class Database:
    def __init__(self):
        conn = mysql.connector.connect(
            					user = "root",
                                host = "127.0.0.1",
                                password = "{Poorna@01}",
                                database = "taxmanagementsystem",
                                auth_plugin = 'mysql_native_password')
        
    def Register(self,FirstName,LastName,Age):
        mycursor = self.conn.cursor()
        sql = "INSERT INTO reg_details (FirstName,LastName,Age) VALUES (%s,%s,%s)"
        val = (FirstName,LastName,Age)
		mycursor.execute(sql,val)
		return True
    


	
