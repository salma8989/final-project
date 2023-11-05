DROP TABLE IF EXISTS members;
CREATE TABLE IF NOT EXISTS members (
    expedition_id TEXT,
    member_id TEXT,
    peak_id TEXT,
    peak_name TEXT,
    year TEXT,
    season TEXT,
    sex TEXT,
    age INTEGER,
    citizenship TEXT,
    expedition_role TEXT,
    hired BOOLEAN,
    highpoint_metres INTEGER,
    success BOOLEAN,
    solo BOOLEAN,
    oxygen_used BOOLEAN,
    died BOOLEAN,
    death_cause TEXT,
    death_height_metres INTEGER,
    injured BOOLEAN,
    injury_type TEXT,
    injury_height_metres INTEGER
);
