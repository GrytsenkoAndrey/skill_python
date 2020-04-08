# Серверное приложение для соединений
"""
К работающему серверу добавить следующий функционал:

    При попытке подключения клиента под логином, который уже есть в чате:
        Отправлять клиенту текст с ошибкой "Логин {login} занят, попробуйте другой"
        Отключать от сервера соединение клиента
        Исправления будут в методе data_received у сервера

    При успешном подключении клиента в чат:
        Отправлять ему последние 10 сообщений из чата
        Создать отдельный метод send_history и вызывать при успешой авторизации в data_received у сервера

    Сдача домашних работ производится через Github.
        Создать аккаунт (если еще нет)
        Загрузить работу в репозиторий
        Проверить, что у него открытый доступ (можете открыть в режиме инкогнито)
        Прикрепить ссылку на репозиторий в форму SkillBox для сдачи работы (Google Формы)


"""
#
# Серверное приложение для соединений
#


import asyncio
from asyncio import transports


class ServerProtocol(asyncio.Protocol):
    login: str = None
    server: 'Server'
    transport: transports.Transport
    mess_list: []

    def __init__(self, server: 'Server'):
        self.server = server

    def sed_history(self):
        pass

    def data_received(self, data: bytes):
        print(data)
        self.mess_list.append(data)

        decoded = data.decode()

        if self.login is not None:
            self.send_message(decoded)
        else:
            if decoded.startswith("login:"):
                self.login = decoded.replace("login:", "").replace("\r\n", "")
                # check if user isset
                for client in self.server.clients:
                    if self.login == client:
                        self.transport.write(f"Логин {self.login} занят, попробуйте другой\n".encode())
                        self.transport.close()
                    else:
                        self.transport.write(f"Привет, {self.login}!\n".encode())
                        self.transport.write("{mess_list[-1:-10]}".encode())
            else:
                self.transport.write("Неправильный логин\n".encode())

    def connection_made(self, transport: transports.Transport):
        self.server.clients.append(self)
        self.transport = transport
        print("Пришел новый клиент")

    def connection_lost(self, exception):
        self.server.clients.remove(self)
        print("Клиент вышел")

    def send_message(self, content: str):
        message = f"{self.login}: {content}\n"

        for user in self.server.clients:
            user.transport.write(message.encode())


class Server:
    clients: list

    def __init__(self):
        self.clients = []

    def build_protocol(self):
        return ServerProtocol(self)

    async def start(self):
        loop = asyncio.get_running_loop()

        coroutine = await loop.create_server(
            self.build_protocol,
            '127.0.0.1',
            8888
        )

        print("Сервер запущен ...")

        await coroutine.serve_forever()


process = Server()

try:
    asyncio.run(process.start())
except KeyboardInterrupt:
    print("Сервер остановлен вручную")
    
    
##################################################################################
#
# import asyncio  # модуль для запуска всех соединений
#
# # опишем наш собственный протокол
# from asyncio import transports
# from typing import Optional
#
#
# class ServerProtocol(asyncio.Protocol):  # подключили (наследовали) подключения, настройки и т.п.
#     login: str = None
#     server: 'Server'
#     transport: transports.Transport
#
#     def __int__(self, server: 'Server'):
#         self.server = server
#
#     def data_received(self, data: bytes):
#         print(data)
#         decoded = data.decode()
#
#         if self.login is not None:
#             self.send_message(decoded)
#         else:
#             if decoded.startswith("login:"):
#                 self.login = decoded.replace("login:", "").replace("\r\n", "")
#                 self.transport.write(
#                     f"Hello, {self.login}!\n".encode()
#                 )
#             else:
#                 self.transport.write("Incorrect login".encode())
#
#     def connection_made(self, transport: transports.Transport):  # отсюда можно читать и писать
#         self.server.clients.append(self)  # добавляем в список наше соединение - клиента
#         self.transport = transport
#         print("New client came")
#
#     def connection_lost(self, exception):  # в случае разрыва соединения
#         self.server.clients.remove(self)  # удаляем клиента из списка
#         print("Client went away")
#
#     def send_message(self, content: str):
#         message = f"{self.login}: {content}\n"
#
#         for user in self.server.clients:
#             user.transport.write(message.encode())
#
#
# class Server:
#     clients: list  # list - это список
#
#     def __init__(self):
#         self.clients = []  # инициализация списка, чтобы при старте всегда был
#
#     def build_protocol(self):
#         return ServerProtocol(self)
#
#     async def start(self):
#         # получаем управление событийным циклом - перехватываем
#         loop = asyncio.get_running_loop()
#
#         coroutine = await loop.create_server(  # создаем сервер в фоне, а вызов await в первом потоке
#             self.build_protocol,  # здесь функцию не вызываем а передаем название
#             '127.0.0.1',
#             8888  # больше 1024 потому что до 1024 все заняты системой
#         )
#         print("Server starts.....")
#         await coroutine.serve_forever()
#
#
# process = Server()
#
# try:
#     asyncio.run(process.start())
# except KeyboardInterrupt:
#     print("Server was stopped manually")

"""
протокол - набора правил и стандартов как и в каком формате передается сообщение
информация передается в виде байт
то есть отправляем байты и принимаем только байты, а что внутри байтов - изображения, строка, числа - не важно

HTTP - нестабильный в качестве передачи данных, но быстрый
TCP  - протокол для частов, более надёжный, если не получилось отправить - попробует ещё раз; если что-то произошло не 
так, то сообщит гарантирует доставку


"""
