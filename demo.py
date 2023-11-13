# datos ej
user = {
    'id': '',
    'user': '',
    'pass': ''
}

persona = {
	'nombre': '',
	'edad': ''
}

progreso = {
    'user': '',
    'problema': '',
    'objetivo': ''
}

consejo = {
    'problema': '',
    'consejo': '',
    'actividad': '',
    'libro': ''
}

list_users = []

for i in range(3):
    usr = f'pepe_{i}'
    list_users.append(usr)

print(list_users)