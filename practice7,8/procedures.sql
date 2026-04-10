--upsert contacts
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM phonebook WHERE name = p_name
    ) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;
--delete_contact
CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = p_value OR phone = p_value;
END;
$$;
--insert_many
CREATE OR REPLACE PROCEDURE insert_many()
LANGUAGE plpgsql AS $$
DECLARE
    names TEXT[] := ARRAY['Ali', 'Aruzhan', 'BadNumber'];
    phones TEXT[] := ARRAY['87001112233', '87005556677', '123'];
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        IF length(phones[i]) < 11 THEN
            RAISE NOTICE 'Invalid phone: %', phones[i];
        ELSE
            INSERT INTO phonebook(name, phone)
            VALUES (names[i], phones[i]);
        END IF;
    END LOOP;
END;
$$;