from django.shortcuts import render

class ListAddShoppingList(generics.ListCreateAPIView):
    serializer_class = ShoppingListSerializer

    def perform_create(self, serializer):  # NEW!
        shopping_list = serializer.save()
        shopping_list.members.add(self.request.user)
        return shopping_list

    def get_queryset(self):
        return ShoppingList.objects.filter(members=self.request.user)