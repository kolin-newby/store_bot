import sys
from amzn_bot import start_amzn_bot
import requests

webhook_url = 'https://discordapp.com/api/webhooks/879585847974969414/4bchq_z8Fyd_Q2D2QqMaoIzMV7C9gPVIJW3O7HxjrZXrRs0rrUwDGzWNAodhwFmp5out'
user_ids = {'ObiWanKnewby': '302872844487098379'}


def main(argv):
    url = str(argv[0])
    trigger_price = float(argv[1])

    message = '<@' + user_ids['ObiWanKnewby'] + \
        '>\nItem successfully purchased!\n[See purchased item below...]'
    error = '0'
    while error != '-1':
        (bought, error) = start_amzn_bot(url, trigger_price)
        if bought:
            break

    if error == '-1':
        message = '<@' + user_ids['ObiWanKnewby'] + \
            '>\nThere was an unexpected error with the bot :(\nNo longer monitoring...'
    else:
        message += '(' + (url) + ')'

    r = requests.request('POST', webhook_url, json={
        "content": message,
        "allowed_mentions": {
            "parse": ["users"]
        }
    }, headers={'Content-Type': 'application/json'})
    print(str(r.status_code) + '/*/' + str(r.content))
    return


if __name__ == '__main__':
    main(sys.argv[1:])
