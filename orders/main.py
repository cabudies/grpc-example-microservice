import json
import uvicorn
from fastapi import FastAPI, APIRouter
import grpc
from google.protobuf.json_format import MessageToDict, MessageToJson
import sys
import pathlib

# from compiled_pb.auth_pb2_grpc import AuthStub
# from compiled_pb.auth_pb2 import AuthenticationRequest
# from products_pb2_grpc import ProductsServiceStub
# from products_pb2 import ProductsRequest

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

# print("parents======", str(pathlib.Path(__file__).resolve().parents[1]))

from definitions.products_pb2_grpc import ProductsServiceStub
from definitions.products_pb2 import ProductsRequest


app = FastAPI(title="Orders_GRPC")


router = APIRouter()


# @router.get("", status_code=200)
# def orders():
#     orders_list = [
#         {
#             "id": 1,
#             "customer_name": "Gurjas",
#             "order_items": [
#                 {
#                     "id": 1,
#                     "name": "Vruddhi",
#                     "quantity": 2
#                 }
#             ]
#         },
#         {
#             "id": 2,
#             "customer_name": "Varsha",
#             "order_items": [
#                 {
#                     "id": 2,
#                     "name": "Trishul",
#                     "quantity": 2
#                 }
#             ]
#         }
#     ]

#     return orders_list

@router.get("", status_code=200)
def orders():
    # channel = grpc.insecure_channel("localhost:8000/products")
    # channel = grpc.insecure_channel("http://127.0.0.1:8000/products")
    # channel = grpc.insecure_channel("http://127.0.0.1:8000")
    channel = grpc.insecure_channel("localhost:8000")
    # channel = grpc.insecure_channel("localhost:8000/products", options=(('grpc.enable_http_proxy', 0),))

    client = ProductsServiceStub(channel)
    request = ProductsRequest(id=1)
    response = client.Product(request)
    final_list = []
    final_list = list(map(lambda x: MessageToDict(x), response.products))
    return final_list


app.include_router(router, prefix="/orders")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)


