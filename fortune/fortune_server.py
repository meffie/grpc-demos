import concurrent.futures
import logging
import grpc
import fortune
import fortune_pb2
import fortune_pb2_grpc

class Fortune(fortune_pb2_grpc.FortuneServicer):

    def __init__(self):
        self.cookies = fortune.CookieFile('fortunes/sample')

    def GetCookie(self, request, context):
        text = self.cookies.pick()
        cookie = fortune_pb2.Cookie(text=text)
        return cookie

def serve():
    tpe = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    server = grpc.server(tpe)
    fortune_pb2_grpc.add_FortuneServicer_to_server(Fortune(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
