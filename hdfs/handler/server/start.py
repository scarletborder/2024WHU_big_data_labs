from fastapi import FastAPI
import uvicorn
import threading
import requests
from server.handler import HandlerList, Handler_lock

# a data handler use http to communicate with this server
# the data handler must contains methods below
# POST: http://url/test, body: {"data": "json data"}, returns {"result": "success"} or {"result": "failed"}
# POST: http://url/send, body: {"data": "json data"}, returns {"result": "success"} or {"result": "failed"}
# POST: http://url/stop, body: {}, returns {"result": "success"} or {"result": "failed"}


app = FastAPI()


@app.post("/register")
async def register(data: dict):
    # register the data handler
    url = data.get("url", "")
    if url == "":
        return {"result": "failed", "msg": "url is empty"}
    # test
    test_data = {
        "date": "2018-06-26 19:00:00",
        "HUFL": "10.11400032043457",
        "HULL": "3.5499999523162837",
        "MUFL": "6.183000087738037",
        "MULL": "1.5640000104904177",
        "LUFL": "3.7160000801086426",
        "LULL": "1.462000012397766",
        "OT": "9.56700038909912",
    }
    response = requests.post(url + "/test", json=test_data)
    try:
        response_data = response.json()
        if (
            response_data is None
            or isinstance(response_data, dict) is False
            or response_data.get("result", "failed") != "success"
        ):
            return {"result": "failed", "msg": "test failed"}
    except ValueError as e:
        return {"result": "failed", "msg": "test failed"}

    # store to the handler list
    with Handler_lock:
        HandlerList.append(url)

    return {"result": "success"}


def start_fastapi_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)
