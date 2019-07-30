import request
import argparse
import sys

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help='the url', metavar='URL', required=True)
    parser.add_argument('-i', '--serverid', help='the server id', metavar='ID', required=True)
    parser.add_argument('-s', '--settings', help='additional server settings (colon separated)', metavar='SETTINGS', required=False)
    args = parser.parse_args()

    url = args.url
    serverId = args.serverid
    settings = args.settings

    args = {
        'serverId': serverId
    }

    if settings is not None:
        args['settings'] = settings

    res = request.post(url + '/runparsec', args)
    request.print_response(res)

if __name__ == "__main__":
    sys.exit(main())