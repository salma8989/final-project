DROP TABLE IF EXISTS expeditions;
CREATE TABLE IF NOT EXISTS expeditions (
    expedition_id TEXT,
    peak_id TEXT,
    peak_name TEXT,
    year TEXT,
    season TEXT,
    basecamp_date DATE,
    highpoint_date DATE,
    termination_date DATE,
    termination_reason TEXT,
    highpoint_metres INTEGER,
    members INTEGER,
    member_deaths INTEGER,
    hired_staff INTEGER,
    hired_staff_deaths INTEGER,
    oxygen_used BOOLEAN,
    trekking_agency TEXT
);
