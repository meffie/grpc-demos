
import argparse
import logging
import sys
import grpc
import chat_pb2
import chat_pb2_grpc


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--host', help='chat host', default='localhost')
    parser.add_argument('--port', type=int, help='port number', default='8080')
    args = parser.parse_args()
    logging.basicConfig()

    addr = '{0}:{1}'.format(args.host, args.port)
    with grpc.insecure_channel(addr) as channel:
        stub = chat_pb2_grpc.ChatStub(channel)

        try:
            message = chat_pb2.Message(nick='tycobb', text='hello world')
            stub.PostMessage(message)
        except grpc.RpcError as e:
            print('rpc error')
            print('details:', e.details())
            print('code:', e.code())

        try:
            empty = chat_pb2.Empty()
            for message in stub.GetMessages(empty):
                print('[{0}]: {1}'.format(message.nick, message.text))
        except grpc.RpcError as e:
            print('rpc error')
            print('details:', e.details())
            print('code:', e.code())

if __name__ == '__main__':
    sys.exit(main())
