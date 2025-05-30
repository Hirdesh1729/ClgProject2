import sqlite3

def create_table():
    with sqlite3.connect("Teacher_Data.db") as con:
        cursor = con.cursor()
        cursor.execute('DROP TABLE IF EXISTS TeacherData')
        
        #Creating Table
        cursor.execute('''
                    CREATE TABLE TeacherData(
                        Id INTEGER NOT NULL,
                        Name TEXT NOT NULL,
                        Department TEXT NOT NULL,
                        Branch TEXT NOT NULL,
                        City TEXT NOT NULL,
                        email TEXT NOT NULL,
                        Phone TEXT NOT NULL)
                       ''')
        
        # List of Teacher Records
        teacher_data = [
    (25001, 'Ananya Sharma', 'Computer Science', 'CSE', 'Mumbai', 'ananya.sharma@example.com', '9876543210'),
    (25002, 'Raj Mehta', 'Mechanical', 'ME', 'Delhi', 'raj.mehta@example.com', '9876543211'),
    (25003, 'Sneha Patel', 'Electronics', 'ECE', 'Ahmedabad', 'sneha.patel@example.com', '9876543212'),
    (25004, 'Aman Verma', 'Electrical', 'EE', 'Kolkata', 'aman.verma@example.com', '9876543213'),
    (25005, 'Priya Singh', 'Civil', 'CE', 'Pune', 'priya.singh@example.com', '9876543214'),
    (25006, 'Karan Joshi', 'Computer Science', 'CSE', 'Bengaluru', 'karan.joshi@example.com', '9876543215'),
    (25007, 'Meera Iyer', 'Mechanical', 'ME', 'Chennai', 'meera.iyer@example.com', '9876543216'),
    (25008, 'Alok Nair', 'Electronics', 'ECE', 'Thiruvananthapuram', 'alok.nair@example.com', '9876543217'),
    (25009, 'Divya Kapoor', 'Electrical', 'EE', 'Lucknow', 'divya.kapoor@example.com', '9876543218'),
    (25010, 'Nikhil Jain', 'Civil', 'CE', 'Jaipur', 'nikhil.jain@example.com', '9876543219'),
    (25011, 'Tanvi Rao', 'Computer Science', 'CSE', 'Hyderabad', 'tanvi.rao@example.com', '9876543220'),
    (25012, 'Rohan Deshmukh', 'Mechanical', 'ME', 'Nagpur', 'rohan.deshmukh@example.com', '9876543221'),
    (25013, 'Isha Bhatt', 'Electronics', 'ECE', 'Surat', 'isha.bhatt@example.com', '9876543222'),
    (25014, 'Manav Gupta', 'Electrical', 'EE', 'Patna', 'manav.gupta@example.com', '9876543223'),
    (25015, 'Neha Reddy', 'Civil', 'CE', 'Vijayawada', 'neha.reddy@example.com', '9876543224'),
    (25016, 'Arjun Malhotra', 'Computer Science', 'CSE', 'Chandigarh', 'arjun.malhotra@example.com', '9876543225'),
    (25017, 'Ritika Das', 'Mechanical', 'ME', 'Guwahati', 'ritika.das@example.com', '9876543226'),
    (25018, 'Vivek Kulkarni', 'Electronics', 'ECE', 'Nashik', 'vivek.kulkarni@example.com', '9876543227'),
    (25019, 'Simran Kaur', 'Electrical', 'EE', 'Amritsar', 'simran.kaur@example.com', '9876543228'),
    (25020, 'Yash Thakur', 'Civil', 'CE', 'Indore', 'yash.thakur@example.com', '9876543229'),
    (25021, 'Shruti Yash', 'Computer Science', 'CSE', 'Kanpur', 'shruti.joshi@example.com', '9876543230'),
    (25022, 'Aniket Sen', 'Mechanical', 'ME', 'Bhopal', 'aniket.sen@example.com', '9876543231'),
    (25023, 'Pooja Mishra', 'Electronics', 'ECE', 'Ranchi', 'pooja.mishra@example.com', '9876543232'),
    (25024, 'Harshita Goyal', 'Electrical', 'EE', 'Noida', 'harshita.goyal@example.com', '9876543233'),
    (25025, 'Aditya Rao', 'Civil', 'CE', 'Mangalore', 'aditya.rao@example.com', '9876543234')
]
 
        #INSERTING RECORD
        cursor.executemany("INSERT INTO TeacherData VALUES (?,?,?,?,?,?,?)", teacher_data)
        
        cursor.execute('SELECT * FROM TeacherData')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            
        con.commit()
        print("Table Created Successfull")
        

create_table()        