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


# 运行 FastAPI 应用
uvicorn.run(app, host="0.0.0.0", port=8964)