SELECT * FROM furniture WHERE furn_type = ‘_furniture’;
SELECT * FROM furniture WHERE interactive = ‘_interaction’;
SELECT furniture.name, furniture.furn_type, furniture.image FROM furniture INNER JOIN origin ON "+_origin+" = 'TRUE' AND origin.furn_id = furniture.furn_id;
SELECT furniture.name, furniture.furn_type, collectible.collect_type, furniture.image FROM furniture INNER JOIN collectible ON collectible.collect_type = '"+_collect+"' AND furniture.furn_id = collectible.furn_id;
SELECT furniture.name, furniture.furn_type, flowers.color, furniture.image FROM furniture INNER JOIN flowers ON flowers.color = '"+_flower+"' AND furniture.furn_id = flowers.furn_id;
SELECT furniture.name, furniture.furn_type, furniture.image FROM furniture INNER JOIN owns ON owns.name = '"+_villager+"' AND furniture.furn_id = owns.furn_id;