

user_input = input("Enter year in AD or BS?")


def Date_converter(a):
    if a == "AD":
        year_ad = int(input("Enter year: "))
        converted_year = year_ad + 57
        print("The year", year_ad, "AD in BS is ", converted_year)
    elif a == "BS":
        year_bs = int(input("Enter year: "))
        converted_year1 = year_bs - 57
        print("The year", year_bs, "BS in AD is ", converted_year1)


Date_converter(user_input)
