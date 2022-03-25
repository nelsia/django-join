from unittest.util import _MAX_LENGTH
from rest_framework import serializers

from myapp.models import Record


class RecordSerializer(serializers.ModelSerializer):
  customer_name = serializers.CharField(label="customer_name", max_length=100)

  class Meta:
    model = Record
    fields = ["id", "phone_number", "customer_name"]
