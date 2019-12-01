
import argparse
import logging
import sys
import grpc
import fortune_pb2
import fortune_pb2_grpc


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--host', help='fortune host', default='localhost')
    parser.add_argument('--port', type=int, help='port number', default='50050')
    parser.add_argument('-c', '--category', help='fortune category')
    parser.add_argument('-l', '--list-categories', action='store_true', help='list fortune categories')
    args = parser.parse_args()
    logging.basicConfig()

    addr = '{0}:{1}'.format(args.host, args.port)
    with grpc.insecure_channel(addr) as channel:
        stub = fortune_pb2_grpc.FortuneStub(channel)
        if args.list_categories:
            try:
                response = stub.ListCategories(fortune_pb2.Empty())
                print('\n'.join(response.categories))
            except grpc.RpcError as e:
                print('rpc error')
                print('details:', e.details())
                print('code:', e.code())
        else:
            try:
                request = fortune_pb2.CookieRequest(category=args.category)
                response = stub.GetCookie(request)
                print(response.cookie)
            except grpc.RpcError as e:
                print('rpc error')
                print('details:', e.details())
                print('code:', e.code())

if __name__ == '__main__':
    sys.exit(main())
