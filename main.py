import db_controller

#import random to use it in demo data
import random

#import Soldier Class
import Soldier


def put_demo_data(j):
    i = 0
    while i in range(j):
        x = Soldier.Soldier(name = f"soldier num {i}",department= random.choice(db_controller.department_list))
        db_controller.add(x)
        i += 1
def get_yaomia(primary:bool):
    names_and_total = db_controller.get_total_departments_count()
    names = names_and_total[0]
    totals = names_and_total[1]
    for name in names:
        print(name)
    input("press Enter to next column")
    for total in totals:
        if total == 0:
            print("-")
        else:
            print(total)
    input("press Enter to next column")
    print("شهرية إجازة")
    rows = db_controller.get_out_departments_count()
    for row in rows:
        if row == 0:
            print("-")
        else:
            print(row)
    input("press Enter to next column")
    print("شطب")
    rows = db_controller.get_departments_count("ش")
    for row in rows:
        if row == 0:
            print("-")
        else:
            print(row)
    input("press Enter to next column")
    print("إداري سجن")
    rows = db_controller.get_departments_count("س ن")
    for row in rows:
        if row == 0:
            print("-")
        else:
            print(row)
    input("press Enter to next column")
    print("محكوم سجن")
    rows = db_controller.get_departments_count("س م")
    for row in rows:
        if row == 0:
            print("-")
        else:
            print(row)
    input("press Enter to next column")
    print("غياب")
    rows = db_controller.get_departments_count("غ")
    for row in rows:
        if row == 0:
            print("-")
        else:
            print(row)
    input("press Enter to next column")
    print("مستشفى حجز")
    rows = db_controller.get_departments_count("س")
    for row in rows:
        if row == 0:
            print("-")
        else:
            print(row)
    input("press Enter to next column")
    print("مرضي إجازة")
    rows = db_controller.get_departments_count("ج م")
    for row in rows:
        if row == 0:
            print("-")
        else:
            print(row)
    input("press Enter to next column")
    print("فرقة")
    rows = db_controller.get_departments_count("فرقة")
    for row in rows:
        if row == 0:
            print("-")
        else:
            print(row)
    input("press Enter to next column")
    if primary:
        print("مأمورية")
        rows = db_controller.get_departments_count("م")
        for row in rows:
            if row == 0:
                print("-")
            else:
                print(row)
        input("press Enter to next column")
    print("الخوارج")
    rows = db_controller.get_khawareg_count(primary)
    for row in rows:
        if row == 0:
            print("-")
        else:
            print(row)
    input("press Enter to next column")
    print("الموجود")
    rows = db_controller.get_here_departments_count(not primary)
    for row in rows:
        if row == 0:
            print("-")
        else:
            print(row)
    input("press Enter to back to the main menu")
