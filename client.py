import asyncio
import aiohttp
from system_pb2 import SysMessage, BaseMessage
from api import api
import sys
import threading
import socket


def parse_message_from_string(bytes):
    message_params = dict()
    message = BaseMessage()
    message.ParseFromString(bytes)

    if message.type == "SYS_MESSAGE":
        message = SysMessage()
        message.ParseFromString(bytes)
        message_params['used_memory'] = message.used_memory
        message_params['total_memory'] = message.total_memory
        message_params['cpu_usage'] = message.cpu_usage
        message_params['ssd_usage'] = message.ssd_usage

    return message_params


async def main(api, ip):
    session = aiohttp.ClientSession()
    async with session.ws_connect(ip) as ws:
        try:
            from wx_ui import main_wx
            thread = threading.Thread(target=main_wx)
            thread.start()
            while True:
                msg = await ws.receive()
                if msg.type == aiohttp.WSMsgType.ERROR:
                    await ws.close()
                    break
                else:
                    server_system = parse_message_from_string(msg.data)
                    api.emit(server_system)
        except Exception as e:
            await ws.close()
            raise e

def runserver():
    print("Введите ip-адресс сервера. Пустое значение означает локальный адрес:")
    ip = input()
    if ip == "":
        ip = "127.0.0.1"
    print("Введите порт сервера:")
    port = input()
    server = "http://{0}:{1}/".format(ip, port)

    import cmd_ui
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(api, server))
    except (aiohttp.client_exceptions.WSServerHandshakeError, aiohttp.client_exceptions.ClientConnectorError, socket.gaierror) as e:
        print("ip адрес или порт указаны неверно. Перезапустите приложение и попробуйте снова")
        input()


if __name__ == '__main__':
    runserver()
