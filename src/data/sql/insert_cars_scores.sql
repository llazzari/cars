INSERT OR IGNORE INTO cars_scores (patient_id, date, scores, total_score, observations)
  VALUES (:patient_id, :date, :scores, :total_score, :observations)