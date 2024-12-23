from model.proto import *
from fastapi import FastAPI, HTTPException
import grpc
import proto.ett_pb2 as example_pb2
import proto.ett_pb2_grpc as example_pb2_grpc
import uvicorn

# 初始化 FastAPI
app = FastAPI()

# 配置 gRPC 客户端
channel = grpc.insecure_channel("localhost:50051")
stub = example_pb2_grpc.ExampleServiceStub(channel)


@app.get("/v1/example/{id}")
async def get_example(id: str):
    try:
        # 转发 HTTP 请求到 gRPC
        grpc_request = example_pb2.ExampleRequest(id=id)
        grpc_response = stub.GetExample(grpc_request)
        return {"message": grpc_response.message}
    except grpc.RpcError as e:
        raise HTTPException(status_code=500, detail=f"gRPC error: {e.details()}")


@app.post("/test")
async def test(request: ETTRequestModel):
    try:
        grpc_request = example_pb2.ETTRequest(
            date=request.date,
            HUFL=request.HUFL,
            HULL=request.HULL,
            MUFL=request.MUFL,
            MULL=request.MULL,
            LUFL=request.LUFL,
            LULL=request.LULL,
            OT=request.OT,
        )
        grpc_response = stub.Test(grpc_request)
        return {"result": grpc_response.result, "msg": grpc_response.msg}
    except grpc.RpcError as e:
        raise HTTPException(status_code=500, detail=f"gRPC error: {e.details()}")


@app.post("/send")
async def send(request: ETTRequestModel):
    """
    Handles POST requests to /send and forwards them to the gRPC server.
    """
    try:
        grpc_request = example_pb2.ETTRequest(
            date=request.date,
            HUFL=request.HUFL,
            HULL=request.HULL,
            MUFL=request.MUFL,
            MULL=request.MULL,
            LUFL=request.LUFL,
            LULL=request.LULL,
            OT=request.OT,
        )
        grpc_response = stub.Test(grpc_request)
        return {"result": grpc_response.result, "msg": grpc_response.msg}
    except grpc.RpcError as e:
        raise HTTPException(status_code=500, detail=f"gRPC error: {e.details()}")


# 运行 FastAPI 应用
uvicorn.run(app, host="0.0.0.0", port=8081)
