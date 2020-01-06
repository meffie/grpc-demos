
import argparse
import concurrent.futures
import logging
import sys
import time

import grpc
import chat_pb2
import chat_pb2_grpc

class Chat(chat_pb2_grpc.ChatServicer):

    def __init__(self):
        pass

    def PostMessage(self, request, context):
        logging.info('PostMessage(): nick="{0}", text="{1}"'\
            .format(request.nick, request.text))
        return chat_pb2.Empty()

    def GetMessages(self, request, context):
        n = 10
        for i in range(1, n+1):
            time.sleep(2)
            text = 'message {0} of {1}'.format(i, n)
            message = chat_pb2.Message(nick='tycobb', text=text)
            yield message
            #time.sleep(1)

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--port', type=int, help='port number', default=8080)
    parser.add_argument('--threads', type=int, help='number of worker threads', default=10)
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

    chat = Chat()
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=args.threads)
    server = grpc.server(executor)
    chat_pb2_grpc.add_ChatServicer_to_server(chat, server)
    addr = '[::]:{0}'.format(args.port)
    logging.info('listening on port {0}'.format(args.port))
    server.add_insecure_port(addr)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    sys.exit(main())
