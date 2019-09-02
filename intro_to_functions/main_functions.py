def convert_to_months(months):
  months_in_a_year = 12
  years = months_in_a_year / months
  return years

if __name__ == "__main__":
    months_from_user = input("Enter age in months: ")
    age_in_months = int(months_from_user)
    age_in_years = convert_to_months(age_in_months)
    print(f'{age_in_years}' + " is " + f'{age_in_months}' + " months.")
