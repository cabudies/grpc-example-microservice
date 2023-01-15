from concurrent.futures import ThreadPoolExecutor
import grpc

from definitions.products_pb2 import ProductsResponse, ProductsResponseList
from definitions.products_pb2_grpc import ProductsServiceServicer, add_ProductsServiceServicer_to_server
import definitions.products_pb2_grpc as products_pb2_grpc_od


products_list = [
    ProductsResponse(id=1, title="Trishul"),
    ProductsResponse(id=2, title="Vruddhi")
]


class Service(ProductsServiceServicer):
    def Product(self, request, context):
        # return ProductsResponseList(products=products_list)
        products_list_response = list(filter(
            lambda x: x.id == request.id, products_list
        ))
        print("products_list_response=======", products_list_response)
        return ProductsResponseList(products=products_list_response)


def execute_server():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    products_pb2_grpc_od.add_ProductsServiceServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:8000")
    # server.add_insecure_port("localhost:8000")
    server.start()

    print("The server is up and running...")
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()
