#!/usr/bin/env python3

"""
Simple Server Utility - Server Module

Initializes a simple socket server which inspects all the traffic sent to it.
"""
import socket
import logging
import sys

logging.getLogger().setLevel(logging.DEBUG)

class Server:
    """A basic server object which uses TCP sockets."""
    def __init__(self, addr: str = 'localhost', port: int = 8000, verbose: str  = True, buffer_size: int = 2048):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            self.socket.bind((addr, port))
        except Exception as exc:
            logging.error(f"gssu.server.bind: {exc}")
            sys.exit(1)

        self.addr = addr
        self.port = port

        if verbose == 'y':
            self.verbose = True
        elif verbose == 'n':
            self.verbose = False
        
        self.bff_sz = buffer_size

        # addr - The address at which the server should listen.
        # port - The port at which the server should listen.
        # verbose - Use verbose logging.
        # bff_sz - Buffer size.

    def run(self):
        """Run the server by listening on the socket of the address and port provided earlier."""
        if self.verbose:
            logging.info("gssu: server is starting.")

        self.socket.listen()
        if self.verbose:
            logging.info("gssu: server is running.")

        while True:
            try:
                conn, addr = self.socket.accept()
                logging.info(f"gssu: {addr[0]}:{addr[1]} is attempting to establish a connection.")
                with conn:
                    data = conn.recv(self.bff_sz)
                    if not data:
                        logging.warn(f"gssu: {addr} sent no data indicating a disconnect/termination of connection.")
                        logging.info(f"{addr}: {data}")
            except KeyboardInterrupt:
                self.forceclose()
                
    def forceclose(self):
        logging.warn("gssu: force closed. do not repeat this in the future as the socket may go into the TIME_WAIT state and becoming unusable for quite a while, use ^C instead of ^Z.")
        self.socket.close()
        sys.exit(0)
