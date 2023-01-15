import grpc

# from definitions.builds.service_pb2 import Null, Ticket
# from definitions.builds.service_pb2_grpc import TestServiceStub
from definitions.products_pb2 import ProductsResponse, ProductsRequest
from definitions.products_pb2_grpc import ProductsServiceStub


def main():
    with grpc.insecure_channel("localhost:8000") as channel:
        client = ProductsServiceStub(channel)
        print("client==========", client)

        # product_details = client.Product(ProductsRequest(
        #     id=1
        # ))
        product_details = client.Products(ProductsRequest(id=1))

        print(product_details)


if __name__ == "__main__":
    main()