# GPS Tracks CSV Upload

The `/gps-tracks-csv-upload` endpoint calculates toll information about a particular route using its GPS points uploaded as CSV file. The use cases of this endpoint are as follows:

| Use Case Name | Request File | Response File |
|---------------|--------------|---------------|
| Sync Upload for Small Files | [View File](01-sync-upload-for-small-files.json) | [View File](../responses/gps-tracks-csv-upload/01-sync-upload-for-small-files.json) |
| Async Upload for Large Files | [View File](02-async-upload-for-large-files.json) | [View File](../responses/gps-tracks-csv-upload/02-async-upload-for-large-files.json) |
| Currency Change | [View File](03-currency-change.json) | [View File](../responses/gps-tracks-csv-upload/03-currency-change.json) |
| Change Mapping Provider | [View File](04-change-mapping-provider.json) | [View File](../responses/gps-tracks-csv-upload/04-change-mapping-provider.json) |
| Change Vehicle Type | [View File](05a-change-vehicle-type.json) | [View File](../responses/gps-tracks-csv-upload/05a-change-vehicle-type.json) |
| Height-Based Toll | [View File](05b-height-based-toll.json) | [View File](../responses/gps-tracks-csv-upload/05b-height-based-toll.json) |
| Weight-Based Toll | [View File](05c-weight-based-toll.json) | [View File](../responses/gps-tracks-csv-upload/05c-weight-based-toll.json) |
| Change Fuel Cost | [View File](06a-change-fuel-cost.json) | [View File](../responses/gps-tracks-csv-upload/06a-change-fuel-cost.json) |
| Change Fuel Efficiency | [View File](06b-change-fuel-efficiency.json) | [View File](../responses/gps-tracks-csv-upload/06b-change-fuel-efficiency.json) |
| Receive EV Locations on the Route | [View File](07-receive-ev-locations-on-the-route.json) | [View File](../responses/gps-tracks-csv-upload/07-receive-ev-locations-on-the-route.json) |

For more details on each use case, refer to the respective JSON files in the [request-bodies](request-bodies/gps-tracks-csv-upload) and [responses](responses/gps-tracks-csv-upload) folders.
| GPS Tracks Test Case | [gps-tracks-test-case.csv](./gps-tracks-test-case.csv) | N/A (No specific response file for CSV upload) |
