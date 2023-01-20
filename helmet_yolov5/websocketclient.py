import asyncio
import websockets


async def main():
    # Connect to the websocket server
    uri = "ws://0.0.0.0:8765"
    async with websockets.connect(uri) as websocket:
        # Continuously send messages to the server
        while True:
            # Read a message from the user


            # Wait for a response from the server
            response = await websocket.recv()
            print(f"Received response: {response}")

asyncio.get_event_loop().run_until_complete(main())