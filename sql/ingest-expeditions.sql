COPY expeditions FROM '/data/expeditions.csv' DELIMITER AS ',' CSV HEADER;
SELECT * FROM expeditions LIMIT 5;