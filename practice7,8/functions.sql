--search contacts
CREATE FUNCTION search_contacts(search_text text)
RETURNS TABLE(name text, phone text)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT ph.name::text, ph.phone::text
    FROM phonebook ph
    WHERE ph.name ILIKE '%' || search_text || '%'
       OR ph.phone ILIKE '%' || search_text || '%';
END;
$$;
--get contacts
CREATE OR REPLACE FUNCTION get_contacts_paginated(lim INT, off INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    LIMIT lim OFFSET off;
END;
$$ LANGUAGE plpgsql;