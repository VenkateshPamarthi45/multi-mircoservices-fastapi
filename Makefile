local_run_products:
	cd products && uvicorn app.products_main:app --reload --port 8000
local_run_orders:
	cd orders && uvicorn app.orders_main:app --reload --port 8002

docker_build_products:
	cd products && docker build -t products .

docker_build_orders:
	cd orders && docker build -t orders .

docker_run_products:
	docker rm products && docker run --name products -p 8000:8000 products

docker_run_orders:
	docker rm orders && docker run --name orders -p 8002:8002 orders

docker_run:
	docker-compose up