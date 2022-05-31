from rest_framework.response import Response
from rest_framework import viewsets, permissions, views
from rest_framework.decorators import action, permission_classes
from rest_framework import status
from .models import CustomerOrder, Customer
from .serializers import CustomerOrderSerializer, CustomerSerializer
from .filters import CustomerFilter


class CustomerViewSet(viewsets.ModelViewSet):
    """
       A viewset for information about customers and theirs orders
    """

    queryset = CustomerOrder.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerOrderSerializer
    filterset_class = CustomerFilter


@permission_classes([permissions.AllowAny, ])
class CustomerListAPIView(views.APIView):

    def get(self, request):
        queryset = Customer.objects.all()
        return Response({'posts': CustomerSerializer(queryset, many=True).data})

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Customer.objects.create(
            name=request.data['name'],
            email=request.data['email'],
            balance=request.data['balance'],
            country=request.data['country'],
            age=request.data['age'],
            sex=request.data['sex'],
            driver_licence=request.data['driver_licence']
        )

        return Response({'post': CustomerSerializer(post_new).data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"error": "Method PUT is not allowed"})

        try:
            instance = Customer.objects.get(pk=pk)

        except:
            return Response({"error": "Object doesn't exist"})

        serializer = CustomerSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        customer = Customer.objects.get(pk=pk)
        customer.delete()

        return Response({"post": "delete post " + str(pk)})
