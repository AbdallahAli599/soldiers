# Import SQLite Module
import sqlite3

#import Soldier Class
import Soldier

# Create Database and connect
db = sqlite3.connect("soldiers.db")

# Create the soldiers table
db.execute("CREATE TABLE IF NOT EXISTS soldiers(id INTEGER PRIMARY KEY AUTOINCREMENT,current_state TEXT, name TEXT UNIQUE, department TEXT, governorate TEXT,saeed BOOL, police_id TEXT, enlistment_date TEXT, birth_date TEXT, trial_id TEXT, national_id TEXT, address TEXT, education_level TEXT, extra_year BOOL, extra_3m BOOL,  weapon_ban BOOL,muslim BOOL, phone_num TEXT, fa_phone_num TEXT, maried BOOL)")

department_list = ["الامن","تدريب","بوفيه السيد المدير","فندقة وإعاشة","منشآت تدريبية","صيانة وإنشاءات","ش. مجندين","ش. ضباط وأفراد","حملة","مخصصات","عهدة","مكتب","مكتب اتصال","نوبتجي"]
department_count_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def clear():
        x = 0
        while x in range(len(department_count_list)):
                department_count_list[x] = 0
                x += 1
        department_count_list.pop()

# Add a soldier to the db
def add(soldier):
        db = sqlite3.connect("soldiers.db")

        cr = db.cursor()

        cr.execute(f"SELECT * FROM soldiers WHERE name = {soldier.get_name()}")
        result = cr.fetchall()
        if not result:
                cr.execute(f"INSERT INTO soldiers(name, current_state, department, governorate,saeed, police_id, enlistment_date, birth_date, trial_id, national_id, address, education_level, extra_year, extra_3m,  weapon_ban,muslim, phone_num, fa_phone_num, maried) VALUES('{soldier.get_name()}', '{soldier.get_current_state()}', '{soldier.get_department()}', '{soldier.get_governorate()}', '{soldier.is_saeed()}', '{soldier.get_police_id()}', '{soldier.get_enlistment_date()}', '{soldier.get_birth_date()}', '{soldier.get_trial_id()}', '{soldier.get_national_id()}', '{soldier.get_address()}', '{soldier.get_education_level()}', '{soldier.is_extra_year()}', '{soldier.is_extra_3m()}', '{soldier.is_weapon_ban()}', '{soldier.is_muslim()}', '{soldier.get_phone_num()}', '{soldier.get_fa_phone_num()}', '{soldier.is_maried()}')")

        # Commit changes
        db.commit()

        # Close database
        db.close()

def set_status(name:str,state):
        db = sqlite3.connect("soldiers.db")

        cr = db.cursor()

        cr.execute(f"UPDATE soldiers SET current_state = '{state}' WHERE name in('{name}',{name.strip()})")

        # Commit changes
        db.commit()

        # Close database
        db.close()

def get_soldier(name):
        db = sqlite3.connect("soldiers.db")

        cr = db.cursor()
        cr.execute(f"SELECT * FROM soldiers WHERE name LIKE '%{name}%'")
        result = cr.fetchall()
        soldiers_list = []
        for row in result:
                out = Soldier.Soldier(row[0],row[2],row[1],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19])
                soldiers_list.append(out)
        db.close()
        return soldiers_list

#get totals
def get_total_departments_count():
        clear()
        db = sqlite3.connect("soldiers.db")

        cr = db.cursor()
        cr.execute(f"SELECT department FROM soldiers")
        result = cr.fetchall()
        total = 0
        for row in result:
                dep = str(row[0])
                if dep.__contains__("حملة "):
                        dep = "مخصصات"
                elif dep.__contains__("مكتب ") and not dep.__contains__("مكتب اتصال"):
                        dep = "مكتب"
                elif dep.__contains__("فراد") or dep.__contains__("ضباط"):
                        dep = "ش. ضباط وأفراد"
                if dep in department_list:
                        department_count_list[department_list.index(dep)] += 1
                else:
                        department_list.append(dep)
                        department_count_list.append(1)
                total += 1
        if not department_list.__contains__("المجموع"):
                department_list.append("المجموع")
        department_count_list.append(total)
        return [department_list,department_count_list]

