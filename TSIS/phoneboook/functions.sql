CREATE OR REPLACE FUNCTION search_contacts(p TEXT)
RETURNS TABLE(name VARCHAR, email VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.email, ph.phone
    FROM contacts c
    LEFT JOIN phones ph ON c.id = ph.contact_id
    WHERE c.name ILIKE '%'||p||'%'
       OR c.email ILIKE '%'||p||'%'
       OR ph.phone ILIKE '%'||p||'%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_contacts(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, email VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.email
    FROM contacts c
    ORDER BY c.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;