import asyncio
import websockets

async def delete_one_error_code():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        
        error_code_delete_one = ("1")
        await websocket.send(error_code_delete_one)
        print(f"> {error_code_delete_one}")

        #confirmation = await websocket.recv()
        #print(f"< {confirmation}")
asyncio.get_event_loop().run_until_complete(delete_one_error_code())
#asyncio.get_event_loop().run_forever()
