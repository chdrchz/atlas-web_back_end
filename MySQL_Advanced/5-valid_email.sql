-- Resets the valid_email variable if the email is updated
CREATE TRIGGER reset_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
    SET NEW.valid_email = 0;
    END IF;
END;