from collections import defaultdict
from typing import Any
from .models import Patient
from datetime import datetime


def count_average_age_of_operation() -> int:
    def inner(dop: int, dob: int) -> int:
        dob_dt = datetime.utcfromtimestamp(dob)
        dop_dt = datetime.utcfromtimestamp(dop)
        return (dop_dt - dob_dt).days // 365

    ages: list[int] = [
            inner(p.date_operation, p.date_of_birthday)
            for p in Patient.objects.all()
            if not p.is_pregnant
    ]

    average_age: int = sum(ages) // len(ages)
    return average_age


def count_gender_percentage() -> tuple[float, float, float]:
    patients: list[Patient] = Patient.objects.all()
    genders_count: list[int] = [0, 0, 0]

    for patient in patients:
        genders_count[patient.gender] += 1

    return tuple([
        (gender_count / len(patients)) * 100
        for gender_count in genders_count
    ])



def count_most_frequent_drug_before_operation() -> tuple[str, float]:
    cache: defaultdict[str, list[float]] = defaultdict(lambda: [0, 0])
    patients: list[Patient] = Patient.objects.all()

    for patient in patients:
        if patient.pretreatment_drug is None or patient.pretreatment == 0:
            continue

        drug_name: str = (patient.pretreatment_drug
                            .replace("registration_pretreatment_name_", ""))

        drug_doze: float = patient.pretreatment
        cache[drug_name][0] += 1
        cache[drug_name][1] += drug_doze

    max_count = max(i[0] for i in cache.values())
    result = [k for k, v in cache.items() if v[0] == max_count][0]

    return tuple([result, cache[result][1] / max_count])


def count_most_frequent_drug_after_operation() -> tuple[str, float]:
    cache: defaultdict[str, list[float]] = defaultdict(lambda: [0, 0])
    patients: list[Patient] = Patient.objects.all()

    for patient in patients:
        if patient.treatment_drug is None or patient.treatment == 0:
            continue

        drug_name: str = patient.treatment_drug
        drug_doze: float = patient.treatment

        cache[drug_name][0] += 1
        cache[drug_name][1] += drug_doze

    max_count = max(i[0] for i in cache.values())
    result = [k for k, v in cache.items() if v[0] == max_count][0]

    return tuple([result, cache[result][1] / max_count])


def count_most_frequent_operation_type() -> str:
    return _get_most_friquent_field(Patient, "operation")


def count_most_frequent_pathology_name() -> str:
    return _get_most_friquent_field(Patient, "pathology_name")


def _get_most_friquent_field(cls, field_name) -> Any:
    cache: defaultdict[Any, int] = defaultdict(lambda: 0)
    objects: list[cls] = cls.objects.all()

    for o in objects:

        field_value: Any = getattr(o, field_name)
        if field_value is not None and type(field_value) == str:
            field_value = field_value.replace("edit_op_", "")

        if field_value is None:
            continue

        cache[field_value] += 1

    return max(cache, key=cache.get)


