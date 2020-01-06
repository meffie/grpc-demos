#
# gRPC chat demo client
#
# Threaded, tkinter-based chat client using gRPC to send and recieve messages.
# A background thread reads messages from the server using a streaming gRPC.
# We periodically read the recieve queue with a tk timer, since we can only
# update the UI from the main thread.
#

import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import threading
import queue
import argparse
import logging
import sys
import time
import grpc
import chat_pb2
import chat_pb2_grpc

class ChatClientRPC:
    def __init__(self, hostname, port):
        addr = '{0}:{1}'.format(hostname, port)
        self.channel = grpc.insecure_channel(addr)
        self.stub = chat_pb2_grpc.ChatStub(self.channel)
        self.send_queue = queue.Queue()
        self.recv_queue = queue.Queue()

    def post_message(self, nick, text):
        element = (nick, text)
        self.send_queue.put(element)

    def start(self):
        self.send_thread = threading.Thread(target=self._post_messages)
        self.recv_thread = threading.Thread(target=self._get_messages)
        self.send_thread.start()
        self.recv_thread.start()

    def _post_messages(self):
        while True:
            element = self.send_queue.get()
            try:
                message = chat_pb2.Message(nick=element[0], text=element[1])
                self.stub.PostMessage(message)
            except grpc.RpcError as e:
                logging.error('rpc error {0}: {1}', e.code, e.details)

    def _get_messages(self):
        empty = chat_pb2.Empty()
        while True:
            try:
                for message in self.stub.GetMessages(empty):
                    text = '[{0}]: {1}'.format(message.nick, message.text)
                    self.recv_queue.put(text)
            except grpc.RpcError as e:
                logging.error('rpc error {0}: {1}', e.code, e.details)
            time.sleep(10)

    def get_next_message(self):
        try:
            yield self.recv_queue.get_nowait()
        except queue.Empty:
            pass

class ChatClientApp:
    def __init__(self, root, nick, hostname, port):
        self.root = root
        self.nick = nick
        self.rpc = ChatClientRPC(hostname, port)
        self.create_app()

    def run(self):
        self.rpc.start()
        self._update_messages()
        self.root.mainloop()

    def create_app(self):
        self.root.title('Chat Client')
        frame = tk.Frame(self.root, width=200, height=200)
        frame.pack(fill='both', expand=True)
        self.create_widgets(frame)
        self.root.bind('<Return>', self.post)

    def create_widgets(self, parent):
        self.textarea = scrolledtext.ScrolledText(
                    master=parent,
                    wrap=tk.WORD,
                    height=10)
        self.textarea.pack(padx=10, pady=10, fill='both', expand=True)
        self.entry = tk.Entry(parent)
        self.ok = tk.Button(parent, text='Ok', command=self.post)
        self.entry.pack(padx=10, pady=10, side='left', fill='both', expand=True)
        self.ok.pack(padx=10, pady=10, side='right')
        self.entry.focus_set()
        self.ok.bind('<Button-1>', self.post)

    def post(self, event=None):
        text = self.entry.get().strip()
        if text:
            self.rpc.post_message(self.nick, text)
            self.entry.delete(0, 'end')

    def _update_messages(self):
        for message in self.rpc.get_next_message():
            if not message.endswith('\n'):
                message += '\n'
            self.textarea.insert('end', message)
            self.textarea.see('end')
            self.textarea.update_idletasks()
        self.textarea.after(100, self._update_messages)

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--nick', help='user nickname', default='nickname')
    parser.add_argument('--hostname', help='chat server hostname', default='localhost')
    parser.add_argument('--port', type=int, help='chat server port number', default='8080')
    args = parser.parse_args()
    logging.basicConfig()

    root = tk.Tk()
    app = ChatClientApp(root, args.nick, args.hostname, args.port)
    app.run()

if __name__ == '__main__':
    sys.exit(main())
