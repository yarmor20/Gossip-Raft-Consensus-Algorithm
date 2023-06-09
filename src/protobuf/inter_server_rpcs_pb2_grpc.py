# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from src.protobuf import inter_server_rpcs_pb2 as inter__server__rpcs__pb2


class InterServerRPCHandlerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HeartbeatRPC = channel.unary_unary(
                '/InterServerRPCHandler/HeartbeatRPC',
                request_serializer=inter__server__rpcs__pb2.Heartbeat.SerializeToString,
                response_deserializer=inter__server__rpcs__pb2.Heartbeat.FromString,
                )
        self.RequestVoteRPC = channel.unary_unary(
                '/InterServerRPCHandler/RequestVoteRPC',
                request_serializer=inter__server__rpcs__pb2.Heartbeat.SerializeToString,
                response_deserializer=inter__server__rpcs__pb2.Heartbeat.FromString,
                )
        self.PullEntriesRPC = channel.unary_unary(
                '/InterServerRPCHandler/PullEntriesRPC',
                request_serializer=inter__server__rpcs__pb2.Heartbeat.SerializeToString,
                response_deserializer=inter__server__rpcs__pb2.PullEntries.FromString,
                )
        self.UpdatePositionRPC = channel.unary_unary(
                '/InterServerRPCHandler/UpdatePositionRPC',
                request_serializer=inter__server__rpcs__pb2.Heartbeat.SerializeToString,
                response_deserializer=inter__server__rpcs__pb2.Heartbeat.FromString,
                )


class InterServerRPCHandlerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def HeartbeatRPC(self, request, context):
        """Used to send heartbeats as a way for inter-server communication.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestVoteRPC(self, request, context):
        """Used during leader elections to vote for the leader server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PullEntriesRPC(self, request, context):
        """Used by syncing servers to pull new log entries from sync sources.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePositionRPC(self, request, context):
        """Used by syncing servers to notify the sync sources that the logs were replicated.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InterServerRPCHandlerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HeartbeatRPC': grpc.unary_unary_rpc_method_handler(
                    servicer.HeartbeatRPC,
                    request_deserializer=inter__server__rpcs__pb2.Heartbeat.FromString,
                    response_serializer=inter__server__rpcs__pb2.Heartbeat.SerializeToString,
            ),
            'RequestVoteRPC': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestVoteRPC,
                    request_deserializer=inter__server__rpcs__pb2.Heartbeat.FromString,
                    response_serializer=inter__server__rpcs__pb2.Heartbeat.SerializeToString,
            ),
            'PullEntriesRPC': grpc.unary_unary_rpc_method_handler(
                    servicer.PullEntriesRPC,
                    request_deserializer=inter__server__rpcs__pb2.Heartbeat.FromString,
                    response_serializer=inter__server__rpcs__pb2.PullEntries.SerializeToString,
            ),
            'UpdatePositionRPC': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePositionRPC,
                    request_deserializer=inter__server__rpcs__pb2.Heartbeat.FromString,
                    response_serializer=inter__server__rpcs__pb2.Heartbeat.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'InterServerRPCHandler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InterServerRPCHandler(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def HeartbeatRPC(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InterServerRPCHandler/HeartbeatRPC',
            inter__server__rpcs__pb2.Heartbeat.SerializeToString,
            inter__server__rpcs__pb2.Heartbeat.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RequestVoteRPC(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InterServerRPCHandler/RequestVoteRPC',
            inter__server__rpcs__pb2.Heartbeat.SerializeToString,
            inter__server__rpcs__pb2.Heartbeat.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PullEntriesRPC(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InterServerRPCHandler/PullEntriesRPC',
            inter__server__rpcs__pb2.Heartbeat.SerializeToString,
            inter__server__rpcs__pb2.PullEntries.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdatePositionRPC(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InterServerRPCHandler/UpdatePositionRPC',
            inter__server__rpcs__pb2.Heartbeat.SerializeToString,
            inter__server__rpcs__pb2.Heartbeat.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
