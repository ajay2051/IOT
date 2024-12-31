import ast
import json

from rest_framework import serializers

from lecture.models import ResourceFile
from question.models import Question, TestPaperCategory


class ResourceFileQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceFile
        fields = ["id", "name", "file", "description", "thumbnail", "owner"]


class QuestionSerializer(serializers.ModelSerializer):
    question_content_text = serializers.SerializerMethodField()

    # Nested fields that are lists of ResourceFileQuestionSerializer
    question_content_image = ResourceFileQuestionSerializer(many=True, required=False)
    question_content_video = ResourceFileQuestionSerializer(many=True, required=False)
    question_content_audio = ResourceFileQuestionSerializer(many=True, required=False)
    question_content_formula = ResourceFileQuestionSerializer(many=True, required=False)

    answer_options_text = serializers.SerializerMethodField()
    answer_options_image = ResourceFileQuestionSerializer(many=True, required=False)
    answer_options_video = ResourceFileQuestionSerializer(many=True, required=False)
    answer_options_audio = ResourceFileQuestionSerializer(many=True, required=False)
    answer_options_formula = ResourceFileQuestionSerializer(many=True, required=False)

    answer_explanation_text = serializers.SerializerMethodField()
    answer_explanation_image = ResourceFileQuestionSerializer(many=True, required=False)

    def get_question_content_text(self, obj):
        if obj.question_content_text:
            try:
                # First try to parse as a list of strings
                parsed = ast.literal_eval(obj.question_content_text)
                # Ensure it's a list of strings
                if isinstance(parsed, list):
                    return [str(item).strip("'") for item in parsed]
                # If not a list, return as a single-item list
                return [str(obj.question_content_text).strip("'")]
            except (ValueError, SyntaxError):
                # If parsing fails, return as a single-item list
                return [str(obj.question_content_text).strip("'")]
        return []

    def get_answer_options_text(self, obj):
        if obj.answer_options_text:
            try:
                # First try to parse as a list of strings
                parsed = ast.literal_eval(obj.answer_options_text)
                # Ensure it's a list of strings
                if isinstance(parsed, list):
                    return [str(item).strip("'") for item in parsed]
                # If not a list, return as a single-item list
                return [str(obj.answer_options_text).strip("'")]
            except (ValueError, SyntaxError):
                # If parsing fails, return as a single-item list
                return [str(obj.answer_options_text).strip("'")]
        return []

    def get_answer_explanation_text(self, obj):
        if obj.answer_explanation_text:
            try:
                # First try to parse as a list of strings
                parsed = ast.literal_eval(obj.answer_explanation_text)
                # Ensure it's a list of strings
                if isinstance(parsed, list):
                    return [str(item).strip("'") for item in parsed]
                # If not a list, return as a single-item list
                return [str(obj.answer_explanation_text).strip("'")]
            except (ValueError, SyntaxError):
                # If parsing fails, return as a single-item list
                return [str(obj.answer_explanation_text).strip("'")]
        return []

    def create(self, validated_data):
        # Get request FILES and POST data
        request_files = self.context['request'].FILES
        request_data = self.context['request'].data

        # Text fields to handle
        text_fields = [
            'question_content_text',
            'answer_options_text',
            'answer_explanation_text'
        ]

        # Remove text and image-related data from validated_data to prevent validation errors
        for field in text_fields:
            validated_data.pop(field, None)

        resource_file_keys = [
            'question_content_image',
            'question_content_video',
            'question_content_audio',
            'question_content_formula',
            'answer_options_image',
            'answer_options_video',
            'answer_options_audio',
            'answer_options_formula',
            'answer_explanation_image'
        ]

        for key in resource_file_keys:
            validated_data.pop(key, None)

        # Handle text fields with array-like keys
        for field in text_fields:
            # Collect all values for this field
            field_values = []

            # Check for keys like 'field[0]', 'field[1]', etc.
            for key in request_data.keys():
                if key.startswith(f'{field}[') and key.endswith(']'):
                    field_values.append(request_data[key])

            # Convert to JSON string if values exist
            if field_values:
                validated_data[field] = json.dumps(field_values)

        # Create the Question instance
        question = Question.objects.create(**validated_data)

        # Resource file types to handle
        resource_mappings = [
            ('question_content_image', question.question_content_image),
            ('question_content_video', question.question_content_video),
            ('question_content_audio', question.question_content_audio),
            ('question_content_formula', question.question_content_formula),
            ('answer_options_image', question.answer_options_image),
            ('answer_options_video', question.answer_options_video),
            ('answer_options_audio', question.answer_options_audio),
            ('answer_options_formula', question.answer_options_formula),
            ('answer_explanation_image', question.answer_explanation_image),
        ]

        # Handle all resource file uploads
        for resource_key, resource_relation in resource_mappings:
            # Find all keys in request.FILES matching the resource type
            resource_files = []
            file_keys = [key for key in request_files.keys() if key.startswith(resource_key)]

            for key in file_keys:
                # Extract file from request
                file = request_files[key]

                # Create ResourceFile instance with name and thumbnail
                resource_file = ResourceFile.objects.create(
                    file=file,
                    name=file.name, # Use the original filename
                    description='',
                    owner=self.context['request'].user,
                    thumbnail=file # You might want to customize thumbnail generation
                )

                resource_files.append(resource_file)

            # Set resources for this relation if any exist
            if resource_files:
                resource_relation.set(resource_files)

        return question

    def update(self, instance, validated_data):
        # Get request FILES and POST data
        request_files = self.context['request'].FILES
        request_data = self.context['request'].data

        # Text fields to handle
        text_fields = [
            'question_content_text',
            'answer_options_text',
            'answer_explanation_text'
        ]

        # Resource file types to handle
        resource_mappings = [
            ('question_content_image', instance.question_content_image),
            ('question_content_video', instance.question_content_video),
            ('question_content_audio', instance.question_content_audio),
            ('question_content_formula', instance.question_content_formula),
            ('answer_options_image', instance.answer_options_image),
            ('answer_options_video', instance.answer_options_video),
            ('answer_options_audio', instance.answer_options_audio),
            ('answer_options_formula', instance.answer_options_formula),
            ('answer_explanation_image', instance.answer_explanation_image),
        ]

        # Remove text and resource-related data from validated_data
        for field in text_fields:
            validated_data.pop(field, None)

        for resource_key, _ in resource_mappings:
            validated_data.pop(resource_key, None)

        # Handle text fields with array-like keys
        for field in text_fields:
            # Collect all values for this field
            field_values = []

            # Check for keys like 'field[0]', 'field[1]', etc.
            for key in request_data.keys():
                if key.startswith(f'{field}[') and key.endswith(']'):
                    field_values.append(request_data[key])

            # Convert to JSON string if values exist
            if field_values:
                validated_data[field] = json.dumps(field_values)

        # Update basic fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Handle all resource file uploads
        for resource_key, resource_relation in resource_mappings:
            # Clear existing resources
            resource_relation.clear()

            # Find all keys in request.FILES matching the resource type
            resource_files = []
            file_keys = [key for key in request_files.keys() if key.startswith(resource_key)]

            for key in file_keys:
                # Extract file from request
                file = request_files[key]

                # Create ResourceFile instance with name and thumbnail
                resource_file = ResourceFile.objects.create(
                    file=file,
                    name=file.name,
                    description='',
                    owner=self.context['request'].user,
                    thumbnail=file
                )

                resource_files.append(resource_file)

            # Set resources for this relation if any exist
            if resource_files:
                resource_relation.set(resource_files)

        return instance

    class Meta:
        model = Question
        fields = [
            "id",
            "title",
            "eval_skill",
            "qn_num",
            "qn_type",
            "score",
            "status",
            "head",
            "statement",
            "question_content_text",
            "question_content_image",
            "question_content_video",
            "question_content_audio",
            "question_content_formula",
            "answer_content_is_char_limited",
            "answer_content_model_answer",
            "answer_options_text",
            "answer_options_image",
            "answer_options_video",
            "answer_options_audio",
            "answer_options_formula",
            "answer_explanation_text",
            "answer_explanation_image",
            "question_group",
            "assigned_at",
            "reviewed_at",
            "reason",
            "question_metadata",
            "category",
            "owner",
            "created_at",
            "updated_at"
        ]

    def get_url(self, item):
        request = self.context.get('request')
        file_url = item.file.url
        return request.build_absolute_uri(file_url)

    def to_representation(self, instance):

        data = super().to_representation(instance)
        data["first_name"] = instance.owner.first_name if instance.owner else None
        data["last_name"] = instance.owner.last_name if instance.owner else None
        data["category"] = instance.category.name if instance.category else None
        data["question_content_image"] = [
            self.get_url(item) for item in instance.question_content_image.all()
        ] if instance.question_content_image else None
        data["question_content_video"] = [
            self.get_url(item) for item in instance.question_content_video.all()
        ] if instance.question_content_video else None
        data["question_content_audio"] = [
            self.get_url(item) for item in instance.question_content_audio.all()
        ] if instance.question_content_audio else None
        data["question_content_formula"] = [
            self.get_url(item) for item in instance.question_content_formula.all()
        ] if instance.question_content_formula else None
        data["answer_options_image"] = [
            self.get_url(item) for item in instance.answer_options_image.all()
        ] if instance.answer_options_image else None
        data["answer_options_video"] = [
            self.get_url(item) for item in instance.answer_options_video.all()
        ] if instance.answer_options_video else None
        data["answer_options_audio"] = [
            self.get_url(item) for item in instance.answer_options_audio.all()
        ] if instance.answer_options_audio else None
        data["answer_options_formula"] = [
            self.get_url(item) for item in instance.answer_options_formula.all()
        ] if instance.answer_options_formula else None
        data["answer_explanation_image"] = [
            self.get_url(item) for item in instance.answer_explanation_image.all()
        ] if instance.answer_explanation_image else None
        return data


class TestPaperCategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = TestPaperCategory
        fields = ['id', 'name', 'description', 'parent', 'owner', 'created_at', 'updated_at', 'is_deleted', 'is_starred', 'extras', 'children']

    def get_children(self, obj):
        if obj.children:
            return TestPaperCategorySerializer(obj.children.filter(is_deleted=False), many=True).data
        return None

if instance.test_category:
    category_serializer = TestPaperCategorySerializer(instance.test_category)
    data['test_category'] = category_serializer.data
else:
    data['test_category'] = None