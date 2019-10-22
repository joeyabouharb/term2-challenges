from base64 import b64decode

encoded = 'NDgtNmYtNmUtNmItMjAtNjktNjYtMjAtNzktNmYtNzUtMjAtNmMtNmYtNzYtNjUtMjAtNDMtMmItMmI='

str_list = b64decode(encoded).decode('utf8').split('-')

hex_list = [int(f"0x{hex_val}", 16) for hex_val in str_list]

msg = bytes(hex_list).decode('utf-8')
print(msg)

