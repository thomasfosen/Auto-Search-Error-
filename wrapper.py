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
        index += 1
        for j in errorLibrary:
            if(i == j + ':'):
                return i, index

errorType, index = checkOutput()
errorMessage = ' '.join(logList[index:])

error = errorType + ' ' + errorMessage

print(error)


''' StackAPI '''

site = StackAPI('stackoverflow')

response = requests.get('https://api.stackexchange.com/2.3/search/advanced?page=1&pagesize=5&order=desc&sort=activity&accepted=True&tagged=python&title='+error+'&site=stackoverflow')

items = response.json()

test = json.dumps(items, indent=4)

#print(test)


def extractURL():
    for item in items:
        print(item)    # Vil bare ha posts med svar