while True:
    res = input("""welcome to our new system
select an option bellow
1-  a soldier has back
2-  a soldier is going on holiday
3-  a soldier is going to m2moria
4-  get total soldiers counts
5-  get in holiday soldiers counts
6-  get active soldiers counts
7-  get a soldier main data
8-  get data about a soldier
9-  yaomia
10- yawmia almodeer
11- put demo data
or q to exit
""")
    if res == "1":
        soldier_name = input("type his name plz\n")
        db_controller.set_status(soldier_name,"ا")
    elif res == "2":
        soldier_name = input("type his name plz\n")
        db_controller.set_status(soldier_name,"ج")
    elif res == "3":
        soldier_name = input("type his name plz\n")
        db_controller.set_status(soldier_name,"م")
    elif res == "4":
        rows = db_controller.get_total_departments_count()
        names = rows[0]
        totals = rows[1]
        for name in names:
            print(name)
        input("press Enter to next column")
        for total in totals:
            if total == 0:
                print("-")
            else:
                print(total)
        input("press Enter to back to the main menu")
    elif res == "5":
        rows = db_controller.get_out_departments_count()
        for row in rows:
            print(row)
        input("press Enter to back to the main menu")
    elif res == "6":
        rows = db_controller.get_here_departments_count(False)
        for row in rows:
            print(row)
        input("press Enter to back to the main menu")
    elif res == "7":
        name = input("type his name plz\n")
        list = db_controller.get_soldier(name)
        x = 1
        for soldier in list:
            print(f"{x} - {soldier.get_name()}")
            x += 1
        soldier_num = input("choose soldier's number\n")
        print(f"name -> {list[int(soldier_num)-1].get_name()} , department -> {list[int(soldier_num)-1].get_department()}")
        input("press Enter to back to the main menu")
    elif res == "8":
        name = input("type his name plz\n")
        list = db_controller.get_soldier(name)
        x = 1
        for soldier in list:
            print(f"{x} - {soldier.get_name()}")
            x += 1
        soldier_num = input("choose soldier's number\n")
        while True:
            wanted_data = input("""which data do you want to know?
                1- current_state
                2- department
                3- governorate
                4- is saeed
                5- police_id
                6- enlistment_date
                7- birth_date
                8- trial_id
                9- national_id
                10- address
                11- education_level
                12- has extra_year
                13- has extra_3m
                14- has weapon_ban
                15- is muslim
                16- phone_num
                17- fa_phone_num
                18- is maried
    """)
            
            if wanted_data == "1":
                print(f"name -> {list[int(soldier_num)-1].get_name()} , current_state -> {list[int(soldier_num)-1].get_current_state()}")
            elif wanted_data == "2":
                print(f"name -> {list[int(soldier_num)-1].get_name()} , department -> {list[int(soldier_num)-1].get_department()}")
            elif wanted_data == "3":
                print(f"name -> {list[int(soldier_num)-1].get_name()} , governorate -> {list[int(soldier_num)-1].get_governorate()}")
            elif wanted_data == "4":
                print(f"name -> {list[int(soldier_num)-1].get_name()} , is saeed -> {list[int(soldier_num)-1].is_saeed()}")
            elif wanted_data == "5":
                print(f"name -> {list[int(soldier_num)-1].get_name()} , police_id -> {list[int(soldier_num)-1].get_police_id()}")
            elif wanted_data == "6":
                print(f"name -> {list[int(soldier_num)-1].get_name()} , enlistment_date -> {list[int(soldier_num)-1].get_enlistment_date()}")
            elif wanted_data == "7":
                print(f"name -> {list[int(soldier_num)-1].get_name()} , birth_date -> {list[int(soldier_num)-1].get_birth_date()}")
            elif wanted_data == "8":
                print(f"name -> {list[int(soldier_num)-1].get_name()} , trial_id -> {list[int(soldier_num)-1].get_trial_id()}")
            elif wanted_data == "9":
                print(f"name -> {list[int(soldier_num)-1].get_name()} , national_id -> {list[int(soldier_num)-1].get_national_id()}")
            elif wanted_data == "10":
                print(f"name -> {list[int(soldier_num)-1].get_name()} , address -> {list[int(soldier_num)-1].get_address()}")
            elif wanted_data == "11":
                print(f"name -> {list[int(soldier_num)-1].get_name()} , education_level -> {list[int(soldier_num)-1].get_education_level()}")
            elif wanted_data == "12":
                print(f"name -> {list[int(soldier_num)-1].get_name()} , has extra_year -> {list[int(soldier_num)-1].is_extra_year()}")
            elif wanted_data == "13":
                print(f"name -> {list[int(soldier_num)-1].get_name()} , has extra_3m -> {list[int(soldier_num)-1].is_extra_3m()}")
            elif wanted_data == "14":
                print(f"name -> {list[int(soldier_num)-1].get_name()} , has weapon_ban -> {list[int(soldier_num)-1].is_weapon_ban()}")
            elif wanted_data == "15":
                print(f"name -> {list[int(soldier_num)-1].get_name()} , is muslim -> {list[int(soldier_num)-1].is_muslim()}")
            elif wanted_data == "16":
                print(f"name -> {list[int(soldier_num)-1].get_name()} , phone_num -> {list[int(soldier_num)-1].get_phone_num()}")
            elif wanted_data == "17":
                print(f"name -> {list[int(soldier_num)-1].get_name()} , fa_phone_num -> {list[int(soldier_num)-1].get_fa_phone_num()}")
            elif wanted_data == "18":
                print(f"name -> {list[int(soldier_num)-1].get_name()} , is maried -> {list[int(soldier_num)-1].is_maried()}")
            elif wanted_data == "b":
                break
            else:
                print("wrong choice")
            inner_res = input("press Enter to choose another data you want to know or b to back to the main menu\n")
            if inner_res =="b":
                break 
    elif res == "9":
        get_yaomia(True)
    elif res == "10":
        get_yaomia(False)
    elif res == "11":
        num = input("how many soldiers do you want to put?\n")
        put_demo_data(int(num))
    elif res == "q":
        break
    else:
        print("wrong choice")
        input("press Enter to back to the main menu")