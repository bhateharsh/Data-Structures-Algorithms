"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
# Checker Function
def checkTimeStamp(timeStamp):
    """Function to check if the time-stamp is correct.
    Parameters
    ----------
    timeStamp: str
    The timestamp of the entry
    
    Returns
    -------
    day: int
    The day of the time-stamp
    hr: int 
    The Hour of the time-stamp
    mins: int
    The minute of the time-stamp
    sec: int
    The second of the time-stamp

    Notes
    -----
    As per the information, the following facts are known:
        * All the calls are in the month of September (09) of year 2016 
        * A 24 hour format is used to report time (0=<hh<24, 0<=mm,ss<<59)
        * Format of time-stamp is 'dd-mm-yy hh:mm:ss' (0<dd<31)
    """
    # Defining Constants
    MAX_DAY = 30
    MIN_DAY = 1
    MAX_HR = 23
    MIN_HR = 0
    MAX_MINS = 59
    MIN_MINS = 0
    MAX_SEC = 59
    MIN_SEC = 0
    F_YEAR = 2016
    F_MONTH = 9
    # Extracting current event times
    day=int(timeStamp[0:2])
    month=int(timeStamp[3:5])
    year=int(timeStamp[6:10])
    hr=int(timeStamp[11:13])
    mins=int(timeStamp[14:16])
    sec=int(timeStamp[17:19])
    # Checking all parameters
    assert (year==F_YEAR)
    assert (month==F_MONTH)
    assert (day>=MIN_DAY and day<=MAX_DAY)
    assert (hr>=MIN_HR and hr<=MAX_HR)
    assert (mins>=MIN_MINS and mins<=MAX_MINS)
    assert (sec>=MIN_SEC and sec<=MAX_SEC)
    #Return the extracted Date
    return [day, hr, mins, sec]

# Function to check if date is minimum
def isMin(day1, hr1, mins1, sec1, day2, hr2, mins2, sec2):
    """Function to check if time-stamp1 is min versus time-stamp2

    Parameters
    ----------
    day1: int
    Day of time-stamp1
    hr1: int
    Hour of time-stamp1
    mins1: int
    Minutes of time-stamp1
    sec1: int
    Seconds of time-stamp1
    day2: int
    Day of time-stamp2
    hr2: int
    Hour of time-stamp2
    mins2: int
    Minutes of time-stamp2
    sec2: int
    Seconds of time-stamp2

    Returns
    -------
    isMin: bool
    True if time-stamp1 < time-stamp2
    """
    # Checking days
    if (day1<day2):
        return True
    if (day1>day2):
        return False
    if (hr1<hr2):
        return True
    if (hr1>hr2):
        return False
    if (mins1<mins2):
        return True
    if (mins1>mins2):
        return False
    if (sec1<sec2):
        return True
    if (sec1>=sec2):
        return False
    return False

def testIsMin():
    """Function to test isMin(...)
    """
    #Same Day
    assert (isMin(1, 0, 0, 53,
                1, 0, 0, 53)==False)
    #Different Day
    assert (isMin(2, 0, 0, 53,
                1, 0, 0, 53)==False)
    #Different Day
    assert (isMin(1, 0, 0, 53,
                5, 0, 0, 53)==True)
    #Different hrs
    assert (isMin(15, 5, 0, 53,
                15, 0, 2, 53)==False)
    #Different hrs
    assert (isMin(15, 4, 0, 53,
                15, 13, 0, 53)==True)
    #Print Output
    print("isMin() TESTS SUCCESSFUL!")

# Function to check if date is maximum
def isMax(day1, hr1, mins1, sec1, day2, hr2, mins2, sec2):
    """Function to check if time-stamp1 is max versus time-stamp2

    Parameters
    ----------
    day1: int
    Day of time-stamp1
    hr1: int
    Hour of time-stamp1
    mins1: int
    Minutes of time-stamp1
    sec1: int
    Seconds of time-stamp1
    day2: int
    Day of time-stamp2
    hr2: int
    Hour of time-stamp2
    mins2: int
    Minutes of time-stamp2
    sec2: int
    Seconds of time-stamp2

    Returns
    -------
    isMax: bool
    True if time-stamp1 > time-stamp2
    """
    # Checking days
    if (day1>day2):
        return True
    if (day1<day2):
        return False
    if (hr1>hr2):
        return True
    if (hr1<hr2):
        return False
    if (mins1>mins2):
        return True
    if (mins1<mins2):
        return False
    if (sec1>sec2):
        return True
    if (sec1<=sec2):
        return False
    return False

def testIsMax():
    """Function to test isMax(...)
    """
    #Same Day
    assert (isMax(1, 0, 0, 53,
                1, 0, 0, 53)==False)
    #Different Day
    assert (isMax(2, 0, 0, 53,
                1, 0, 0, 53)==True)
    #Different Day
    assert (isMax(1, 0, 0, 53,
                5, 0, 0, 53)==False)
    #Different hrs
    assert (isMax(15, 5, 0, 53,
                15, 0, 2, 53)==True)
    #Different hrs
    assert (isMax(15, 4, 0, 53,
                15, 13, 0, 53)==False)
    #Print Output
    print("isMax() TESTS SUCCESSFUL!")


# Function to first texter
def firstText():
    """Function to find the first text entry"""
    minDay=30
    minHours=23
    minMins=59
    minSecs=59
    for sendNos, recvNos, timeStamp in texts:
        day, hrs, mins, secs = checkTimeStamp(timeStamp)
        if (isMin(day, hrs, mins, secs, minDay, minHours, minMins, minSecs)):
            minDay=day
            minHours=hrs
            minMins=mins
            minSecs=secs
            displaySenderNos=sendNos
            displayRecvNos=recvNos
            displayTimeStamp=timeStamp
    msg="First record of texts, {} texts {} at time {}"\
        .format(displaySenderNos, displayRecvNos, displayTimeStamp)
    print (msg)

#Function to find last caller
def lastCall():
    """Function to find the first text entry"""
    maxDay=1
    maxHours=0
    maxMins=0
    maxSecs=0
    for sendNos, recvNos, timeStamp, duration in calls:
        day, hrs, mins, secs = checkTimeStamp(timeStamp)
        if (isMax(day, hrs, mins, secs, maxDay, maxHours, maxMins, maxSecs)):
            minDay=day
            minHours=hrs
            minMins=mins
            minSecs=secs
            displaySenderNos=sendNos
            displayRecvNos=recvNos
            displayTimeStamp=timeStamp
            displayDuration=duration
    msg="Last record of calls, {} calls {} at time {}, lasting {} seconds"\
        .format(displaySenderNos, 
            displayRecvNos, 
            displayTimeStamp, 
            displayDuration)
    print (msg)

# Testing
# testIsMin()
# testIsMax()
        
#Running functions
firstText()
lastCall()