from subprocess import Popen, PIPE, STDOUT
from stackapi import StackAPI, StackAPIError
from datetime import date
import requests
import json


filePath = ' /Users/thomasfosen/Documents/Prosjekter/autoError/Auto-Search-Error-/error.py'

errorLibrary = ['NameError', 'IndexError', 'KeyError','IndentationError', 'TypeError', 'ValueError', 'ModuleNotFoundError', 'AttributeError']

process = Popen('python3' + filePath , stdout = PIPE, stderr = STDOUT, shell = True)
stdout, stderr = process.communicate()

consoleMessage = stdout.decode('utf-8')

logList = consoleMessage.split()


def checkOutput():
    index = 0
    for i in logList:
        index = index + 1
        for j in errorLibrary:
            if(i == j + ':'):
                return i, index

errorType, index = checkOutput()
errorMessage = ' '.join(logList[index:])

error = errorType + ' ' + errorMessage

print(error)


''' StackAPI '''

site = StackAPI('stackoverflow')

'''
listOfDicts = site.fetch('questions', min = 20, tagged = errorType, sort = 'votes',
fromdate = 1457136000, todate = date.today(), page_size = 1, max_pages = 1, accepted = True)


parameters = {
    'min' : 20,
    'tagged' : errorType,
    'sort' : 'votes',
    'fromdate' : 1457136000,
    'todate' : date.today(),
    'page_size' : 1,
    'max_pages' : 1,
    'accepted' : True
}
'''

response = requests.get('https://api.stackexchange.com/2.3/search/advanced?page=1&pagesize=1&order=desc&sort=activity&accepted=True&tagged=python&title='+error+'&site=stackoverflow')

test = response.json()

print(test)
'''
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())
'''

'''
def get_value(listOfDicts, key):
    for subVal in listOfDicts:
        if key in subVal:
            return subVal[key]

result = get_value(listOfDicts, 'backoff')
'''
