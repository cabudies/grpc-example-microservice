import uvicorn
from fastapi import FastAPI, APIRouter
import grpc
from google.protobuf.json_format import MessageToDict
import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from definitions.products_pb2_grpc import ProductsServiceStub
from definitions.products_pb2 import ProductsRequest


app = FastAPI(title="Orders_GRPC")


router = APIRouter()

@router.get("", status_code=200)
def orders():
    channel = grpc.insecure_channel("localhost:8000")
    client = ProductsServiceStub(channel)
    request = ProductsRequest(id=1)
    response = client.Product(request)
    final_list = []
    final_list = list(map(lambda x: MessageToDict(x), response.products))
    return final_list


app.include_router(router, prefix="/orders")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)


