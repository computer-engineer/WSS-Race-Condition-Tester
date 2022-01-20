#!/usr/bin/python
import sys, concurrent.futures
from functools import partial
from websocket import create_connection

def make_websocket_request(url, data, i):
    ws = create_connection(url) #,http_proxy_host="127.0.0.1", http_proxy_port=8080) # TO DEBUG
    #print(ws.recv())
    ws.send(data)
    ws.close()

def main():
    if len(sys.argv) != 5:
        print ("(+) usage: %s <url> <data> <threads> <number of requests to send>"  % sys.argv[0])
        print ('(+) eg: %s wss://localhost:8000 hello' % sys.argv[0])
        sys.exit(-1)

    #multi: retrieved_value = searchFriends_sqli(ip,  injection_string)
    with concurrent.futures.ThreadPoolExecutor(max_workers=int(sys.argv[3])) as executor: 
        threads = executor.map(partial(make_websocket_request, sys.argv[1], sys.argv[2]),list(range(0, int(sys.argv[4]))))
    
    print("\rNumber of requests sent: %s" % sys.argv[4])

if __name__ == "__main__":
    main()

