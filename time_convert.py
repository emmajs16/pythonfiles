# Emma Stoverink
# September 5, 2018
# Problem: Take a number in seconds and output the time in minutes and seconds
def convert_time():
    # Get time in seconds
    time =  int(input("Please enter a time in seconds:"))
    # Convert the time to minutes and seconds
    minutes = time // 60
    seconds = time % 60
    # Output the results
    print("\t", time, "seconds is equal to", minutes,"minutes and", seconds,"seconds.")
convert_time()