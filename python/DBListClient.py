from __future__ import print_function
import logging

import grpc
import DBListService_pb2
import DBListService_pb2_grpc

import const

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = DBListService_pb2_grpc.DBListServiceStub(channel)

        response = stub.GetList(DBListService_pb2.Null())
        print(("-"*30) + '\n' + str(response))

        stub.Append(DBListService_pb2.Value(value=6))
        stub.Append(DBListService_pb2.Value(value=4))
        stub.Append(DBListService_pb2.Value(value=3))
        stub.Append(DBListService_pb2.Value(value=2))
        stub.Append(DBListService_pb2.Value(value=1))
        response = stub.GetList(DBListService_pb2.Null())
        print(("-"*30) + '\n' + str(response))

        stub.Insert(DBListService_pb2.IndexValue(
            index=DBListService_pb2.Index(id=2),
            value=DBListService_pb2.Value(value=5)
        ))
        stub.Insert(DBListService_pb2.IndexValue(
            index=DBListService_pb2.Index(id=6),
            value=DBListService_pb2.Value(value=7)
        ))
        response = stub.GetList(DBListService_pb2.Null())
        print(("-"*30) + '\n' + str(response))

        stub.Sort(DBListService_pb2.Null())
        response = stub.GetList(DBListService_pb2.Null())
        print(("-"*30) + '\n' + str(response))

        stub.Reverse(DBListService_pb2.Null())
        response = stub.GetList(DBListService_pb2.Null())
        print(("-"*30) + '\n' + str(response))

        response = stub.SearchValue(DBListService_pb2.Value(value=4))
        p = response.id
        print(p)

        response = stub.GetValue(DBListService_pb2.Index(id=p))
        print(response.value)

        response = stub.GetLength(DBListService_pb2.Null())
        print(response.size)

        stub.RemoveIdx(DBListService_pb2.Index(id=p))
        response = stub.GetList(DBListService_pb2.Null())
        print(("-"*30) + '\n' + str(response))

        stub.RemoveIdx(DBListService_pb2.Index(id=2))
        response = stub.GetList(DBListService_pb2.Null())
        print(("-"*30) + '\n' + str(response))

        stub.RemoveValue(DBListService_pb2.Value(value=2))
        response = stub.GetList(DBListService_pb2.Null())
        print(("-"*30) + '\n' + str(response))

if __name__ == '__main__':
    logging.basicConfig()
    run()
    