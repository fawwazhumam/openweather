CREATE TABLE IF NOt EXISTS weather (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    humidity INTEGER,
    weather_description TEXT,
    date DATE
);