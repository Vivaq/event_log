import requests
import json
import time
import random

while True:
    response = requests.post(
        'http://localhost:8000/event_log/add_log/',
        random.choice([
            json.dumps({'E': [random.randint(0, 10000),
                              random.choice(['agent', 'user']),
                              str(random.randint(1980, 2016)) +
                              ''.join(['-' + str(random.randint(1, 12)) for a in xrange(0, 2)]),
                              random.choice(['big error', 'DoS', 'unknown']),
                              random.randint(0, 10)]}),
            json.dumps({'LA': [random.randint(0, 10000),
                               random.choice(['agent', 'user']),
                               str(random.randint(1980, 2016)) +
                               ''.join(['-' + str(random.randint(1, 12)) for b in xrange(0, 2)]),
                               random.choice([True, False])]}),
            json.dumps({'CC': [random.randint(0, 10000),
                               random.choice(['agent', 'user']),
                               str(random.randint(1980, 2016)) +
                               ''.join(['-' + str(random.randint(1, 12)) for c in xrange(0, 2)]),
                               random.choice(['changed port', 'all .cgi files changed'])]})
            ]
        )
    )

    print response.text
    time.sleep(10)
