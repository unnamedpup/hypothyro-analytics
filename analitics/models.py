from django.db import models


def _get_fileds_as_str(obj) -> str:
    fields = [
            f"{k}: {v}"
            for k, v in vars(obj).items()
            if not k.startswith("_")
    ]

    return ", ".join(fields)


# Create your models here.
class Notification(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.BigIntegerField(blank=True, null=True)
    patient_id = models.BigIntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    text = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification'

    def __repr__(self) -> str:
        return _get_fileds_as_str(self)

    __str__ = __repr__


class Patient(models.Model):
    id = models.BigIntegerField(primary_key=True)
    can_be_pregnant = models.BooleanField(blank=True, null=True)
    checkinterval = models.FloatField(blank=True, null=True)
    date_of_birthday = models.BigIntegerField(blank=True, null=True)
    date_operation = models.BigIntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    is_pregnant = models.BooleanField(blank=True, null=True)
    lowthslev = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    operation = models.CharField(max_length=255, blank=True, null=True)
    pathology_name = models.CharField(max_length=255, blank=True, null=True)
    pretreatment = models.FloatField(blank=True, null=True)
    pretreatment_drug = models.CharField(max_length=255, blank=True, null=True)
    ths_date = models.BigIntegerField(blank=True, null=True)
    ths_result = models.FloatField(blank=True, null=True)
    treatment = models.FloatField(blank=True, null=True)
    treatment_drug = models.CharField(max_length=255, blank=True, null=True)
    upthslev = models.FloatField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'

    def __repr__(self) -> str:
        return _get_fileds_as_str(self)

    __str__ = __repr__

