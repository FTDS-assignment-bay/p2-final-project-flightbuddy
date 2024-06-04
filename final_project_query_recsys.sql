CREATE TABLE airline_reviews (
    id SERIAL PRIMARY KEY,
    airline_name VARCHAR(255),
    overall_rating VARCHAR,
    review_title VARCHAR(255),
    review_date VARCHAR(50),
    verified BOOLEAN,
    review TEXT,
    aircraft VARCHAR(50),
    type_of_traveller VARCHAR(50),
    seat_type VARCHAR(50),
    route VARCHAR(255),
    date_flown VARCHAR(50),
    seat_comfort FLOAT,
    cabin_staff_service FLOAT,
    food_beverages FLOAT,
    ground_service FLOAT,
    inflight_entertainment FLOAT,
    wifi_connectivity FLOAT,
    value_for_money FLOAT,
    recommended VARCHAR(10)
);

COPY airline_reviews
FROM '/tmp/airline_review_cleaned.csv'
DELIMITER ','
CSV HEADER;

SELECT * FROM airline_reviews

SELECT 
    airline_name,
    AVG(seat_comfort) AS avg_seat_comfort,
    AVG(cabin_staff_service) AS avg_cabin_staff_service,
    AVG(food_beverages) AS avg_food_beverages,
    AVG(ground_service) AS avg_ground_service,
    AVG(inflight_entertainment) AS avg_inflight_entertainment,
    AVG(wifi_connectivity) AS avg_wifi_connectivity,
    AVG(value_for_money) AS avg_value_for_money
FROM 
    airline_reviews
GROUP BY 
    airline_name

COPY (
    SELECT 
        airline_name,
        AVG(seat_comfort) AS avg_seat_comfort,
        AVG(cabin_staff_service) AS avg_cabin_staff_service,
        AVG(food_beverages) AS avg_food_beverages,
        AVG(ground_service) AS avg_ground_service,
        AVG(inflight_entertainment) AS avg_inflight_entertainment,
        AVG(wifi_connectivity) AS avg_wifi_connectivity,
        AVG(value_for_money) AS avg_value_for_money
    FROM 
        airline_reviews
    GROUP BY 
        airline_name
) TO '/tmp/avg_ratings_per_airline.csv' WITH CSV HEADER;

