# Where the data comes from

The data is the NYC TLC Trip Record Data, published monthly by the New York City Taxi and Limousine Commission (TLC).

- **TLC Trip Record Data page:** https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- On that page, pick a year and month and download **Yellow Taxi Trip Records (PARQUET)**.

## Files used here

- Trip file: `yellow_tripdata_2024-01.parquet` — January 2024, 2,964,624 yellow taxi trips
- Zone lookup: `taxi_zone_lookup.csv` — maps pickup and dropoff location IDs to the 260 NYC taxi zones
  - Direct link: https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv

Trip files follow this pattern, one file per month:

- `yellow_tripdata_YYYY-MM.parquet` — for example, `yellow_tripdata_2024-01.parquet` is January 2024
- Direct link pattern: `https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_YYYY-MM.parquet`

## What is in the files

Yellow taxi trip records include pickup and dropoff timestamps, passenger count, trip distance, fare amount, tip, tolls, payment type, and pickup and dropoff location IDs. The data goes back to 2009 and is updated monthly.

## Do not commit the data

The parquet files are large and the data is free to download, so they are not kept in this repo. Download the month you want, put it in `data/`, and run the notebook.
