import sys, json
data = json.loads(sys.stdin.read())
print(data['data']['data'][sys.argv[1]])
