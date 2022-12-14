# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import DBListService_pb2 as DBListService__pb2


class DBListServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetList = channel.unary_unary(
                '/DBList_service.DBListService/GetList',
                request_serializer=DBListService__pb2.Null.SerializeToString,
                response_deserializer=DBListService__pb2.List.FromString,
                )
        self.GetValue = channel.unary_unary(
                '/DBList_service.DBListService/GetValue',
                request_serializer=DBListService__pb2.Index.SerializeToString,
                response_deserializer=DBListService__pb2.Value.FromString,
                )
        self.Append = channel.unary_unary(
                '/DBList_service.DBListService/Append',
                request_serializer=DBListService__pb2.Value.SerializeToString,
                response_deserializer=DBListService__pb2.Null.FromString,
                )
        self.SearchValue = channel.unary_unary(
                '/DBList_service.DBListService/SearchValue',
                request_serializer=DBListService__pb2.Value.SerializeToString,
                response_deserializer=DBListService__pb2.Index.FromString,
                )
        self.RemoveIdx = channel.unary_unary(
                '/DBList_service.DBListService/RemoveIdx',
                request_serializer=DBListService__pb2.Index.SerializeToString,
                response_deserializer=DBListService__pb2.Null.FromString,
                )
        self.RemoveValue = channel.unary_unary(
                '/DBList_service.DBListService/RemoveValue',
                request_serializer=DBListService__pb2.Value.SerializeToString,
                response_deserializer=DBListService__pb2.Null.FromString,
                )
        self.Sort = channel.unary_unary(
                '/DBList_service.DBListService/Sort',
                request_serializer=DBListService__pb2.Null.SerializeToString,
                response_deserializer=DBListService__pb2.Null.FromString,
                )
        self.Reverse = channel.unary_unary(
                '/DBList_service.DBListService/Reverse',
                request_serializer=DBListService__pb2.Null.SerializeToString,
                response_deserializer=DBListService__pb2.Null.FromString,
                )
        self.GetLength = channel.unary_unary(
                '/DBList_service.DBListService/GetLength',
                request_serializer=DBListService__pb2.Null.SerializeToString,
                response_deserializer=DBListService__pb2.Size.FromString,
                )


class DBListServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetList(self, request, context):
        """Retorna a lista
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetValue(self, request, context):
        """Retorna o valor do index
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Append(self, request, context):
        """Adiciona um valor a lista
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchValue(self, request, context):
        """Retora o indice do primeiro elemento com valor Value
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveIdx(self, request, context):
        """Remove o elemento de index Index da lista
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveValue(self, request, context):
        """Remove o elemento com valor Value
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sort(self, request, context):
        """Ordena os elementos da lista
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Reverse(self, request, context):
        """Reverte os elementos da lista
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLength(self, request, context):
        """Retorna o tamanhao da lista
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DBListServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetList,
                    request_deserializer=DBListService__pb2.Null.FromString,
                    response_serializer=DBListService__pb2.List.SerializeToString,
            ),
            'GetValue': grpc.unary_unary_rpc_method_handler(
                    servicer.GetValue,
                    request_deserializer=DBListService__pb2.Index.FromString,
                    response_serializer=DBListService__pb2.Value.SerializeToString,
            ),
            'Append': grpc.unary_unary_rpc_method_handler(
                    servicer.Append,
                    request_deserializer=DBListService__pb2.Value.FromString,
                    response_serializer=DBListService__pb2.Null.SerializeToString,
            ),
            'SearchValue': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchValue,
                    request_deserializer=DBListService__pb2.Value.FromString,
                    response_serializer=DBListService__pb2.Index.SerializeToString,
            ),
            'RemoveIdx': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveIdx,
                    request_deserializer=DBListService__pb2.Index.FromString,
                    response_serializer=DBListService__pb2.Null.SerializeToString,
            ),
            'RemoveValue': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveValue,
                    request_deserializer=DBListService__pb2.Value.FromString,
                    response_serializer=DBListService__pb2.Null.SerializeToString,
            ),
            'Sort': grpc.unary_unary_rpc_method_handler(
                    servicer.Sort,
                    request_deserializer=DBListService__pb2.Null.FromString,
                    response_serializer=DBListService__pb2.Null.SerializeToString,
            ),
            'Reverse': grpc.unary_unary_rpc_method_handler(
                    servicer.Reverse,
                    request_deserializer=DBListService__pb2.Null.FromString,
                    response_serializer=DBListService__pb2.Null.SerializeToString,
            ),
            'GetLength': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLength,
                    request_deserializer=DBListService__pb2.Null.FromString,
                    response_serializer=DBListService__pb2.Size.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DBList_service.DBListService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DBListService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DBList_service.DBListService/GetList',
            DBListService__pb2.Null.SerializeToString,
            DBListService__pb2.List.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DBList_service.DBListService/GetValue',
            DBListService__pb2.Index.SerializeToString,
            DBListService__pb2.Value.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Append(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DBList_service.DBListService/Append',
            DBListService__pb2.Value.SerializeToString,
            DBListService__pb2.Null.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DBList_service.DBListService/SearchValue',
            DBListService__pb2.Value.SerializeToString,
            DBListService__pb2.Index.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveIdx(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DBList_service.DBListService/RemoveIdx',
            DBListService__pb2.Index.SerializeToString,
            DBListService__pb2.Null.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DBList_service.DBListService/RemoveValue',
            DBListService__pb2.Value.SerializeToString,
            DBListService__pb2.Null.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sort(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DBList_service.DBListService/Sort',
            DBListService__pb2.Null.SerializeToString,
            DBListService__pb2.Null.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Reverse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DBList_service.DBListService/Reverse',
            DBListService__pb2.Null.SerializeToString,
            DBListService__pb2.Null.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLength(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DBList_service.DBListService/GetLength',
            DBListService__pb2.Null.SerializeToString,
            DBListService__pb2.Size.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
