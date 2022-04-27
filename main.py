#!/usr/bin/env python3

"""
Simple Server Utility - CLI

Accepts the input from the terminal.
"""

import argparse
import logging
import sys

logging.getLogger().setLevel(logging.DEBUG)

argument_parser = argparse.ArgumentParser(description = "GSSU: Simple Server Utility")

argument_parser.add_argument(
    "address",
    metavar = "a",
    type = str,
    help = f"The address at which the server will listen for traffic.",
    nargs = "?"
)

argument_parser.add_argument(
    "port",
    metavar = "p",
    type = int,
    help = f"The port at which the server will listen for traffic.",
    nargs = "?"
)

argument_parser.add_argument(
    "verbose",
    metavar = "v",
    type = str,
    help = f'Whether or not to log "unnecessary" messages. (expects y or n)',
    nargs = "?"
)

argument_parser.add_argument(
    "buffer",
    metavar = "b",
    type = int,
    help = f"Buffer size of packets expected.",
    nargs="?"
)

argument_parser.add_argument(
    "help",
    metavar = "h",
    type = None,
    help = f'Show the help menu. (gssu_showhelp)',
    nargs = "?"
)

def gssu_showhelp():
    logging.info(
"""
Usage: gssu [options]
Options:
\t--address\t\tThe address at which the server should listen.
\t--port\t\tThe port at which the server should listen.
\t--verbose\t\tWhether or not to log "unnecessary" messages. (expects 'y' or 'n')
\t--buffer\t\tThe buffer size to expect.

Options can be abbreviated with the first letter using metavars. (eg., -a for --address)
"""
    )

def main():
    """Entry-point function for GSSU."""
    args = argument_parser.parse_args()
    addr, port, verbose, buffer_size, help = args.address, args.port, args.verbose, args.buffer, args.help

    if not addr or not port:
        gssu_showhelp()
        sys.exit(1)

    if help:
        gssu_showhelp()
        sys.exit(0)
    if verbose:
        if verbose.lower() not in ('y', 'n'):
            logging.error(f"gssu: expected 'y' or 'n' as --verbose argument; got '{verbose}' instead. ")
            gssu_showhelp()
            sys.exit(1)

    from server import Server

    serv = Server(addr, port, verbose, buffer_size)
    serv.run()
        
if __name__ == "__main__":
    main()
