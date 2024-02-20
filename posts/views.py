from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)

        # Checar se os campos inválidos foram inseridos na requisição
        validated_data = serializer.validated_data
        if 'id' in validated_data or 'created_datetime' in validated_data or 'username' in validated_data:
            return Response({"detail": "Não é possível alterar o id, username ou data de criação."},
                            status=status.HTTP_400_BAD_REQUEST)
                            
        # Atualizar a instância com os dados validados
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data
        if 'id' in validated_data or 'created_datetime' in validated_data or 'username' in validated_data:
            return Response({"detail": "Não é possível alterar o id, username ou data de criação."},
                            status=status.HTTP_400_BAD_REQUEST)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return Response(serializer.data)