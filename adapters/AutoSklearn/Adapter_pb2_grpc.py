# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Adapter_pb2 as Adapter__pb2


class AdapterServiceStub(object):
    """
    AutoML Adapter Service implementation. Service provide functionality to execute and interact with the current AutoML process.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartAutoML = channel.unary_stream(
                '/AdapterService/StartAutoML',
                request_serializer=Adapter__pb2.StartAutoMLRequest.SerializeToString,
                response_deserializer=Adapter__pb2.StartAutoMLResponse.FromString,
                )
        self.TestAdapter = channel.unary_unary(
                '/AdapterService/TestAdapter',
                request_serializer=Adapter__pb2.TestAdapterRequest.SerializeToString,
                response_deserializer=Adapter__pb2.TestAdapterResponse.FromString,
                )


class AdapterServiceServicer(object):
    """
    AutoML Adapter Service implementation. Service provide functionality to execute and interact with the current AutoML process.
    """

    def StartAutoML(self, request, context):
        """
        Execute a new AutoML run. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestAdapter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AdapterServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartAutoML': grpc.unary_stream_rpc_method_handler(
                    servicer.StartAutoML,
                    request_deserializer=Adapter__pb2.StartAutoMLRequest.FromString,
                    response_serializer=Adapter__pb2.StartAutoMLResponse.SerializeToString,
            ),
            'TestAdapter': grpc.unary_unary_rpc_method_handler(
                    servicer.TestAdapter,
                    request_deserializer=Adapter__pb2.TestAdapterRequest.FromString,
                    response_serializer=Adapter__pb2.TestAdapterResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AdapterService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AdapterService(object):
    """
    AutoML Adapter Service implementation. Service provide functionality to execute and interact with the current AutoML process.
    """

    @staticmethod
    def StartAutoML(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/AdapterService/StartAutoML',
            Adapter__pb2.StartAutoMLRequest.SerializeToString,
            Adapter__pb2.StartAutoMLResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TestAdapter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AdapterService/TestAdapter',
            Adapter__pb2.TestAdapterRequest.SerializeToString,
            Adapter__pb2.TestAdapterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
