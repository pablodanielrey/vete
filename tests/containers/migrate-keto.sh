docker exec -ti `docker ps | grep keto | grep -v db | awk '{print($1)}'` keto migrate sql -e