def get_here_departments_count(with_m:bool):
        clear()
        db = sqlite3.connect("soldiers.db")

        cr = db.cursor()
        if with_m:
                cr.execute(f"SELECT department FROM soldiers WHERE current_state = 'ا' or current_state = 'م'")
        else:
                cr.execute(f"SELECT department FROM soldiers WHERE current_state = 'ا'")
        result = cr.fetchall()
        total = 0
        for row in result:
                dep = str(row[0])
                if dep.__contains__("حملة "):
                        dep = "مخصصات"
                elif dep.__contains__("مكتب ") and not dep.__contains__("مكتب اتصال"):
                        dep = "مكتب"
                elif dep.__contains__("فراد") or dep.__contains__("ضباط"):
                        dep = "ش. ضباط وأفراد"
                if dep in department_list:
                        department_count_list[department_list.index(dep)] += 1
                else:
                        department_list.append(dep)
                        department_count_list.append(1)
                total += 1
        department_count_list.append(total)
        return department_count_list

def get_out_departments_count():
        clear()
        db = sqlite3.connect("soldiers.db")

        cr = db.cursor()
        cr.execute(f"SELECT department FROM soldiers WHERE current_state IN ('ج', 'ع')")
        result = cr.fetchall()
        total = 0
        for row in result:
                dep = str(row[0])
                if dep.__contains__("حملة "):
                        dep = "مخصصات"
                elif dep.__contains__("مكتب ") and not dep.__contains__("مكتب اتصال"):
                        dep = "مكتب"
                elif dep.__contains__("فراد") or dep.__contains__("ضباط"):
                        dep = "ش. ضباط وأفراد"
                if dep in department_list:
                        department_count_list[department_list.index(dep)] += 1
                else:
                        department_list.append(dep)
                        department_count_list.append(1)
                total += 1
        department_count_list.append(total)
        return department_count_list

def get_khawareg_count(with_m:bool):
        clear()
        db = sqlite3.connect("soldiers.db")

        cr = db.cursor()
        if with_m:
                cr.execute(f"SELECT department FROM soldiers WHERE current_state in ('ج' , 'ع' , 'ش' , 'س ن' , 'س م' , 'غ' , 'س' , 'ج م' , 'فرقة' , 'م')")
        else:
                cr.execute(f"SELECT department FROM soldiers WHERE current_state in ('ج' , 'ع' , 'ش' , 'س ن' , 'س م' , 'غ' , 'س' , 'ج م' , 'فرقة')")
        result = cr.fetchall()
        total = 0
        for row in result:
                dep = str(row[0])
                if dep.__contains__("حملة "):
                        dep = "مخصصات"
                elif dep.__contains__("مكتب ") and not dep.__contains__("مكتب اتصال"):
                        dep = "مكتب"
                elif dep.__contains__("فراد") or dep.__contains__("ضباط"):
                        dep = "ش. ضباط وأفراد"
                if dep in department_list:
                        department_count_list[department_list.index(dep)] += 1
                else:
                        department_list.append(dep)
                        department_count_list.append(1)
                total += 1
        department_count_list.append(total)
        return department_count_list

def get_departments_count(search_value):
        clear()
        db = sqlite3.connect("soldiers.db")

        cr = db.cursor()
        cr.execute(f"SELECT department FROM soldiers WHERE current_state = '{search_value}'")
        result = cr.fetchall()
        total = 0
        for row in result:
                dep = str(row[0])
                if dep.__contains__("حملة "):
                        dep = "مخصصات"
                elif dep.__contains__("مكتب ") and not dep.__contains__("مكتب اتصال"):
                        dep = "مكتب"
                elif dep.__contains__("فراد") or dep.__contains__("ضباط"):
                        dep = "ش. ضباط وأفراد"
                if dep in department_list:
                        department_count_list[department_list.index(dep)] += 1
                else:
                        department_list.append(dep)
                        department_count_list.append(1)
                total += 1
        department_count_list.append(total)
        return department_count_list

# create a new month
def create_new_month(month:int,year:int):
        if month in (4,6,9,11):
                days = 31
        elif month == 2:
                if year%4 == 0:
                        days = 30
                else:
                        days = 29
        else:
                days = 32
        i = 1
        while i in range(days):
                db.execute(f"ALTER TABLE d43 ADD '{i}/{month}/{year}' TEXT")
                i += 1

# commit changes
db.commit()

# Close database
db.close()