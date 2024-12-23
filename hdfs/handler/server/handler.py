import requests
import threading

HandlerList: list[str] = []
Handler_lock = threading.Lock()


def Send_Data(data: str):
    with Handler_lock:
        for handler in HandlerList:
            response = requests.post(
                handler + "/send",
                data=data,  # 直接作为字符串传递
                headers={"Content-Type": "application/json"},  # 手动设置请求头
            )
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
