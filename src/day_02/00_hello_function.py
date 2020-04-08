
def user_hello(user: str):
    print(f"Hello, {user}")

clients = ['Nick', 'David', 'Andy', 'Pawel', 'Mateusz']

for user in clients:
    user_hello(user)

clients_two = ['Chak']
for user in clients_two:
    user_hello(user)

