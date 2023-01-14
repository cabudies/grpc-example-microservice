import uvicorn
from fastapi import FastAPI, APIRouter

app = FastAPI(title="Products_GRPC")


router = APIRouter()


@router.get("", status_code=200)
def products():
    products_list = [
        {
            "id": 1,
            "name": "Trishul"
        },
        {
            "id": 2,
            "name": "Vruddhi"
        }
    ]

    return products_list


app.include_router(router, prefix="/products")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # server = grpc.server(ThreadPoolExecutor(max_workers=10))
    # add_TestServiceServicer_to_server(Service(), server)
    # server.add_insecure_port("[::]:3000")
    # server.start()

    # print("The server is up and running...")
    # server.wait_for_termination()

