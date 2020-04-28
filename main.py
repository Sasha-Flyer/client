import asyncio
import aiohttp
from system_pb2 import SysMessage, BaseMessage
from api import api
import sys


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
        while True:
            msg = await ws.receive()
            if msg.type == aiohttp.WSMsgType.ERROR:
                await ws.close()
                break
            else:
                server_system = parse_message_from_string(msg.data)

                api.emit(server_system)


if __name__ == '__main__':
    ip = "http://127.0.0.1:8080/"
    if sys.argv[1] != "local":
        ip = "http://{0}:8080/".format(sys.argv[1])
    if "cmd_ui" in sys.argv:
        import cmd_ui
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(api, ip))
