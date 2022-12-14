# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import data_stream_service_pb2 as data__stream__service__pb2


class DataStreamStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUserByID = channel.unary_unary(
                '/DataStream/GetUserByID',
                request_serializer=data__stream__service__pb2.ID.SerializeToString,
                response_deserializer=data__stream__service__pb2.UserData.FromString,
                )
        self.GetUserList = channel.unary_unary(
                '/DataStream/GetUserList',
                request_serializer=data__stream__service__pb2.UserRequest.SerializeToString,
                response_deserializer=data__stream__service__pb2.UserDataList.FromString,
                )


class DataStreamServicer(object):
    """The greeting service definition.
    """

    def GetUserByID(self, request, context):
        """single object return
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserList(self, request, context):
        """list of object
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataStreamServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUserByID': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserByID,
                    request_deserializer=data__stream__service__pb2.ID.FromString,
                    response_serializer=data__stream__service__pb2.UserData.SerializeToString,
            ),
            'GetUserList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserList,
                    request_deserializer=data__stream__service__pb2.UserRequest.FromString,
                    response_serializer=data__stream__service__pb2.UserDataList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DataStream', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataStream(object):
    """The greeting service definition.
    """

    @staticmethod
    def GetUserByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataStream/GetUserByID',
            data__stream__service__pb2.ID.SerializeToString,
            data__stream__service__pb2.UserData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataStream/GetUserList',
            data__stream__service__pb2.UserRequest.SerializeToString,
            data__stream__service__pb2.UserDataList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
