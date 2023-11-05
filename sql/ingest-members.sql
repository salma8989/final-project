COPY members FROM '/data/members.csv' DELIMITER AS ',' CSV HEADER;
SELECT * FROM members LIMIT 5;