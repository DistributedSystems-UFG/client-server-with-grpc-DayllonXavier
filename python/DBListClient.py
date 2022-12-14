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
        print('\n' + str(response))
        response = stub.GetValue(DBListService_pb2.Index(id=0))
        print('Valor {} na posição {}.'.format(response.value, 0))
        response = stub.GetValue(DBListService_pb2.Index(id=1))
        print('Valor {} na posição {}.'.format(response.value, 1))

        stub.Append(DBListService_pb2.Value(value=60))
        response = stub.GetList(DBListService_pb2.Null())
        print('\n' + str(response))

        response = stub.SearchValue(DBListService_pb2.Value(value=60))
        print('Valor {} na posição {}.'.format(60, response.id))

        stub.Sort(DBListService_pb2.Null())
        response = stub.GetList(DBListService_pb2.Null())
        print('\n' + str(response))

        stub.Reverse(DBListService_pb2.Null())
        response = stub.GetList(DBListService_pb2.Null())
        print('\n' + str(response))

        response = stub.GetLength(DBListService_pb2.Null())
        print('Size {}'.format(response.size))

        stub.RemoveValue(DBListService_pb2.Value(value=60))
        response = stub.GetList(DBListService_pb2.Null())
        print('\n' + str(response))

        stub.RemoveIdx(DBListService_pb2.Index(id=0))
        response = stub.GetList(DBListService_pb2.Null())
        print('\n' + str(response))

if __name__ == '__main__':
    logging.basicConfig()
    run()
    