from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def home(request):
    data = {
        "message": "Welcome to BokChampions API",
        "endpoints": {
            "contact": "/api/contact/",
            "signup": "/api/signup/",
        }
    }
    return Response(data)