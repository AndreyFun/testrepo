from datetime import date, datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def get_birthdays_per_week(users):
    today = date.today()
    birthdays_per_week = {day: [] for day in weekdays}

    if not users:
        return {}
    all_birthdays_passed = all(today > user['birthday'].replace(year=today.year) for user in users)
    if all_birthdays_passed:
        return {}

    for user in users:
        user_name = user['name']
        user_birthday = user['birthday'].replace(year=today.year)

        def change_actual_year(user_birthday):
            if today > user_birthday:
                return user_birthday.replace(year=today.year + 1)
            else:
                 return user_birthday
        

        def output_birthday(user_name, user_birthday):
            condition_met = today.year < user_birthday.year or (today.year == user_birthday.year and user_birthday.weekday() >= 5)
            

            while user_birthday.weekday() >= 5:
                user_birthday += timedelta(days=1)

            if condition_met:
                day_name = weekdays[user_birthday.weekday()]
                birthdays_per_week[day_name].append(user_name)

        user_birthday = change_actual_year(user_birthday)
        output_birthday(user_name, user_birthday)

    return birthdays_per_week

