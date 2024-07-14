from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSrializer


# Create your views here.
@api_view(["GET", "POST", "PATCH"])
def home(request):
    if request.method == "GET":
        return Response(
            {
                "status": 200,
                "message": "yes this is django framwork",
                "method_called": "you called GET method",
            }
        )
    elif request.method == "POST":
        return Response(
            {
                "status": 100,
                "message": "yes this is django framwork",
                "method_called": "you called POST method",
            }
        )
    elif request.method == "PATCH":
        return Response(
            {
                "status": 400,
                "message": "yes this is django framwork",
                "method_called": "you called PATCH method",
            }
        )


@api_view(["POST"])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSrializer(data=data)
        if serializer.is_valid():
            print(serializer.data)
            return Response(
                {"status": True, "message": "succes data", "data": serializer.data}
            )
        return Response(
                {"status": False, "message": "invalid data", "data": serializer.errors}
            )
    except Exception as e:
        print(e)
    return Response(
        {
            "status": False,
            "message": "something went wrong",
        }
    )
