UPDATE cars_scores
SET scores = :scores, total_score = :total_score, observations = :observations
WHERE patient_id = :patient_id AND date = :date
