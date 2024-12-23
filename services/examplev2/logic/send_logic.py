import proto.ett_pb2 as example_pb2
import proto.ett_pb2_grpc as example_pb2_grpc

def send_entry(data):
    print(data)

def Send_Logic(request, context):
    send_entry(request)
    return example_pb2.StandardResponse(result="success", msg="success")