def eos_cal(enlistment_date, education_level, extra_year, extra_3m):
	#split current date
	if "/" in enlistment_date:
		date_as_list = enlistment_date.split("/")
	elif "-" in enlistment_date:
		date_as_list = enlistment_date.split("-")
	#set the year and month
	if int(date_as_list[0]) > 100:
		year = int(date_as_list[0])
	else:
		year = int(date_as_list[2])
	month = int(date_as_list[1])

	#start calculation
	end_day = "25"
	if month in [1,2]:
		if not education_level == "فوق متوسط":
			end_month = "2"
			if extra_year:
				end_day = 10
				if extra_3m:
					end_month = "7"
				else:
					end_month = "4"
			elif extra_3m:
				end_month = "5"
			if education_level == "عليا":
				end_year = year + 1
			if education_level == "متوسط":
				end_year = year + 2
			if education_level == "بدون مؤهل":
				end_year = year + 3
		else:
			end_month = "8"
			end_year = year + 1
			if extra_year:
				end_day = 10
				if extra_3m:
					end_month = "1"
					end_year = year + 2
				else:
					end_month = "10"
			elif extra_3m:
				end_month = "11"

	elif month == 4:
		if not education_level == "فوق متوسط":
			end_month = "5"
			if extra_year:
				end_day = 10
				if extra_3m:
					end_month = "10"
				else:
					end_month = "7"
			elif extra_3m:
				end_month = "8"
			if education_level == "عليا":
				end_year = year + 1
			if education_level == "متوسط":
				end_year = year + 2
			if education_level == "بدون مؤهل":
				end_year = year + 3
		else:
			end_month = "11"
			end_year = year + 1
			if extra_year:
				end_day = 10
				if extra_3m:
					end_month = "4"
					end_year = year + 2
				else:
					end_month = "1"
					end_year = year + 2
			elif extra_3m:
				end_month = "2"
				end_year = year + 2

	elif month == 7:
		if not education_level == "فوق متوسط":
			end_month = "8"
			if extra_year:
				end_day = 10
				if extra_3m:
					end_month = "1"
					year += 1
				else:
					end_month = "10"
			elif extra_3m:
				end_month = "11"
			if education_level == "عليا":
				end_year = year + 1
			if education_level == "متوسط":
				end_year = year + 2
			if education_level == "بدون مؤهل":
				end_year = year + 3
		else:
			end_month = "2"
			end_year = year + 2
			if extra_year:
				end_day = 10
				if extra_3m:
					end_month = "7"
				else:
					end_month = "4"
			elif extra_3m:
				end_month = "5"

	elif month == 10:
		if not education_level == "فوق متوسط":
			end_month = "11"
			if extra_year:
				end_day = 10
				if extra_3m:
					end_month = "4"
					year += 1
				else:
					end_month = "1"
					year += 1
			elif extra_3m:
				end_month = "2"
				year += 1
			if education_level == "عليا":
				end_year = year + 1
			if education_level == "متوسط":
				end_year = year + 2
			if education_level == "بدون مؤهل":
				end_year = year + 3
		else:
			end_month = "5"
			end_year = year + 2
			if extra_year:
				end_day = 10
				if extra_3m:
					end_month = "10"
				else:
					end_month = "7"
			elif extra_3m:
				end_month = "8"

	return f"{end_year}/{end_month}/{end_day}"


class Soldier:
	
	soldiers_counter = 0
    
	def __init__(it,id = -1, name = "name",current_state = "none",department = "green horn", governorate = "egypt", saeed = False,police_id = "00000",enlistment_date = "1/1/2020", birth_date = "1/1/1900", trial_id = "00/00/00", national_id = "000", address = "address",education_level = "عليا", extra_year = False, extra_3m = False,  weapon_ban = False,muslim = True, phone_num = "010", fa_phone_num = "011", maried = False):
		it.id = id
		it.name = name
		it.current_state = current_state
		it.department = department
		it.governorate = governorate
		it.saeed = saeed
		it.police_id = police_id
		it.enlistment_date = enlistment_date
		it.EOS_date = eos_cal(enlistment_date, education_level.strip(), extra_year, extra_3m)
		it.birth_date = birth_date
		it.trial_id = trial_id
		it.national_id = national_id
		it.address = address
		it.education_level = education_level.strip()
		it.extra_year = extra_year
		it.extra_3m = extra_3m
		it.weapon_ban = weapon_ban
		it.muslim = muslim
		it.phone_num = phone_num
		it.fa_phone_num = fa_phone_num
		it.maried = maried
		Soldier.soldiers_counter += 1

	def get_all(it):
		return (it.get_name(),it.get_current_state(),it.get_department(),it.get_governorate(),it.is_saeed(),it.get_police_id(),it.get_enlistment_date(),it.get_birth_date(),it.get_trial_id(),it.get_national_id(),it.get_address(),it.get_education_level(),it.is_extra_year(),it.is_extra_3m(),it.is_weapon_ban(),it.is_muslim(),it.get_phone_num(),it.get_fa_phone_num(),it.is_maried())
	
	
	def get_current_state(it):
		return it.current_state

	def set_current_state(it,current_state):
		it.current_state = current_state


	def get_name(it):
		return it.name

	def set_name(it,name):
		it.name = name


	def get_department(it):
		return it.department

	def set_department(it,department):
		it.department = department


	def get_governorate(it):
		return it.governorate

	def set_governorate(it,governorate):
		it.governorate = governorate


	def is_saeed(it):
		return it.saeed

	def set_saeed(it,saeed):
		it.saeed = saeed


	def get_police_id(it):
		return it.police_id

	def set_police_id(it,police_id):
		it.police_id = police_id


	def get_enlistment_date(it):
		return it.enlistment_date

	def set_enlistment_date(it,enlistment_date):
		it.enlistment_date = enlistment_date


	def get_eos(it):
		return it.EOS_date

	def set_eos(it):
		pass ####################


	def get_birth_date(it):
		return it.birth_date

	def set_birth_date(it,birth_date):
		it.birth_date = birth_date


	def get_trial_id(it):
		return it.trial_id

	def set_trial_id(it,trial_id):
		it.trial_id = trial_id


	def get_national_id(it):
		return it.national_id

	def set_national_id(it,national_id):
		it.national_id = national_id


	def get_address(it):
		return it.address

	def set_address(it,address):
		it.address = address


	def get_education_level(it):
		return it.education_level

	def set_education_level(it,education_level):
		it.education_level = education_level #########


	def is_extra_year(it):
		return it.extra_year

	def set_extra_year(it,extra_year):
		it.extra_year = extra_year ##########


	def is_extra_3m(it):
		return it.extra_3m

	def set_extra_3m(it,extra_3m):
		it.extra_3m = extra_3m ##########


	def is_weapon_ban(it):
		return it.weapon_ban

	def set_weapon_ban(it,weapon_ban):
		it.weapon_ban = weapon_ban


	def is_muslim(it):
		return it.muslim

	def set_muslim(it,muslim):
		it.muslim = muslim


	def get_phone_num(it):
		return it.phone_num

	def set_phone_num(it,phone_num):
		it.phone_num = phone_num


	def get_fa_phone_num(it):
		return it.fa_phone_num

	def set_fa_phone_num(it,fa_phone_num):
		it.fa_phone_num = fa_phone_num


	def is_maried(it):
		return it.maried

	def set_maried(it,maried):
		it.maried = maried