import asyncio
from datetime import datetime

import websockets
import time
import json


async def echo_server(websocket):
    async for message in websocket:
        response_dict = {'requestType': 'check state', 'sessionId': 1, 'version': '0.0.1', 'state': 'NEW',
                               'timestamp': datetime.now().strftime('%d/%m/%Y, %H:%M:%S %f')}


        print(f"Received message: {message}")
        message_dict = json.loads(message)

        if message_dict.get('requestType') == 'check state':
            await asyncio.sleep(1)

        if message_dict.get('requestType') == 'create session':
            await asyncio.sleep(1)
            response_dict['state'] = "READY"
            response_dict['requestType'] = "create session"

        if message_dict.get('requestType') == 'send measures':
            await asyncio.sleep(3)
            response_dict['state'] = "READY"
            response_dict['requestType'] = "send measures"

        if message_dict.get('requestType') == 'set state':
            await asyncio.sleep(1)
            state_to_set = message_dict['state']
            response_dict['state'] = state_to_set
            response_dict['requestType'] = "set state"

        await websocket.send(json.dumps(response_dict))



async def main():
    server = await websockets.serve(echo_server, "localhost", 8765)
    print("WebSocket server started")
    await server.wait_closed()

asyncio.run(main())