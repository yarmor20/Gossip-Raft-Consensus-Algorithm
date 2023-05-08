# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from src.protobuf import client_server_rpcs_pb2 as client__server__rpcs__pb2


class RPCHandlerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PutEntriesRPC = channel.unary_unary(
                '/RPCHandler/PutEntriesRPC',
                request_serializer=client__server__rpcs__pb2.Entries.SerializeToString,
                response_deserializer=client__server__rpcs__pb2.ServerResponse.FromString,
                )
        self.AckEntriesRPC = channel.unary_unary(
                '/RPCHandler/AckEntriesRPC',
                request_serializer=client__server__rpcs__pb2.ServerResponse.SerializeToString,
                response_deserializer=client__server__rpcs__pb2.ClientResponse.FromString,
                )


class RPCHandlerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PutEntriesRPC(self, request, context):
        """Used by client to pass the entries to the server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AckEntriesRPC(self, request, context):
        """Used by server to acknowledge to the client that the log entry was committed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RPCHandlerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PutEntriesRPC': grpc.unary_unary_rpc_method_handler(
                    servicer.PutEntriesRPC,
                    request_deserializer=client__server__rpcs__pb2.Entries.FromString,
                    response_serializer=client__server__rpcs__pb2.ServerResponse.SerializeToString,
            ),
            'AckEntriesRPC': grpc.unary_unary_rpc_method_handler(
                    servicer.AckEntriesRPC,
                    request_deserializer=client__server__rpcs__pb2.ServerResponse.FromString,
                    response_serializer=client__server__rpcs__pb2.ClientResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RPCHandler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RPCHandler(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PutEntriesRPC(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RPCHandler/PutEntriesRPC',
            client__server__rpcs__pb2.Entries.SerializeToString,
            client__server__rpcs__pb2.ServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AckEntriesRPC(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RPCHandler/AckEntriesRPC',
            client__server__rpcs__pb2.ServerResponse.SerializeToString,
            client__server__rpcs__pb2.ClientResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
