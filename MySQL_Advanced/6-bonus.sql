DELIMITER //

CREATE PROCEDURE AddBonus (
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    DECLARE project_id INT;

    -- Check if the project exists
    SELECT id INTO project_id 
    FROM projects 
    WHERE name = project_name;

    -- If the project doesn't exist, insert a new project
    IF project_id IS NULL THEN
        INSERT INTO projects (name) 
        VALUES (project_name);
        
        -- Get the last inserted project ID
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Add the correction (linking user, project, and score)
    INSERT INTO corrections (user_id, project_id, score) 
    VALUES (user_id, project_id, score);

END //

DELIMITER ;