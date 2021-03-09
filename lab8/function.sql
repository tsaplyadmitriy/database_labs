CREATE OR REPLACE FUNCTION generate_longtitude()
RETURNS TABLE(address VARCHAR(45), district VARCHAR(45),city_id smallint)) AS
$$
BEGIN
RETURN QUERY
SELECT address.address, address.district,address.city_id
FROM address
WHERE  address.address::text  LIKE '%' || '11' || '%'
AND address.city_id >399
AND address.city_id <601;
END;
$$
LANGUAGE plpgsql;