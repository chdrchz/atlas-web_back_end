-- Create a need_meeting view
-- if no meeting has occured for a month
CREATE VIEW need_meeting AS
SELECT name 
FROM students 
WHERE score < 80 
AND (last_meeting IS NULL OR last_meeting <= CURDATE() - INTERVAL 1 MONTH);