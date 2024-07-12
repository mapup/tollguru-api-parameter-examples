# TollTally - GPS Tracks CSV Upload

The `/gps-tracks-csv-upload` endpoint calculates route details, toll information, fuel expenses, etc., about a particular route using its GPS points uploaded as CSV file.

This endpoint takes in a CSV file as input. The JSON files present in this directory represent the query parameters that are sent in the URL along with the uploaded file.

To make it easier to generate a request with these sample query parameters, we have provided utility scripts in the `scripts/` folder written for both Python and Node.js. For example, a `cURL` request for the `01-sync-upload-for-small-files.json` file can be generated by running `python scripts/convert_json_params_to_curl.py 01-sync-upload-for-small-files.json out.txt`

## Downloading Responses for Async Requests

For requests made to this endpoint with `isAsync` set to `true`, typically for large files, the response will contain a `requestId`. This `requestId` parameter can be used to make a `POST` request against the `/gps-tracks-csv-download` endpoint to download the processed result when it is done, which would look something like this:

```json
{
    "requestId": "<YOUR_REQUEST_ID>"
}
```

Some examples on the different ways a request to this endpoint can be customized are as follows:

| ID | Name                                      | Request                                        | Response                                      |
|----|-------------------------------------------|------------------------------------------------|-----------------------------------------------|
| 01 | Sync Upload for Small Files               | [View](./01-sync-upload-for-small-files.json) | [View](../../responses/03-TollTally-GPS-Tracks-To-Toll/01-sync-upload-for-small-files.json) |
| 02 | Async Upload for Large Files              | [View](./02-async-upload-for-large-files.json) | [View](../../responses/03-TollTally-GPS-Tracks-To-Toll/02-async-upload-for-large-files.json) |
| 03 | Specify Currency                         | [View](./03-specify-currency.json) | [View](../../responses/03-TollTally-GPS-Tracks-To-Toll/03-specify-currency.json) |
| 04 | Specify Map Provider                  | [View](./04-specify-map-provider.json) | [View](../../responses/03-TollTally-GPS-Tracks-To-Toll/04-specify-map-provider.json) |
| 05a | Specify Vehicle Type                     | [View](./05a-specify-vehicle-type.json) | [View](../../responses/03-TollTally-GPS-Tracks-To-Toll/05a-specify-vehicle-type.json) |
| 05b | Height-Based Toll                        | [View](./05b-height-based-toll.json) | [View](../../responses/03-TollTally-GPS-Tracks-To-Toll/05b-height-based-toll.json) |
| 05c | Weight-Based Toll                        | [View](./05c-weight-based-toll.json) | [View](../../responses/03-TollTally-GPS-Tracks-To-Toll/05c-weight-based-toll.json) |
| 06a | Specify Fuel Cost                        | [View](./06a-specify-fuel-cost.json) | [View](../../responses/03-TollTally-GPS-Tracks-To-Toll/06a-specify-fuel-cost.json) |
| 06b | Specify Fuel Efficiency                  | [View](./06b-specify-fuel-efficiency.json) | [View](../../responses/03-TollTally-GPS-Tracks-To-Toll/06b-specify-fuel-efficiency.json) |
