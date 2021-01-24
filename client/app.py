import grpc
import click

import item_pb2
import item_pb2_grpc

def get_itemizer_stub():
    channel = grpc.insecure_channel('localhost:3000')
    return item_pb2_grpc.ItemizerStub(channel)

@click.group()
def cli():
    pass

@click.command()
@click.option('--name', '-n', required=True)
def create_item(name):
    stub = get_itemizer_stub()
    response = stub.CreateItem(item_pb2.Item(name=name))
    click.echo(response)

@click.command()
@click.option('--name', '-n', 'names', multiple=True)
def create_items(names):
    stub = get_itemizer_stub()
    items = map(lambda name: item_pb2.Item(name=name), names)
    response = stub.CreateItems(item_pb2.Items(items=items))
    click.echo(response)

@click.command()
def get_items():
    stub = get_itemizer_stub()
    response = stub.GetItems(item_pb2.NullRequest())
    click.echo(response)

@click.command()
@click.option('--name', '-n', 'names', multiple=True)
def create_items_stream(names):
    stub = get_itemizer_stub()
    items = map(lambda name: item_pb2.Item(name=name), names)
    response = stub.CreateItemsStream(items)
    click.echo(response)

@click.command()
def get_items_stream():
    stub = get_itemizer_stub()
    for item in stub.GetItemsStream(item_pb2.NullRequest()):
        click.echo(item)

@click.command()
@click.option('--name', '-n', 'names', multiple=True)
def find_items_stream(names):
    stub = get_itemizer_stub()
    items = map(lambda name: item_pb2.Item(name=name), names)
    for found_response in stub.FindItemsStream(items):
        click.echo(found_response.found)

if __name__ == '__main__':
    cli.add_command(create_item)
    cli.add_command(create_items)
    cli.add_command(get_items)
    cli.add_command(create_items_stream)
    cli.add_command(get_items_stream)
    cli.add_command(find_items_stream)
    cli()