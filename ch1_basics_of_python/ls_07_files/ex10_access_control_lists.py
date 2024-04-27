import win32security
import ntsecuritycon as con


def get_file_permissions(filename):
    # Получение объекта безопасности файла
    sd = win32security.GetFileSecurity(filename, win32security.DACL_SECURITY_INFORMATION)
    # Получение DACL (Discretionary Access Control List)
    dacl = sd.GetSecurityDescriptorDacl()

    for i in range(dacl.GetAceCount()):
        ace = dacl.GetAce(i)
        # Получение информации о пользователе/группе
        user_sid = ace[2]
        user_name, _, _ = win32security.LookupAccountSid(None, user_sid)

        print(f"Access for {user_name}:")
        mask = ace[1]
        if mask & con.FILE_READ_DATA:
            print("Read")
        if mask & con.FILE_WRITE_DATA:
            print("Write")
        if mask & con.FILE_EXECUTE:
            print("Execute")
        if mask & con.DELETE:
            print("Delete")


# Пример использования
get_file_permissions("ex04.txt")
