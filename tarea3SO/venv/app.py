import os
import requests

api_url_base = 'http://localhost:9999/1.0'
headers = {'Content-Type': 'application/json'}


class user:
    def __init__(self):
        self.username = ''
        self.password = ''



if __name__ == '__main__':
    userLogged = user()
    repos = os.system('cd repositorio')
    if repos == 512:
        os.system('mkdir repositorio')
        # print('Aun no existe un carpeta para los repositorios, por favor cree uno :)')
        # newUser = user()
        # newUser.username = input("Ingrese un nombre de usuario")
        # newUser.password = input("Ingrese una contrasena")
        # data = requests.post(api_url_base + '/repoUsers/createUser', data={'username': newUser.username, 'password': newUser.password})
        # respuesta = data.json()
        # if respuesta['errors'] == True:
        #     print(respuesta['message'])
        # if respuesta['errors'] == False:
        #     os.system('mkdir repositorio')
        #     os.system('sudo useradd -m yesy') #+ newUser.username + ' -p ' + newUser.password)
        #     # os.system('icacls "/repositorio" /grant Users:' + newUser.username)
        #     repos = 0
    while True:

        print("Bienvenido al sistema de repos", userLogged.username)
        while userLogged.username != '':
            action = input("Que desea hacer? U.Update V.Ver C.Commit A.Asignar usuario E.Eliminar C.Cerrar sesion A.Agregar M.Modificar=>").upper()
            if action == 'V':
                os.system('ls repositorio/' + userLogged.username + '/temporal/')
                nombreArchivo = input('Cual archivo desea ver? => ')
                os.system('cat repositorio/' + userLogged.username + '/temporal/' + nombreArchivo)
            if action == 'C':
                os.system('cd repositorio/' + userLogged.username + ' git add .')
                os.system('cd repositorio/' + userLogged.username + ' git commit -am "testing"')
                os.system('cd repositorio/' + userLogged.username + ' git push origin master')
            if action == 'M':
                os.system('ls repositorio/' + userLogged.username + '/temporal/')
                nombreArchivo = input('Cual archivo desea modificar? => ')
                os.system('edit repositorio/' + userLogged.username + '/temporal/'+nombreArchivo)
            if action == 'A':
                nombreArchivo = input("Digite el nombre del nuevo archivo=>")
                os.system('touch repositorio/' + userLogged.username + '/temporal/'+nombreArchivo+'.txt')
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
                os.system('mkdir repositorio/'+userLogged.username)
                os.system('mkdir repositorio/'+userLogged.username+'/permanente')
                os.system('mkdir repositorio/' + userLogged.username + '/temporal')
                os.system('mkdir repositorio/' + userLogged.username + '/permanente/commits')


