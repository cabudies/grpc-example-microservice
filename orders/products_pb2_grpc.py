# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import products_pb2 as products__pb2


class ProductsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Products = channel.unary_unary(
                '/ProductsService/Products',
                request_serializer=products__pb2.ProductsRequest.SerializeToString,
                response_deserializer=products__pb2.ProductsResponse.FromString,
                )


class ProductsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Products(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Products': grpc.unary_unary_rpc_method_handler(
                    servicer.Product,
                    request_deserializer=products__pb2.ProductsRequest.FromString,
                    response_serializer=products__pb2.ProductsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ProductsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProductsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Products(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProductsService/Products',
            products__pb2.ProductsRequest.SerializeToString,
            products__pb2.ProductsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
