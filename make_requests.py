import glob
import re
import os
from urllib.parse import urljoin
import urllib.parse
import requests
import json


def convert_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def extract_match(glob_pattern, path):
    # Escape special characters in the glob pattern
    escaped_pattern = re.escape(glob_pattern)

    # Replace the escaped wildcard with a capturing group
    regex_pattern = escaped_pattern.replace("\\*", "(.+?)")

    # Use the regular expression to match the path
    match = re.match(regex_pattern, path)

    if match:
        # Extract the matched part of the path
        extracted_match = match.group(1)
        return extracted_match
    else:
        return None


if __name__ == "__main__":
    api_key = os.environ.get("TOLLGURU_API_KEY")
    assert api_key != None, "TollGuru API key required"

    aliases = {
        "01-Origin-Destination-Cost-Tradeoff": "origin-destination-waypoints",
        "02-Complete-Polyline-To-Toll": "complete-polyline-from-mapping-service",
        "03-TollTally-GPS-Tracks-To-Toll": "gps-tracks-csv-upload",
    }

    base_url = "https://apis.tollguru.com/v2/"
    folder_glob = "request-bodies/*/"
    responses_path = "responses"

    for folder in glob.glob(folder_glob):
        endpoint = aliases[str(extract_match(folder_glob, folder))]
        url = urljoin(base_url, endpoint)

        # if endpoint != "gps-tracks-csv-upload":
        #     continue

        for example in glob.glob(f"{folder}/*.json"):
            out_path = os.path.join(
                responses_path, *os.path.normpath(example).split(os.sep)[1:]
            )
            with open(example, "r+") as f:
                data = f.read()
                print(f"Requesting {example}")
                if len(data) <= 0:
                    print(f"  Skipping {example}")
                    continue

                if endpoint == "gps-tracks-csv-upload":
                    params = json.loads(data)
                    params = "&".join(
                        [
                            f"{urllib.parse.quote(key)}={urllib.parse.quote(str(convert_value(value)))}"
                            for key, value in params.items()
                        ]
                    )
                    with open(
                        "request-bodies/03-TollTally-GPS-Tracks-To-Toll/gps-tracks-test-case.csv",
                        "r",
                    ) as gps_file:
                        response_raw = requests.request(
                            "POST",
                            f"{url}?{params}",
                            headers={
                                "Content-Type": "text/csv",
                                "Accept": "application/json",
                                "x-api-key": api_key,
                            },
                            data=gps_file,
                        )
                else:
                    response_raw = requests.request(
                        "POST",
                        url,
                        headers={
                            "Content-Type": "application/json",
                            "Accept": "application/json",
                            "x-api-key": api_key,
                        },
                        data=data,
                    )

                response = response_raw.json()
                try:
                    del response["meta"]
                except:
                    pass

                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                with open(out_path, "w+") as o:
                    o.write(json.dumps(response, indent=4))

                print(f"  Successfully written {out_path}")
