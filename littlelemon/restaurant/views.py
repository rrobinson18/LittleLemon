from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer


# @api_view()
# @permission_classes([IsAuthenticated])
# def msg(request):
#     return Response({"message": "This view is protected"})

def index(request):
    return render(request, 'index.html', {})

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


# class BookingViewSet():
    
#     serializer_class = BookingSerializer   

# class UserViewSer(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]     
