import subprocess


def get_administrators_powershell(group_name="Администраторы"):
    cmd = f'Get-LocalGroupMember -Group "{group_name}" | Select-Object -ExpandProperty Name'
    process = subprocess.Popen(["powershell", "-Command", cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        print(f"Ошибка: {error.decode('cp866')}")
        return []

    # Декодирование вывода с использованием CP866
    users = [line.strip() for line in output.decode('cp866').split('\n') if line.strip()]
    return users


administrators = get_administrators_powershell()
print("Пользователи группы 'Администраторы':")
for admin in administrators:
    print(admin)
