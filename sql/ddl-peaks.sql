DROP TABLE IF EXISTS peaks;
CREATE TABLE IF NOT EXISTS peaks (
    peak_id TEXT,
    peak_name TEXT,
    peak_alternative_name TEXT,
    height_metres INTEGER,
    climbing_status TEXT,
    first_ascent_year TEXT,
    first_ascent_country TEXT,
    first_ascent_expedition_id TEXT
);
