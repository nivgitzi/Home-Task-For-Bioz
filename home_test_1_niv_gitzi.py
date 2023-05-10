import boto3
import gzip
import json
import base64
from textwrap import dedent



s3 = boto3.client('s3',
                  aws_access_key_id=base64.b64decode("QUtJQTJEUlFGREdLMzM1UVVFSFc=".encode()).decode(),
                  aws_secret_access_key=base64.b64decode("MFVmMEVyc1gyRE9QRGtGVmdGM3FWZmM4T1AwQVRtem9zdjFTcmNZRA==".encode()).decode())

bucket_name = "sample-log-data-028a9a4884211e5c6"
key = "example.log.gz"




#My Code:

with open('/Users/Niv/example.log.gz', 'wb') as f:
    s3.download_fileobj(bucket_name, key, f)


with gzip.open('/Users/Niv/example.log.gz', 'rb') as f:
    file_content = f.read().decode()
    file_content = ''.join((dedent(line)) for line in file_content) #explanation at chatGPT
    #print (file_content)

file_content = (file_content.replace('\n', ''))
print(file_content) #just for check
file_content = (file_content.replace(':', ': '))
file_content = (file_content.replace(',', ', '))


json_strings = []
start_idx = 0
while True:
    start_idx = file_content.find('{', start_idx) #here starts our next string we should read
    if start_idx == -1: #it means that '{' is not found anymore, which means no more strings to read.
        break
    end_idx = start_idx + 1
    stack = ['{']
    while stack: #stack will be empty when found we the "}" which closes the outer "{", then we have our string to append
        if file_content[end_idx] == '{':
            stack.append('{')
        elif file_content[end_idx] == '}':
            stack.pop()
        end_idx += 1
    json_strings.append(file_content[start_idx:end_idx])
    #append only when we found the "}" which closes the outer "{"

    start_idx = end_idx
    #in the next itteration we start from the current endindex,
    #and then in the next 'While True' itteration we will find the next outer "{"
    #which means the starting point of the next string we should read






assert len(json_strings) == 21

first_json_string = json_strings[0]
print(first_json_string) #just for check
assert first_json_string.startswith('{"FleetId": "fleet-xxx", "Errors": []')
assert first_json_string.endswith(', "RetryAttempts": 0}}')

last_json_string = json_strings[-1]
assert last_json_string.startswith('{"Resources": ["i-xxx"]')
assert last_json_string.endswith('"Value": "xxx-78"}]}')

