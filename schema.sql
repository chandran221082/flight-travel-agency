DROP TABLE IF EXISTS flights;

CREATE TABLE flights (
    origin_city TEXT NOT NULL,
    destination_city TEXT NOT NULL,
    airline TEXT NOT NULL,
    depart_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    available_seates INTEGER
);
