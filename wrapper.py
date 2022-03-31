from subprocess import Popen, PIPE, STDOUT


filePath = ' /Users/thomasfosen/Documents/Prosjekter/autoError/Auto-Search-Error-/error.py'

errorLibrary = ['NameError', 'IndexError', 'KeyError','IndentationError', 'TypeError', 'ValueError', 'ModuleNotFoundError']

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


errorMessage = logList[index:]
errorMessage = ' '.join(logList[index:])

print(errorType, errorMessage)
