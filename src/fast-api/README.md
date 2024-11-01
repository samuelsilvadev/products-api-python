# How to run?

1. Find the container you created for this repo:

```shell
    docker container ls
```

2. Let's say it has the id = 123, now, we need to enter the docker container using that id:

```shell
    docker exec -it 123  bash
```

3. Activate environment

```shell
    cd src/fast-api
    source venv/bin/activate
```

4. Run the app

```shell
    uvicorn app:app --host 0.0.0.0 --port 4000 --reload
```
