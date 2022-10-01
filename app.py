import dbhelper


def display_homes(homes):
    for home in homes:
        print('------')
        print('address', home[1])
        print('rooms', home[2])
        print('bathrooms', home[3])
        print('square feet', home[4])
        print('------')


def ask_homes_rooms():
    num_rooms = input('please input number of rooms:')
    results = dbhelper.run_statment('CALL rooms(?)', [num_rooms])
    display_homes(results)

        


def ask_homes_city():
    city = input('please input city:')
    results = dbhelper.run_statment('CALL search_city(?)', [city])
    display_homes(results)


ask_homes_rooms()
# ask_homes_city()

