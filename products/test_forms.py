# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):

    def test_comment_body_is_not_required(self):
        form = CommentForm({'name': 'test body'})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertNotEqual(form.Meta.fields, ['body'])
