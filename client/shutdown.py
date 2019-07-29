import request
import argparse
import sys

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help='the url', metavar='URL', required=True)
    parser.add_argument('-t', '--timeout', help='the shutdown timeout', metavar='Seconds', default=0, type=int)
    args = parser.parse_args()

    url = args.url
    timeout = args.timeout

    response = request.post(url + '/shutdown', { 'timeout': timeout })
    print(response.json())

if __name__ == "__main__":
    sys.exit(main())
