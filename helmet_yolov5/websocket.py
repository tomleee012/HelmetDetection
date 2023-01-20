import asyncio
import websockets
import json
from val import helmet_status
import sys
# from detect import queue
# Define a handler function that will be called when a client connects

async def handle_connection(websocket, path):
    # Continuously send messages to the client every 10 seconds
    while True:
        # Send a message to the client
        # my_dict=helmet_status[0]
        my_dict = update()
        json_str = json.dumps(my_dict)
        await websocket.send(json_str)

        # Wait for 10 seconds before sending the next message
        await asyncio.sleep(0.1)

# Start the server on localhost, port 8765
import errno
def update():
    queueAll=[Queue.get() for i in range(Queue.qsize())]
    if len(queueAll)==0:
        return {"status":True}
    else:
        return queueAll[-1]
def start_ws_server(queue,handle_connection:callable = handle_connection)->any:
    global Queue
    Queue=  queue
    print('1111111111111111111111111111111')

    try:
        
        server = websockets.serve(handle_connection, "0.0.0.0", 8765)

        asyncio.get_event_loop().run_until_complete(server)
        asyncio.get_event_loop().run_forever()
        return True
    except OSError as e:
        if e.errno == errno.EADDRINUSE:
            print("Error: Port 8765 is already in use, start websocket failed, exit program")
            sys.exit()
            # return server_protocol 
        else:
            raise


# if __name__ == "__main__":

#     wsServer=start_ws_server()
    # server = websockets.serve(handle_connection, "0.0.0.0", 8765)

    # asyncio.get_event_loop().run_until_complete(server)
    # asyncio.get_event_loop().run_forever()
