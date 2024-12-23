import json
import requests
import threading

HandlerList: list[str] = []
Handler_lock = threading.Lock()


def Send_Data(data):
    with Handler_lock:
        print(f"have {len(HandlerList)} handlers")
        for handler in HandlerList:
            response = requests.post(handler + "/send", json=data)
            try:
                response_data = response.json()
                if (
                    response_data is None
                    or isinstance(response_data, dict) is False
                    or response_data.get("result", "failed") != "success"
                ):
                    return {"result": "failed", "msg": "send failed"}
            except ValueError as e:
                return {"result": "failed", "msg": "send failed"}
    return {"result": "success"}
