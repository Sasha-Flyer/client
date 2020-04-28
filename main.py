import asyncio
import aiohttp
from system_pb2 import SysMessage, BaseMessage
from signaller import Signal, autoconnect
from api import api
import cmd_ui


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


async def main(api):
    session = aiohttp.ClientSession()
    async with session.ws_connect('http://188.134.86.16:8080/') as ws:
        while True:
            msg = await ws.receive()
            if msg.type == aiohttp.WSMsgType.ERROR:
                await ws.close()
                break
            else:
                server_system = parse_message_from_string(msg.data)

                api.emit(server_system)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(api))


