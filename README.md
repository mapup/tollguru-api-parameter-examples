# TollGuru API Parameter Examples

Sample request and response JSON payloads for the TollGuru Toll API and TollTally endpoints.

## Table of Contents

- [Project Description](#project-description)
- [Repository Structure](#repository-structure)
- [Endpoints](#endpoints)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Additional Resources](#additional-resources)

## Project Description

This repository provides sample JSON request bodies and response payloads for the TollGuru Toll API. Use these examples as a reference when building integrations — each file demonstrates a specific parameter combination or feature of the API.

The examples cover three API endpoints across the TollGuru and TollTally product suite:
- Toll calculation via origin, destination, and waypoints
- Toll calculation via complete polyline (TollTally)
- Toll calculation via GPS track CSV upload (TollTally)

For API authentication and full endpoint documentation, visit the [TollGuru API Documentation](https://www.tollguru.com/toll-api-docs).

## Repository Structure

```
.
├── request-bodies/                            # Sample JSON request payloads, organized by endpoint
│   ├── 01-Origin-Destination-Cost-Tradeoff/
│   ├── 02-Complete-Polyline-To-Toll/
│   └── 03-TollTally-GPS-Tracks-To-Toll/
└── responses/                                 # Corresponding sample JSON responses
    ├── 01-Origin-Destination-Cost-Tradeoff/
    ├── 02-Complete-Polyline-To-Toll/
    └── 03-TollTally-GPS-Tracks-To-Toll/
```

## Endpoints

### 1. Origin-Destination-Cost-Tradeoff

Endpoint: `/origin-destination-waypoints`

Calculates toll costs, route details, and fuel expenses by specifying an origin, destination, and optional waypoints.

[View request examples →](./request-bodies/01-Origin-Destination-Cost-Tradeoff/)

---

### 2. TollTally-Complete-Polyline-To-Toll

Endpoint: `/complete-polyline-from-mapping-service`

Calculates toll costs and route details by providing a route's complete polyline as an encoded string or as decoded coordinates.

[View request examples →](./request-bodies/02-Complete-Polyline-To-Toll/)

---

### 3. TollTally-GPS-Tracks-To-Toll

Endpoint: `/gps-tracks-csv-upload`

Calculates toll costs and route details from GPS points uploaded as a CSV file. Supports both synchronous (small files) and asynchronous (large files) uploads.

[View request examples →](./request-bodies/03-TollTally-GPS-Tracks-To-Toll/)

---

## Usage

Clone the repository and use the JSON files directly as request bodies in your API calls.

```bash
git clone https://github.com/mapup/tollguru-api-parameter-examples.git
cd tollguru-api-parameter-examples
```

### Example: Origin-Destination request using cURL

```bash
curl -X POST <TOLLGURU_API_BASE_URL>/origin-destination-waypoints \
  -H "Content-Type: application/json" \
  -H "x-api-key: YOUR_API_KEY" \
  -d @request-bodies/01-Origin-Destination-Cost-Tradeoff/01-address-as-string.json
```

The request body used (`01-address-as-string.json`):

```json
{
    "from": {
        "address": "Walt Whitman Brg Philadelphia, PA 19148, USA"
    },
    "to": {
        "address": "Ocean City, NJ 08226 USA"
    },
    "vehicle": {
        "type": "2AxlesAuto"
    }
}
```

Replace `YOUR_API_KEY` with your actual TollGuru API key and `TOLLGURU_API_BASE_URL` with the base URL from the [API documentation](https://www.tollguru.com/toll-api-docs#authentication).

### TollTally GPS Tracks

For the `/gps-tracks-csv-upload` endpoint, parameters are sent as query parameters alongside the CSV file upload. Utility scripts are provided to help generate cURL commands from the sample JSON parameter files:

```bash
python request-bodies/03-TollTally-GPS-Tracks-To-Toll/scripts/convert_json_params_to_curl.py \
  01-sync-upload-for-small-files.json out.txt
```

## Contributing

We welcome contributions to this repository! If you have suggestions or improvements, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or support, please reach out to [api-support@tollguru.com](mailto:api-support@tollguru.com).

## Additional Resources

For full API documentation, refer to:

- [API Overview](https://www.tollguru.com/toll-api-docs#api-overview)
- [Authentication](https://www.tollguru.com/toll-api-docs#authentication)
- [Origin-Destination Waypoints](https://www.tollguru.com/toll-api-docs#tolls-between-origin-destination-and-waypoints)
- [TollTally Complete Polyline](https://www.tollguru.com/toll-api-docs#route-encoded-polyline)
- [TollTally GPS Tracks](https://www.tollguru.com/toll-api-docs#tolltally---gps-tracks-to-toll-api)
- [Vehicle Types](https://www.tollguru.com/toll-api-docs#vehicle-types-supported-by-tollguru)
- [Error Handling](https://www.tollguru.com/toll-api-docs#errors-and-troubleshooting)
- [FAQ](https://www.tollguru.com/toll-api-docs#faq)
