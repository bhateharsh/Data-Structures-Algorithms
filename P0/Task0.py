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
# Display Functions
def printTextInfo(entry):
    """Function to print text info"""
    incomingNos = entry[0]
    answeringNos = entry[1]
    time = entry[2]
    msg="First record of texts, {} texts {} at time {}"\
        .format(incomingNos, answeringNos, time)
    print (msg)

def printCallInfo(entry):
    """Function to print text info"""
    incomingNos = entry[0]
    answeringNos = entry[1]
    time = entry[2]
    duration=entry[3]
    msg="Last record of calls, {} calls {} at time {}, lasting {} seconds"\
        .format(incomingNos, answeringNos, time, duration)
    print (msg)

# Test Functions
def testPrintTextInfo():
    """Function to test printTextInfo()"""
    entry=texts[1]
    msg="Input Entry: {}".format(entry)
    print (msg)
    printTextInfo(entry)

def testPrintCallInfo():
    """Function to test printCallInfo()"""
    entry=calls[-1]
    msg="Input Entry: {}".format(entry)
    print (msg)
    printCallInfo(entry)

# Testing Display Functions (Uncomment to test)
# testPrintTextInfo()
# testPrintCallInfo()

# Executing the task
textEntry=texts[0]  # First Entry of text
callEntry=calls[-1] # Last Entry of call
printTextInfo(textEntry)
printCallInfo(callEntry)