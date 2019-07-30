import request
import argparse
import sys

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help='the url', metavar='URL', required=True)
    args = parser.parse_args()

    url = args.url

    res = request.get(url + '/processlist')
    request.print_response(res)

if __name__ == "__main__":
    sys.exit(main())
