import subprocess

# ps_script = f"""
# Get-WinEvent -LogName System -MaxEvents 10
# """
#
# result = subprocess.run(["PowerShell", "-Command", ps_script], capture_output=True, text=True)
# print(result.stdout)
#

cmd_script = "systeminfo"

r = subprocess.run(["cmd", "/C", cmd_script], capture_output=True)
output = r.stdout.decode('cp866')
print(output)
