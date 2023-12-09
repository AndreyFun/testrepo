from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    today = date.today()
    birthdays_per_week = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],
        }

    
    for user in users:
        
        user_birthday = user['birthday']

        if user_birthday.year < today.year:
            user_birthday = user_birthday.replace(year=today.year + 1)
            
        if today <= user_birthday < today + timedelta(days=7):
            day_of_week = user_birthday.strftime("%A")

            if day_of_week in birthdays_per_week:
                if day_of_week in ["Saturday", "Sunday"]:
                    user_birthday += timedelta(days=1)
                    day_of_week = "Monday"
                birthdays_per_week[day_of_week].append(user["name"])
    
    birthdays_per_week = {
        day_name: names for day_name, names in birthdays_per_week.items() if names
    }
    return birthdays_per_week


