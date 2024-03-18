CREATE TABLE IF NOT EXISTS cars_scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    scores TEXT NOT NULL,  -- JSON or comma-separated string for scores
    observations TEXT,
    total_score REAL NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(id),
    UNIQUE(patient_id)
);