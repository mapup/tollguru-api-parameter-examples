import os
import urllib.parse
import json

def encode_to_curl(input_file, output_folder, base_url):
    with open(input_file, 'r') as file:
        data = json.load(file)

    def convert_value(value):
        if isinstance(value, bool):
            return str(value).lower()
        return value

    params = "&".join([f"{urllib.parse.quote(str(key))}={urllib.parse.quote(str(convert_value(value)))}" for key, value in data.items()])

    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + '_curl.txt')

    # Add headers here (modify as needed)
    headers = {
        "Content-Type": "text/csv",
        "x-api-key": "{{apiKey}}",
    }

    headers_str = " ".join([f"-H '{key}: {value}'" for key, value in headers.items()])

    with open(output_file, 'w') as file:
        curl_command = f"curl -X POST {base_url}?{params} {headers_str} --data-binary"
        file.write(curl_command)

    print(f"Generated cURL command for {input_file}: {output_file}")

if __name__ == "__main__":
    input_folder = "input-json-with-params"
    output_folder = "output-curl-txts"
    base_url = "https://apis.tollguru.com/toll/v2/gps-tracks-csv-upload"

    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            input_file = os.path.join(input_folder, filename)
            encode_to_curl(input_file, output_folder, base_url)

    print("Conversion complete.")