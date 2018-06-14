import os
import requests

api_url_base = 'http://localhost:9999/1.0'
headers = {'Content-Type': 'application/json'}
payload = {'seeker': '001'}


class user:
    def __init__(self):
        self.username = ''
        self.password = ''

    def user_name(self):
        print(self.name)

if __name__ == '__main__':
    userLogged = user()
    while True:
        print("Bienvenido al sistema de repos", userLogged.username)
        while userLogged.username != '':
            action = input("Que desea hacer? C.Clonar V.Ver U.Commit, A.Asignar usuario =>").upper()

            os.system('node -v')



        action = input("Que deseas hacer? I.Iniciar sesion, R.Registrar usuario =>").upper()
        if action == 'I':
            newUser = user()
            newUser.username = input("Ingrese un nombre de usuario:")
            newUser.password = input("Ingrese una contrasena:")
            data = requests.post(api_url_base + '/repoUsers/login', data={'username': newUser.username, 'password': newUser.password})
            respuesta = data.json()
            if respuesta['errors'] == True:
                print(respuesta['message'])
            if respuesta['errors'] == False:
                userLogged = newUser
        if action == 'R':
            newUser = user()
            newUser.username = input("Ingrese un nombre de usuario:")
            newUser.password = input("Ingrese una contrasena:")
            data = requests.post(api_url_base + '/repoUsers/createUser', data={ 'username': newUser.username, 'password': newUser.password })
            respuesta = data.json()
            if respuesta['errors'] == True:
                print(respuesta['message'])
            if respuesta['errors'] == False:
                userLogged = newUser
                os.system('mkdir Repositories/'+userLogged.username)
                # os.system('git remote add origin git@github.com:roberto2504/'+userLogged.username)

