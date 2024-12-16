from django.db import models

from lecture.models import ResourceFile
from user_auth.models import AuthUser, BaseModel
from utils.enums import MetaDataInput, MetaDataType, QuestionStatus, QuestionType


class Metadata(BaseModel):
    type = models.CharField(max_length=2, choices=MetaDataType.choices(), default=MetaDataType.GENERAL_CONTENT.value, )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    input_method = models.CharField(max_length=10, choices=MetaDataInput.choices(), default=MetaDataInput.INPUT.value, )
    is_required = models.BooleanField(default=True)
    value_text = models.TextField(null=True, blank=True)
    value_radio = models.CharField(max_length=255, null=True, blank=True)
    value_dropdown = models.CharField(max_length=255, null=True, blank=True)
    value_checkbox = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(AuthUser, on_delete=models.SET_NULL, blank=True, null=True, related_name="metadata_owner")

    class Meta:
        db_table = "metadata"
        verbose_name = "Metadata"

    def __str__(self):
        return self.name


class QuestionCategory(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey("self", related_name="children", on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(AuthUser, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = "question_category"
        verbose_name = "Question Category"

    def __str__(self):
        return self.name


class QuestionGroup(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    eval_skill = models.CharField(max_length=2, choices=MetaDataType.choices(), default=MetaDataType.GENERAL_CONTENT.value, )
    head = models.CharField(max_length=1000)
    owner = models.ForeignKey(AuthUser, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(QuestionCategory, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "question_group"
        verbose_name = "Question Group"

    def __str__(self):
        return self.name


class Question(BaseModel):
    title = models.CharField(max_length=100, null=True, blank=True)
    eval_skill = models.CharField(max_length=2, choices=MetaDataType.choices(), default=MetaDataType.GENERAL_CONTENT.value, )
    qn_num = models.IntegerField(blank=True, null=True)
    qn_type = models.CharField(max_length=10, choices=QuestionType.choices(), default=QuestionType.SINGLE_CHOICE.value, )
    score = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=QuestionStatus.choices(), default=QuestionStatus.CREATED.value, )
    head = models.CharField(max_length=1000)
    statement = models.TextField(blank=True, null=True)

    question_content_text = models.TextField(null=True, blank=True)
    question_content_image = models.ManyToManyField(ResourceFile, blank=True,
                                             related_name="question_content_image", )
    question_content_video = models.ManyToManyField(ResourceFile, blank=True,
                                             related_name="question_content_video", )
    question_content_audio = models.ManyToManyField(ResourceFile, blank=True,
                                             related_name="question_content_audio", )
    question_content_formula = models.ManyToManyField(ResourceFile, blank=True,
                                                 related_name="question_content_formula", )

    answer_content_is_char_limited = models.BooleanField(default=False)
    answer_content_model_answer = models.TextField(null=True, blank=True)

    answer_options_text = models.TextField(null=True, blank=True)
    answer_options_image = models.ManyToManyField(ResourceFile, blank=True, related_name="answer_options_image", )
    answer_options_video = models.ManyToManyField(ResourceFile, blank=True, related_name="answer_options_video", )
    answer_options_audio = models.ManyToManyField(ResourceFile, blank=True, related_name="answer_options_audio", )
    answer_options_formula = models.ManyToManyField(ResourceFile, blank=True,
                                             related_name="answer_options_formula", )

    answer_explanation_text = models.TextField(null=True, blank=True)
    answer_explanation_image = models.ManyToManyField(ResourceFile, blank=True,
                                                 related_name="answer_explanation_image", )

    question_group = models.ForeignKey(QuestionGroup, on_delete=models.SET_NULL, null=True, blank=True)

    assigned_at = models.DateTimeField(blank=True, null=True)
    reviewed_at = models.DateTimeField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    question_metadata = models.ForeignKey(Metadata, on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(QuestionCategory, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(AuthUser, on_delete=models.SET_NULL, blank=True, null=True, related_name="owner")
    reviewers = models.ForeignKey(AuthUser, on_delete=models.SET_NULL, blank=True, null=True, related_name="reviewers")

    class Meta:
        db_table = "question"
        verbose_name = "Question"

    def __str__(self):
        return self.title
