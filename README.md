# Home-Task-For-Bioz



The task is to analyze a log file, and extract all the json strings it contains
The file is in S3
Assume that the log file timestamps can be from any date and time





Starting point:

----------
import base64

aws_access_key_id = base64.b64decode("QUtJQTJEUlFGREdLMzM1UVVFSFc=".encode()).decode()
aws_secret_access_key = base64.b64decode("MFVmMEVyc1gyRE9QRGtGVmdGM3FWZmM4T1AwQVRtem9zdjFTcmNZRA==".encode()).decode()

bucket_name = "sample-log-data-028a9a4884211e5c6"
key = "example.log.gz"


#My code here


assert len(json_strings) == 21

first_json_string = json_strings[0]
assert first_json_string.startswith('{"FleetId": "fleet-xxx", "Errors": []')
assert first_json_string.endswith(', "RetryAttempts": 0}}')

last_json_string = json_strings[-1]
assert last_json_string.startswith('{"Resources": ["i-xxx"]')
assert last_json_string.endswith('"Value": "xxx-78"}]}')

----------
