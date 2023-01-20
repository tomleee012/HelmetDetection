import pytest
from websocket import start_ws_server

def test_start_ws_server():
    server=start_ws_server()
    assert server.is_serving()==True