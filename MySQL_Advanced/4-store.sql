-- Creates a trigger to update each row
-- whenever something new is inserted
DELIMITER //

CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW 
BEGIN 
    UPDATE items SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;

//