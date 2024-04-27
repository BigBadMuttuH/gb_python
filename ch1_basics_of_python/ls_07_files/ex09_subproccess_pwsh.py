import json
import subprocess


# cmd = 'Get-LocalGroup | ConvertTo-Json'
# process = subprocess.Popen(['powershell', '-command', cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# stdout, stderr = process.communicate()
# if not stderr:
#     groups = json.loads(stdout.decode('cp866'))
#     print(*(group['Name'] for group in groups), sep='\n')
# else:
#     print(stderr.decode('cp866'))

cmd = 'Get-LocalGroupMember "Администраторы" | ConvertTo-Json'
proc = subprocess.Popen(['powershell', '-command', cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = proc.communicate()
if not stderr:
    users = json.loads(stdout.decode('cp866'))
    print(*(f'name:{user['Name'].split('\\')[1]}; SID:{user['SID']['Value']}' for user in users), sep='\n')
else:
    print(stderr.decode('cp866'))
