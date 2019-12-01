
import argparse
import concurrent.futures
import logging
import os
import sys

import grpc
import fortune
import fortune_pb2
import fortune_pb2_grpc

class Fortune(fortune_pb2_grpc.FortuneServicer):

    def __init__(self, cookie_path, cookie_file):
        filename = os.path.join(cookie_path, cookie_file)
        self.default_file = cookie_file
        self.cookie_files = {}
        for filename in fortune.CookieFile.filenames(cookie_path):
            logging.info('reading cookie file {0}'.format(filename))
            cookie_file = fortune.CookieFile(filename)
            category = os.path.basename(filename)
            self.cookie_files[category] = cookie_file

    def ListCategories(self, request, context):
        logging.info('ListCategories()')
        categories = self.cookie_files.keys()
        response = fortune_pb2.Categories(categories=categories)
        return response

    def GetCookie(self, request, context):
        logging.info('GetCookie(category="{}")'.format(request.category))
        category = request.category
        if not category:
            category = self.default_file
        cookie_file = self.cookie_files.get(category)
        if cookie_file:
            cookie = cookie_file.pick()
            response = fortune_pb2.CookieResponse(cookie=cookie)
        else:
            context.set_details('Unknown category. Try ListCategories() to find categories.')
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            response = fortune_pb2.CookieResponse()
        return response

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--port', type=int, help='port number', default=50050)
    parser.add_argument('--cookie-path', help='path to fortune files', default='./fortunes')
    parser.add_argument('--cookie-file', help='default fortune file', default='quotes')
    parser.add_argument('--threads', type=int, help='number of worker threads', default=10)
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

    fortune = Fortune(args.cookie_path, args.cookie_file)
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=args.threads)
    server = grpc.server(executor)
    fortune_pb2_grpc.add_FortuneServicer_to_server(fortune, server)
    addr = '[::]:{0}'.format(args.port)
    logging.info('listening on port {0}'.format(args.port))
    server.add_insecure_port(addr)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    sys.exit(main())
