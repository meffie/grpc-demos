from __future__ import print_function
import logging
import grpc
import fortune_pb2
import fortune_pb2_grpc

def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = fortune_pb2_grpc.FortuneStub(channel)
        request = fortune_pb2.Request()
        cookie = stub.GetCookie(request)
        print(cookie.text)

if __name__ == '__main__':
    logging.basicConfig()
    main()
