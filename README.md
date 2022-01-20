# WSS-Race-Condition-Tester
Simple python script to test and exploit race condition vulnerabilities in websockets


## Requirements
1. Python 3
2. Linux/Windows/MAC OSX

## Installation 
```python
pip3 install -r requirements.txt 
```

## Usage
```python
(+) usage: /WSS-Race-Condition-Tester/race-condition-test.py <url> <data> <threads> <number of requests to send>
```

## Example
```python
python3 race-condition-test.py ws://localhost:9000 '{"action":"transfer_balance", "sender":"Alice", "receiver":"Bob", "amount":1}' 20 20
Number of requests sent: 20
```

