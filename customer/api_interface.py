from django.http import Http404
from rest_framework import permissions, status, views, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response

from core.common_api_interface.common_api_interface import CustomViewSet

from .filters import CustomerFilter
from .models import Customer, CustomerOrder
from .serializers import CustomerOrderSerializer, CustomerSerializer


@permission_classes(
    [
        permissions.AllowAny,
    ]
)
class CustomerListAPIView(views.APIView):
    # TODO: separeted endpoint for customer details
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, **kwargs):
        pk = kwargs.get("pk", None)
        if pk:
            customer = self.get_object(pk)
            customer_data = CustomerSerializer(customer).data
            return Response({"Customer details": customer_data}, status=status.HTTP_200_OK)

        queryset = Customer.objects.all()
        customers = CustomerSerializer(queryset, many=True)
        data = customers.data
        return Response({"posts": data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Customer.objects.create(
            name=request.data["name"],
            email=request.data["email"],
            balance=request.data["balance"],
            country=request.data["country"],
            age=request.data["age"],
            sex=request.data["sex"],
            driver_licence=request.data["driver_licence"],
        )

        data = CustomerSerializer(post_new).data

        return Response(data={"post": data}, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"error": "Method PUT is not allowed"})

        try:
            instance = Customer.objects.get(pk=pk)

        except:
            return Response(
                {"error": "Object doesn't exist"},
                status=status.HTTP_204_NO_CONTENT,
            )

        serializer = CustomerSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        customer = Customer.objects.get(pk=pk)
        customer.delete()

        return Response({"post": "delete post " + str(pk)}, status=status.HTTP_200_OK)


class CustomerOrderViewSet(CustomViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer
