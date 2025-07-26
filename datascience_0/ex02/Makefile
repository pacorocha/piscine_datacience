DOCKER_CONTAINER = piscine_datascience_postgres

run: up create_tables exec

up:
	docker compose up pds-db -d --remove-orphans

stop:
	docker compose stop

exec:
	docker exec -it $(DOCKER_CONTAINER) bash

create_tables:
	python3 ./table.py

clean:
	docker compose down --volumes --remove-orphans
	docker rm -f $(DOCKER_CONTAINER) 2>/dev/null || true