from subprocess import Popen, PIPE, STDOUT


filePath = ' /Users/thomasfosen/Documents/Prosjekter/autoError/Auto-Search-Error-/error.py'


process = Popen('python3' + filePath , stdout = PIPE, stderr = STDOUT, shell = True)
stdout, stderr = process.communicate()

consoleMessage = stdout.decode('utf-8')

'''
output = process.stdout.readline()
output2 = process.stdout.readline()

error = process.stderr.readline()
error1 = error.decode('utf-8')
'''
#output2 = process.stderr.readline()

print(consoleMessage)
