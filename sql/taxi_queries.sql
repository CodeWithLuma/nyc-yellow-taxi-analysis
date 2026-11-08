-- NYC Yellow Taxi Demand Analysis — SQL
-- Dialect: DuckDB / Postgres. Load the yellow taxi parquet file into a
-- table called yellow_trips first (see data/DATA_SOURCE.md for the file).
-- These queries answer the same questions as the notebook.

-- Total trips and total farebox revenue
SELECT
    COUNT(*) AS trip_count,
    SUM(fare_amount) AS total_farebox
FROM yellow_trips;

-- Average fare, average distance, average trip duration in minutes
SELECT
    AVG(fare_amount) AS avg_fare,
    AVG(trip_distance) AS avg_distance,
    AVG(EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime)) / 60) AS avg_duration_minutes
FROM yellow_trips;

-- Same totals after cleaning out bad rows:
-- negative fares, negative totals, zero-distance trips, trips over 3 hours
SELECT
    COUNT(*) AS trip_count,
    SUM(fare_amount) AS total_farebox
FROM yellow_trips
WHERE fare_amount >= 0
  AND total_amount >= 0
  AND trip_distance > 0
  AND tpep_dropoff_datetime > tpep_pickup_datetime
  AND tpep_dropoff_datetime - tpep_pickup_datetime <= INTERVAL '3 hours';

-- Busiest pickup zones (location IDs map to 260 NYC taxi zones)
SELECT
    PULocationID AS pickup_zone_id,
    COUNT(*) AS trip_count
FROM yellow_trips
GROUP BY PULocationID
ORDER BY trip_count DESC;

-- Trips by pickup hour — when is demand highest
SELECT
    EXTRACT(HOUR FROM tpep_pickup_datetime) AS pickup_hour,
    COUNT(*) AS trip_count
FROM yellow_trips
GROUP BY pickup_hour
ORDER BY pickup_hour;

-- Average fare by payment type
SELECT
    payment_type,
    COUNT(*) AS trip_count,
    AVG(fare_amount) AS avg_fare
FROM yellow_trips
GROUP BY payment_type
ORDER BY trip_count DESC;
