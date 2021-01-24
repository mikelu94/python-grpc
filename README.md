# gRPC Client/Server in Python

## Dependencies

- `grpcio-tools`

## How Generated Code was Generated

```bash
$ python3 -m grpc_tools.protoc -I./ --python_out=./client --grpc_python_out=./client item.proto
$ python3 -m grpc_tools.protoc -I./ --python_out=./server --grpc_python_out=./server item.proto
```

## How to Set Up

```bash
for dir in client server
do
    python3 -m venv ${dir}/venv
    ${dir}/venv/bin/pip install --upgrade pip
    ${dir}/venv/bin/pip install -r ${dir}/requirements.txt
done
```

## How to Run Server

```bash
$ server/venv/bin/python server/app.py &
```

## How to Use Client

```bash
$ client/venv/bin/python client/app.py --help
```