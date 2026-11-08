# NYC Yellow Taxi Demand Analysis

**Question:** when and where is yellow-taxi demand highest in New York City, and what does a trip cost?

This project works with real trip records from New York City's yellow taxis. No made-up data — every number here comes from the NYC Taxi and Limousine Commission (TLC), the city agency that licenses and regulates taxis.

## The data

- **Source:** NYC TLC Trip Record Data, published monthly by the NYC Taxi and Limousine Commission
- **File used here:** yellow taxi trips for January 2024 — 2,964,624 trips
- **Coverage:** the full dataset goes back to 2009 and is updated monthly. Pickup and dropoff location IDs map to 260 NYC taxi zones.
- **Fields:** pickup and dropoff timestamps, passenger count, trip distance, fare amount, tip, tolls, payment type, pickup and dropoff location IDs
- **Get the data:** see `data/DATA_SOURCE.md` — the files are free, no account needed. The dataset itself is not in this repo.

## How to run it

1. Download the January 2024 yellow taxi parquet file — see `data/DATA_SOURCE.md` — and put it in `data/`.
2. Install the tools: `pip install -r requirements.txt`
3. Open `notebooks/01-taxi-demand-analysis.ipynb` and run it top to bottom.
4. The SQL version of the same questions is in `sql/taxi_queries.sql` (DuckDB / Postgres).

## How the data was cleaned

TLC data is real and messy. I dropped:

- trips with a negative fare or negative total amount (data-entry errors)
- trips with zero distance (GPS failures or cancelled rides)
- trips longer than 3 hours (almost always a meter left running)

One published pipeline dropped about 4.5% of rows as bad data. The same kind of cleaning is in the notebook.

## What the data shows

- **Calendar year 2024:** yellow taxis completed 41,169,638 trips, up 19% on calendar year 2023. Total farebox revenue was $965,887,028. There were 13,587 medallion taxicabs licensed, 10,870 of them active. Average farebox per driver was $48,698.
- **For comparison:** in 2021, total farebox revenue was just over $486 million across almost 31 million trips.
- **January 2024 alone:** 2,964,624 yellow taxi trips.
- **August 2024, one published analysis:** the raw file had about 3 million rows. A 1-million-row random sample was used, and 859,762 rows remained after cleaning. Midtown Center had the most pickups, with 44,892.
- **What a trip costs (August 2024 analysis):** trips within Manhattan averaged 2.16 miles, a fare of $14.41, and 13.17 minutes. Trips into Manhattan from outside averaged 4.47 miles, $26.62, and 21.09 minutes. Trips out of Manhattan averaged 3.57 miles, $33.91, and 22.54 minutes.
- **Green taxis** were only about 2% of total taxi trips.

## Limitations

- One month is a snapshot. January is not the whole year, and demand changes by season.
- The tip column records card tips only. Cash tips are not recorded.
- The TLC notes the trip data comes from the taxi technology providers, not from the TLC itself.
- Farebox and trip totals for the full year come from the TLC annual report, not from adding up one month's file.

## Tools

- Python (pandas, matplotlib, pyarrow)
- SQL (DuckDB / Postgres)
- Jupyter

## About

Built by Lovely Kumari — data analyst. Portfolio project on public data from the NYC Taxi and Limousine Commission.
