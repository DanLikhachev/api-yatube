from http import HTTPStatus

from posts.models import Comment, Group, Post
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def create(self, request, *args, **kwargs):
        serilizer = self.get_serializer(data=request.data)
        if serilizer.is_valid():
            self.perform_create(serilizer)
            return Response(serilizer.data, status=HTTPStatus.CREATED)
        return Response(status=HTTPStatus.BAD_REQUEST)

    def update(self, request, *args, **kwargs):

        post = self.get_object()

        if post.author != request.user:
            return Response(status=HTTPStatus.FORBIDDEN)

        serializer = self.get_serializer(
            post,
            data=request.data,
            partial=False
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.OK)

        return Response(status=HTTPStatus.BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):

        post = self.get_object()

        if post.author != request.user:
            return Response(status=HTTPStatus.FORBIDDEN)

        serializer = self.get_serializer(post, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.OK)
        else:
            return Response(status=HTTPStatus.BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):

        post = self.get_object()

        if post.author != request.user:
            return Response(status=HTTPStatus.FORBIDDEN)
        else:
            self.perform_destroy(post)
            return Response(status=HTTPStatus.NO_CONTENT)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        related_post = self.kwargs.get('post')
        comments = Comment.objects.filter(post=related_post)
        return comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post')
        post = Post.objects.get(pk=post_id)
        serializer.save(author=self.request.user, post=post)

    def update(self, request, *args, **kwargs):
        comment = self.get_object()

        if comment.author != request.user:
            return Response(status=HTTPStatus.FORBIDDEN)

        serializer = self.get_serializer(
            comment,
            data=request.data,
            partial=False
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.OK)

        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        comment = self.get_object()

        if comment.author != request.user:
            return Response(status=HTTPStatus.FORBIDDEN)

        serializer = self.get_serializer(
            comment,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.OK)
        else:
            return Response(status=HTTPStatus.BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            return Response(status=HTTPStatus.FORBIDDEN)
        else:
            self.perform_destroy(comment)
            return Response(status=HTTPStatus.NO_CONTENT)
