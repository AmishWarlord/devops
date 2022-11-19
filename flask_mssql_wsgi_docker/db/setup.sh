#!/bin/bash
mysql -u root -p$MYSQL_ROOT_PASSWORD << EOF
GRANT SELECT ON $MYSQL_DB.* TO '$MYSQL_USER'@'%'; 
EOF