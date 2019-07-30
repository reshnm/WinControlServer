import request
import argparse
import sys

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help='the url', metavar='URL', required=True)
    parser.add_argument('-t', '--timeout', help='the shutdown timeout', metavar='Seconds', default=0, type=int)
    parser.add_argument('-f', '--force', help='force shutdown', action='store_true', default=False)
    args = parser.parse_args()

    url = args.url
    timeout = args.timeout
    force = args.force

    res = request.post(url + '/shutdown', { 'timeout': timeout, 'force': force })
    request.print_response(res)

if __name__ == "__main__":
    sys.exit(main())
