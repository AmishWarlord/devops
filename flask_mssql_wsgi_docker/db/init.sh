#!/bin/bash
mysql -u root -p$MYSQL_ROOT_PASSWORD << EOF
  use $MYSQL_DB;

  CREATE TABLE $MYSQL_TABLE (
    name VARCHAR(20),
    color VARCHAR(10)
  );

  INSERT INTO $MYSQL_TABLE
    (name, color)
  VALUES
    ('Lancelot', 'blue'),
    ('Galahad', 'yellow');
EOF