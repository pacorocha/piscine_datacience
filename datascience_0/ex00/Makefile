DOCKER_CONTAINER = piscine_datascience_postgres

run: up exec

up:
	docker compose up pds-db -d --remove-orphans

stop:
	docker compose stop

exec:
	docker exec -it $(DOCKER_CONTAINER) bash

clean:
	docker compose down --rmi all --volumes