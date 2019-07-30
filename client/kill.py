import request
import argparse
import sys

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help='the url', metavar='URL', required=True)
    parser.add_argument('-p', '--pid', help='the PID', metavar='PID', required=True, type=int)
    args = parser.parse_args()

    url = args.url
    pid = args.pid

    res = request.post(url + '/killprocess', { 'pid': pid })
    request.print_response(res)

if __name__ == "__main__":
    sys.exit(main())
