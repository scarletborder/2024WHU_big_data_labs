import grpc
from concurrent import futures
import proto.ett_pb2 as example_pb2
import proto.ett_pb2_grpc as example_pb2_grpc
from logic import send_logic, stop_logic, test_logic


class ExampleService(example_pb2_grpc.ExampleServiceServicer):
    def GetExample(self, request, context):
        return example_pb2.ExampleResponse(message=f"Hello, {request.id}!")

    def Test(self, request, context):
        return test_logic.test_logic(request, context)

    def Send(self, request, context):
        return send_logic.Send_Logic(request, context)

    def Stop(self, request, context):
        return example_pb2.StandardResponse(result="success", msg="success")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_ExampleServiceServicer_to_server(ExampleService(), server)
    server.add_insecure_port("[::]:50051")
    print("gRPC server is running on port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
