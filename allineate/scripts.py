#!/usr/bin/env python3

import argparse
import logging
import sys
from signal import signal, SIGPIPE, SIG_DFL
import os.path

# Get the version:
version = {}
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'version.py')) as f: exec(f.read(), version)

# Handle broken pipes:
signal(SIGPIPE, SIG_DFL) 

# A function to set up logging:
def setupLog(verbosity):
    log = logging.getLogger()
    log_handler = logging.StreamHandler()
    log.default_msec_format = ''
    log_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
    log.setLevel(verbosity.upper())
    log.addHandler(log_handler)
    return log

# A function to quit with an error:
def error(log, msg, exit_code=1):
    log.error(msg)
    exit(exit_code)

def allineate():
    # Set the global defaults:
    defaults = {'verbose':'warning', 'delimiter':'|', 'padding':' ', 'sort':'none'}
    # Set up the commandline:
    parser = argparse.ArgumentParser(description='Align lines in a file by the first occurrence of a given substring')
    parser.add_argument('-V', '--version', action='version', version='%(prog)s {0}'.format(version['__version__']))
    parser.add_argument('-v', '--verbose', dest='verbose', default=defaults['verbose'], choices=['error', 'warning', 'info', 'debug'], help='Set logging level (default {verbose})'.format(**defaults))
    parser.add_argument('-d', '--delimiter', dest='delimiter', metavar='<s>', default=defaults['delimiter'], help='Delimiter string (default "{delimiter}")'.format(**defaults))
    parser.add_argument('-p', '--padding', dest='padding', metavar='<s>', default=defaults['padding'], help='padding character (default "{padding}")'.format(**defaults))
    parser.add_argument('-e', '--include-empty', dest='empty', action='store_true', help='return non-matching lines')
    parser.add_argument('-s', '--sort', dest='sort', default=defaults['sort'], choices=['none', 'lhs', 'rhs'], help='Sort output by string length (default "{sort}")'.format(**defaults))
    parser.add_argument(dest='search_seq', metavar='<s>', help='substring to align on')
    parser.add_argument(dest='input_file', metavar='<file>', nargs='?', help='input file to process')
    args = parser.parse_args()
    
    #Set up logging:
    log = setupLog(args.verbose)

    # Check the inputs:
    if len(args.padding) == 0:
        log.debug('using empty padding charcater')
    if len(args.padding) > 1:
        log.warning('clipping multiple-character padding string "{}" to "{}"'.format(args.padding, args.padding[0]))
        args.padding = args.padding[0]
    log.info('using padding character "{}"'.format(args.padding))
    log.info('using delimiter string "{}"'.format(args.delimiter))

    # Set up the input file:
    if args.input_file is None:
        log.info('reading input from stdin')
        input_handle = sys.stdin
    else:
        try: input_handle = open(args.input_file, 'rt')
        except: error(log, 'failed to open input file {}'.format(args.input_file))
        else: log.info('reading input from {}'.format(args.input_file))

    # Extract the search sequence:
    search_seq = args.search_seq    
    log.info('aligning on the first occurence of string "{}"'.format(search_seq))

    # Iterate through the file:
    lines = []
    maxlen_lhs = 0
    maxlen_rhs = 0
    for line in input_handle.readlines():
        line = line.strip()
        len_lhs = line.find(search_seq)
        if len_lhs == -1:
            log.debug('line {} does not contain search sequence'.format(line))
            lines.append((None, 0, 0))
            continue
        len_rhs = len(line) - len_lhs
        maxlen_lhs = max(maxlen_lhs, len_lhs)
        maxlen_rhs = max(maxlen_rhs, len_rhs)
        lines.append((line, len_lhs, len_rhs))

    # Perform sorting if necessary:
    if args.sort == 'lhs':
        log.debug('sorting lines by length of LHS')
        lines.sort(key=lambda x: x[1], reverse=True)
    if args.sort == 'rhs':
        log.debug('sorting lines by length of RHS')
        lines.sort(key=lambda x: x[2], reverse=True)

    # Process and print output:
    pad_chr = args.padding
    sep_chr = args.delimiter
    for line in lines:
        seq = line[0]
        if seq is None:
            if args.empty is True: print('')
            continue
        len_lhs = line[1]
        len_rhs = line[2]
        len_lpad = maxlen_lhs - len_lhs
        len_rpad = maxlen_rhs - len_rhs
        lhs_pad = pad_chr * len_lpad
        rhs_pad = pad_chr * len_rpad
        lhs = seq[:len_lhs]
        rhs = seq[len_lhs:]
        print('{}{}{}{}{}'.format(lhs_pad, lhs, sep_chr, rhs, rhs_pad))
