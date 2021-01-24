from concurrent import futures
import grpc

import item_pb2
import item_pb2_grpc

items = []
class ItemizerServicer(item_pb2_grpc.ItemizerServicer):

    def CreateItem(self, request, context):
        items.append(request)
        return item_pb2.SuccessResponse(success=True)

    def CreateItems(self, request, context):
        items.extend(request.items)
        return item_pb2.SuccessResponse(success=True)

    def GetItems(self, request, context):
        return item_pb2.Items(items=items)

    def CreateItemsStream(self, request_iterator, context):
        for item in request_iterator:
            items.append(item)
        return item_pb2.SuccessResponse(success=True) 

    def GetItemsStream(self, request, context):
        for item in items:
            yield item

    def FindItemsStream(self, request_iterator, context):
        for item in request_iterator:
            print(item in items)
            yield item_pb2.FoundResponse(found=item in items)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    item_pb2_grpc.add_ItemizerServicer_to_server(ItemizerServicer(), server)
    server.add_insecure_port('[::]:3000')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    print('Server listening on port 3000')
    serve()