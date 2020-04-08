'''

асинхронность

работа одновременно одного экзмепляра функции

user put number

async function starts X times
function counts from 0 to X
between starts 0.5 seconds
'''
import asyncio


async def print_counter(x: int):
    for number in range(x):
        print(number)
        await asyncio.sleep(.5)
"""
def start(x: int):
    for _ in range(x):
        print_counter(x)

start(2) # sync calls and work

фритинг работает с потоками системы у него больше требований к безопасности системы (на уровне байтов, блокировок) но и ресурсов больше затрагивается
асинк - симуляция, нет проблем с безопасностью по перемещению к асинхронным функциям

синхронность это порядковость выполнения
асинхронность это беспорядочное выполнение

глобальные в рамках одного модуля - будут меняться
глобальные другие - нет, их можно будет только читать

если фукнция выполняется дольше чем 1 с, то она будет асинхронной
если иначе, то синхронная
"""
async def start(x: int):
    coroutines = []

    for _ in range(x):
        coroutines.append( # для того чтобы Питон положил задачи в некий ящик (коробку) чтобы потом разом запустить
            asyncio.create_task(print_counter(x))
        )
    await asyncio.wait(coroutines) # ожидание на запуск на выполнение для корректной работы надо сказать куда возвращаться после запуска очередной

user_count = int(input("Enter your number "))
asyncio.run(start(user_count))