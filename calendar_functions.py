# Emma Stoverink
# November 14, 2018

# Enter a year
# Enter a month
# Output calendar for that month

def get_month(month_num):
    # takes in int value as the month
    # returns a string value of the year
    months = ["January","February","March", "April", "May", "June","July","August","September","October","November","December"]
    return(months[month_num-1])