# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

import grpc

# from definitions.builds.service_pb2 import Confirmation
# from definitions.builds.service_pb2_grpc import TestServiceServicer, add_TestServiceServicer_to_server
# from ..definitions.products_pb2 import ProductsResponse
# from ..definitions.products_pb2_grpc import ProductsServiceServicer, add_ProductsServiceServicer_to_server

from products_pb2 import ProductsResponse
from products_pb2_grpc import ProductsServiceServicer, add_ProductsServiceServicer_to_server

class Service(ProductsServiceServicer):
    # def Health(self, request, context):
    #     return request

    def ProductsResponse(self, request, context):
        # expected_dateline = datetime.utcnow() + timedelta(days=request.story_points)
        # return Confirmation(expected_dateline=expected_dateline.strftime("%Y-%m-%d %H:%M:%S"))
        return ProductsResponse


def execute_server():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_ProductsServiceServicer_to_server(Service(), server)
    # server.add_insecure_port("[::]:8000")
    server.add_insecure_port("localhost:8000")
    server.start()

    print("The server is up and running...")
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()
