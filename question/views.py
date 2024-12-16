
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
from rest_framework.exceptions import NotFound
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.response import Response
# from project.response import DefaultResponse as Response
from rest_framework.views import APIView

from lecture.models import ResourceFile
from question.api.serializers.question_serializers import QuestionSerializer
from question.models import Question
from utils.file_hash import calculate_file_hash
from utils.pagintation import CustomPagination


class QuestionList(APIView):
    """
    List All Question
    """

    # queryset = Question.objects.filter(is_deleted=False).order_by("-id")
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination

    @swagger_auto_schema(
        operation_description="List All Question",
        responses={200: QuestionSerializer, 400: 'Bad Request'}
    )
    def get_queryset(self, request):
        return Question.objects.filter(is_deleted=False, owner=request.user.id).order_by("-id")

    def get(self, request, *args, **kwargs):
        paginator = self.pagination_class()
        title = self.request.query_params.get("title", None)
        head = self.request.query_params.get("head", None)
        search = self.request.query_params.get("search", None)
        query = Q()
        if title:
            query &= Q(title=title)
        if head:
            query &= Q(head=head)
        if search:
            query &= Q(title__icontains=search)
        queryset = self.get_queryset(request).filter(query)
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = self.serializer_class(page, many=True, context={'request': request})
            return paginator.get_paginated_response(serializer.data)

        serializer = self.serializer_class(self.get_queryset(request), many=True)
        return Response(
            {"message": "Question Successfully Listed", "result": serializer.data},
            status=status.HTTP_200_OK,
        )


class QuestionAPIView(APIView):
    queryset = Question.objects.filter(is_deleted=False).order_by("-id")
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    @swagger_auto_schema(
        operation_description="Create Question",
        responses={200: QuestionSerializer, 400: 'Bad Request'}
    )
    def post(self, request):
        """
        Create Question
        :param request: title, head, statement
        :return: data
        """
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            # Directly modify the validated_data dictionary
            serializer.validated_data['owner'] = request.user.id
            question = serializer.save(owner=request.user)
            self.handle_files(question, request)
            return Response(
                {"message": "Question Successfully Created", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def handle_files(self, question, request):
        file_fields = [
            "question_content_image",
            "question_content_video",
            "question_content_audio",
            "question_content_formula",
            "answer_options_image",
            "answer_options_video",
            "answer_options_audio",
            "answer_options_formula",
            "answer_explanation_image",
        ]

        for field in file_fields:
            files = request.FILES.getlist(field)
            for file in files:
                file_hash = calculate_file_hash(file)
                existing_file = ResourceFile.objects.filter(file_hash=file_hash).first()

                if existing_file:
                    print(f"File '{file.name}' already exists in the database.")
                    continue

                resource_file = ResourceFile.objects.create(
                    file=file,
                    owner=request.user,
                    file_hash=file_hash
                )
                # Use the related manager to add files
                getattr(question, field).add(resource_file)

        question.save()

    @swagger_auto_schema(
        operation_description="Get Single Question",
        responses={200: QuestionSerializer, 400: 'Bad Request'}
    )
    def get(self, request, pk=None):
        """
        Get Single Question
        :param request: id
        :param pk: pk
        :return: data
        """
        try:
            question = Question.objects.get(id=pk)
        except Question.DoesNotExist:
            raise NotFound("Question does not exist")

        serializer = self.serializer_class(question)
        return Response(
            {"message": "Question Found Successfully", "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        operation_description="Update Single Question",
        responses={200: QuestionSerializer, 400: 'Bad Request'}
    )
    def patch(self, request, pk=None):
        """
        Update Single Question
        :param request: id
        :param pk: pk
        :return: data
        """
        try:
            question = Question.objects.get(id=pk)
        except Question.DoesNotExist:
            raise NotFound("Question does not exist")
        serializer = self.serializer_class(question, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"message": "Question Successfully Updated", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete Single Question",
        responses={200: QuestionSerializer, 400: 'Bad Request'}
    )
    def delete(self, request, pk=None):
        """
        Delete Single Question
        :param request: id
        :param pk: pk
        :return: Success Response
        """
        try:
            question = Question.objects.get(id=pk)
        except Question.DoesNotExist:
            raise NotFound("Question does not exist")
        question.is_deleted = True
        question.save()
        return Response(
            {"message": "Question Deleted Successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
