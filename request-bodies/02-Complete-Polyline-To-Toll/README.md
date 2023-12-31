# Complete Polyline from Mapping Service

The `/complete-polyline-from-mapping-service` endpoint allows users to obtain route details, toll information, fuel expenses, etc., about a particular route by specifying the route's complete polyline as an encoded string or as decoded coordinates.
Some examples for the different ways a request to this endpoint can be customized are as follows:

| ID | Name                                   | Request                                      | Response                                    |
|----|----------------------------------------|----------------------------------------------|---------------------------------------------|
| 01a | Polyline as Encoded String            | [View](./01a-polyline-as-encoded-string.json) | [View](../../responses/02-Complete-Polyline-To-Toll/01a-polyline-as-encoded-string.json) |
| 01b | Polyline as Decoded Path              | [View](./01b-polyline-as-decoded-path.json) | [View](../../responses/02-Complete-Polyline-To-Toll/01b-polyline-as-decoded-path.json) |
| 02a | Polyline with Timestamps              | [View](./02a-polyline-with-timestamps.json) | [View](../../responses/02-Complete-Polyline-To-Toll/02a-polyline-with-timestamps.json) |
| 02b | Path with Timestamps                  | [View](./02b-path-with-timestamps.json) | [View](../../responses/02-Complete-Polyline-To-Toll/02b-path-with-timestamps.json) |
| 03 | Specify Departure Time                 | [View](./03-specify-departure-time.json) | [View](../../responses/02-Complete-Polyline-To-Toll/03-specify-departure-time.json) |
| 04 | Specify Currency                       | [View](./04-specify-currency.json) | [View](../../responses/02-Complete-Polyline-To-Toll/04-specify-currency.json) |
| 05a | Specify Vehicle Type                  | [View](./05a-specify-vehicle-type.json) | [View](../../responses/02-Complete-Polyline-To-Toll/05a-specify-vehicle-type.json) |
| 05b | Height-Based Toll                     | [View](./05b-height-based-toll.json) | [View](../../responses/02-Complete-Polyline-To-Toll/05b-height-based-toll.json) |
| 05c | Weight-Based Toll                     | [View](./05c-weight-based-toll.json) | [View](../../responses/02-Complete-Polyline-To-Toll/05c-weight-based-toll.json) |
| 06a | Specify Fuel Cost                      | [View](./06a-specify-fuel-cost.json) | [View](../../responses/02-Complete-Polyline-To-Toll/06a-specify-fuel-cost.json) |
| 06b | Specify Fuel Efficiency                | [View](./06b-specify-fuel-efficiency.json) | [View](../../responses/02-Complete-Polyline-To-Toll/06b-specify-fuel-efficiency.json) |
| 07 | Receive State Mileage and Toll Distance                  | [View](./07-receive-state-mileage-and-toll-distance.json) | [View](../../responses/02-Complete-Polyline-To-Toll/07-receive-state-mileage-and-toll-distance.json) |
