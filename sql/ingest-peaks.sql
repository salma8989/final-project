COPY peaks FROM '/data/peaks.csv' DELIMITER AS ',' CSV HEADER;
SELECT * FROM peaks LIMIT 5;