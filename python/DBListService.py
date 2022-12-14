from concurrent import futures
import logging

import grpc
import DBListService_pb2
import DBListService_pb2_grpc

DBListList=[
    42, 24
 ]

class DBListServer(DBListService_pb2_grpc.DBListServiceServicer):

    def GetList(self, request, context):
        list = DBListService_pb2.List()
        for item in DBListList:
            list.values.append(DBListService_pb2.Value(value=item))
        return list

    def GetValue(self, request, context):
        return DBListService_pb2.Value(value=DBListList[request.id])

    def Append(self, request, context):
        DBListList.append(request.value)
        return DBListService_pb2.Null()

    def SearchValue(self, request, context):
        for i in range(0, len(DBListList)):
            if (DBListList[i] == request.value):
                return DBListService_pb2.Index(id=i)
        return DBListService_pb2.Index(id=-1)

    def RemoveIdx(self, request, context):
        DBListList.pop(request.id)
        return DBListService_pb2.Null()
    
    def RemoveValue(self, request, context):
        DBListList.remove(request.value)
        return DBListService_pb2.Null()

    def Sort(self, request, context):
        DBListList.sort()
        return DBListService_pb2.Null()

    def Reverse(self, request, context):
        DBListList.reverse()
        return DBListService_pb2.Null()

    def GetLength(self, request, context):
        return DBListService_pb2.Size(size=len(DBListList))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    DBListService_pb2_grpc.add_DBListServiceServicer_to_server(DBListServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()