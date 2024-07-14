# TollGuru API Parameter Examples

This repository provides examples of how to interact with the TollGuru API. The TollGuru API offers a comprehensive suite of tools for calculating toll costs for various routes and vehicles, providing accurate and efficient toll pricing information. This guide will help you understand how to use the provided examples to integrate toll calculations into your applications.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Additional Resources](#additional-resources)

## Project Description

The TollGuru API allows developers to calculate toll costs for different routes based on vehicle parameters and toll policies. This API is useful for various applications, including fleet management, trip planning, and logistics. With support for different vehicle types and configurations, the API provides flexible and accurate toll calculation.

Key features include:
- **Route Calculation**: Determine toll costs for specified routes.
- **Vehicle Parameterization**: Customize calculations based on vehicle type, fuel cost, tag cost, and more.
- **Multi-Route Support**: Compare toll costs for multiple routes to find the most cost-effective path.

For a comprehensive overview of the TollGuru API, please visit the [TollGuru API Documentation](https://www.tollguru.com/toll-api-docs).

## Installation

To use the examples in this repository, clone the repo to your local machine and install the necessary dependencies.

```bash
git clone https://github.com/mapup/tollguru-api-parameter-examples.git
cd tollguru-api-parameter-examples
npm install
```

## Usage

The repository includes several example scripts that demonstrate how to interact with the TollGuru API. Each example showcases different functionalities of the API.

### Example: Calculate Toll Costs

```javascript
const axios = require('axios');

const calculateToll = async () => {
  const response = await axios.post('https://api.tollguru.com/v1/calc/route', {
    source: {
      lat: 37.7749,
      lng: -122.4194
    },
    destination: {
      lat: 34.0522,
      lng: -118.2437
    },
    vehicleType: "2AxlesAuto",
    departure_time: "2023-08-01T12:00:00Z"
  }, {
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': 'YOUR_API_KEY'
    }
  });

  console.log(response.data);
};

calculateToll();
```

Replace `'YOUR_API_KEY'` with your actual API key. This example demonstrates how to calculate toll costs for a route between San Francisco and Los Angeles for a 2-axle automobile.

### Example: Vehicle Parameters

```javascript
const axios = require('axios');

const getVehicleParameters = async () => {
  const response = await axios.get('https://api.tollguru.com/v1/vehicle-types', {
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': 'YOUR_API_KEY'
    }
  });

  console.log(response.data);
};

getVehicleParameters();
```

### Example: Route Preferences

```javascript
const axios = require('axios');

const calculatePreferredRoute = async () => {
  const response = await axios.post('https://api.tollguru.com/v1/calc/route', {
    source: {
      lat: 40.7128,
      lng: -74.0060
    },
    destination: {
      lat: 34.0522,
      lng: -118.2437
    },
    vehicleType: "2AxlesAuto",
    departure_time: "2023-08-01T12:00:00Z",
    preferred_routes: ["fastest", "shortest"]
  }, {
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': 'YOUR_API_KEY'
    }
  });

  console.log(response.data);
};

calculatePreferredRoute();
```

## Features

- **Route Calculation**: Calculate the toll costs for a given route.
- **Vehicle Parameterization**: Customize toll calculations based on vehicle types and configurations.
- **Multi-Route Support**: Compare toll costs for multiple routes.

For more detailed examples, refer to the scripts provided in this repository.

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

For a comprehensive overview and additional details, refer to the following sections of the [TollGuru API Documentation](https://www.tollguru.com/toll-api-docs):

- [API Overview](https://www.tollguru.com/toll-api-docs#api-overview)
- [Authentication](https://www.tollguru.com/toll-api-docs#authentication)
- [Endpoints and Parameters](https://www.tollguru.com/toll-api-docs#endpoints-and-parameters)
  - [Calculate Toll Costs](https://www.tollguru.com/toll-api-docs#calculate-toll-costs)
  - [Vehicle Types](https://www.tollguru.com/toll-api-docs#vehicle-types)
  - [Route Preferences](https://www.tollguru.com/toll-api-docs#route-preferences)
- [Response Structure](https://www.tollguru.com/toll-api-docs#response-structure)
- [Error Handling](https://www.tollguru.com/toll-api-docs#error-handling)
- [FAQ](https://www.tollguru.com/toll-api-docs#faq)
