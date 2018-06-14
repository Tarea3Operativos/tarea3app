import os
import requests

api_url_base = 'http://localhost:9999/1.0'
headers = {'Content-Type': 'application/json'}


class user:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.superAdmin = False

class folder:
    def __init__(self):
        self.name = ''
        self.repoUserId = ''
        self.edit = True
        self.view = True
        self.delete = True
        self.add = True


if __name__ == '__main__':
    userLogged = user()
    repos = os.system('cd repositorio')
    if repos == 512:
        os.system('mkdir repositorio')
        newUser = user()
        newUser.username = input("Ingrese un nombre del super usuario:")
        newUser.password = input("Ingrese una contrasena:")
        data = requests.post(api_url_base + '/repoUsers/createUser',
                             data={'username': newUser.username, 'password': newUser.password, 'superAdmin': True})
    while True:

        print("Bienvenido al sistema de repos", userLogged.username)
        while userLogged.username != '':
            if userLogged.superAdmin == True:
                action = input("Que desea hacer super admin? A.Asignar permisos U.Usuarios C.Carpetas CS.Cerrar sesion=>").upper()
                if action == 'U':
                    data = requests.get(api_url_base + '/repoUsers/getUsers', headers=headers)
                    respuesta = data.json()
                    print('USUARIOS: ')
                    print(respuesta['response'])
                if action == 'CS':
                    userLogged.username = ''
                if action == 'C':
                    print('Carpetas: ')
                    os.system('ls repositorio/')
                if action == 'A':
                    data = requests.get(api_url_base + '/repoUsers/getUsers', headers=headers)
                    respuesta = data.json()
                    print('USUARIOS: ')
                    print(respuesta['response'])
                    print('FOLDERS: ')
                    os.system('ls repositorio/')
                    username = input('Ingrese un nombre de usuario valido')
                    folderName = input('Ingrese un nombre de carpeta valido')
                    delete = input('Puede eliminar? 1.True o 2.False')
                    edit = input('Puede editar 1.True o 2.False')
                    add = input('Puede agregar? 1.True o 2.False')
                    view = input('Puede ver? 1.True o 2.False')
                    data = requests.post(api_url_base + '/folders/addFolder', data={'name': folderName, 'username': userLogged.username, 'delete': delete, 'edit': edit, 'add': add, 'view': view})


            if userLogged.superAdmin == False:
                print('Carpetas: ')
                os.system('ls repositorio/')
                nombreCarpeta = input("Cual carpeta desea modificar")
                data = requests.get(api_url_base + '/folders/validatePermission/'+nombreCarpeta+'/'+userLogged.username, headers=headers)

                respuesta = data.json()
                print(respuesta['response'])
                if respuesta['errors'] == True:
                    print('No tienes permisos para gestionar esta carpeta')
                if respuesta['errors'] == False:

                    if respuesta['response']['delete'] == True:
                        print('')
                    action = input("Que desea hacer? U.Update V.Ver C.Commit A.Asignar usuario E.Eliminar C.Cerrar sesion A.Agregar M.Modificar=>").upper()
                    if action == 'V':
                        os.system('ls repositorio/' + userLogged.username + '/temporal/')
                        nombreArchivo = input('Cual archivo desea ver? => ')
                        os.system('cat repositorio/' + userLogged.username + '/temporal/' + nombreArchivo)
                    if action == 'C':
                        userLogged.username = ''
                    if action == 'M':
                        os.system('ls repositorio/' + userLogged.username + '/temporal/')
                        nombreArchivo = input('Cual archivo desea modificar? => ')
                        os.system('edit repositorio/' + userLogged.username + '/temporal/'+nombreArchivo)
                    if action == 'A':
                        nombreArchivo = input("Digite el nombre del nuevo archivo=>")
                        os.system('touch repositorio/' + userLogged.username + '/temporal/'+nombreArchivo+'.txt')
                    if action == 'U':
                        tipo = input('1.Restaurar toda la capeta 2.Algun archivo en especifico')


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
                userLogged.superAdmin = respuesta['response']['superAdmin']

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
                nombreCarpeta = input('Digite el nombre de la carpeta=>')
                carpeta = os.system('cd repositorio/'+nombreCarpeta)
                if carpeta == 512:
                    os.system('mkdir repositorio/' + nombreCarpeta)
                    os.system('mkdir repositorio/' + nombreCarpeta + '/permanente')
                    os.system('mkdir repositorio/' + nombreCarpeta + '/temporal')
                    os.system('mkdir repositorio/' + nombreCarpeta + '/permanente/commits')
                if carpeta == 0:
                    while carpeta == 0:
                        nombreCarpeta = input('Ya existe una carpeta con ese nombre, digite otro=>')
                        carpeta = os.system('cd repositorio/' + nombreCarpeta)
                        if carpeta == 512:
                            os.system('mkdir repositorio/' + nombreCarpeta)
                            os.system('mkdir repositorio/' + nombreCarpeta + '/permanente')
                            os.system('mkdir repositorio/' + nombreCarpeta + '/temporal')
                            os.system('mkdir repositorio/' + nombreCarpeta + '/permanente/commits')
                data = requests.post(api_url_base + '/folders/addFolder', data={'name': nombreCarpeta, 'username': userLogged.username, 'delete': '1', 'edit': '1', 'add': '1', 'view': 1 })


