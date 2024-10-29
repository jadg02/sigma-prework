import datetime
# update

date_input = input('Enter a date (dd-mm-yyyy): ')

date_input = [int(s) for s in date_input.split('-')]

input_date = datetime.datetime(date_input[2], date_input[1], date_input[0])

cur_date = datetime.datetime.now()

print(abs(cur_date-input_date).days//365, 'years')
