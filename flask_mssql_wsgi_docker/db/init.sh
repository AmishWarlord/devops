#!/bin/bash
mysql -u root -p$MYSQL_ROOT_PASSWORD << EOF
  use $MYSQL_DB;

  CREATE TABLE favorite_colors (
    name VARCHAR(20),
    color VARCHAR(10)
  );

  INSERT INTO favorite_colors
    (name, color)
  VALUES
    ('Lancelot', 'blue'),
    ('Galahad', 'yellow');
EOF