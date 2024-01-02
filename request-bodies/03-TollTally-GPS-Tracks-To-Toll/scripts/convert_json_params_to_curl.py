import json
import sys
import os
import urllib.parse

def convert_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value

def encode_to_curl(input_file, output_file, base_url):
    with open(input_file, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    params = '&'.join(
        [f"{urllib.parse.quote(key)}={urllib.parse.quote(str(convert_value(value)))}" for key, value in json_data.items()]
    )

    headers = {
        'Content-Type': 'text/csv',
        'x-api-key': '{{apiKey}}',
    }

    headers_str = ' '.join([f"-H '{key}: {value}'" for key, value in headers.items()])

    curl_command = f"curl -X POST {base_url}?{params} {headers_str} --data-binary '@'"

    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(curl_command)

    print(f"Generated cURL command for {input_file}: {output_file}")

# Process command line arguments
if len(sys.argv) < 3:
    print(f"Usage: python {sys.argv[0]} <input-file> <output-file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
base_url = 'https://apis.tollguru.com/toll/v2/gps-tracks-csv-upload'

encode_to_curl(input_file, output_file, base_url)

print('Conversion complete.')

