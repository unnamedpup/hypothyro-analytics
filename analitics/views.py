from django.shortcuts import render
from django.http import HttpResponse
from .analitics_service import (
        count_average_age_of_operation, count_gender_percentage,
        count_most_frequent_drug_before_operation, count_most_frequent_drug_after_operation,
        count_most_frequent_operation_type, count_most_frequent_pathology_name
)

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")


def average_age_of_operation(request):
    return HttpResponse(
            "Average age of operation: "
            f"{count_average_age_of_operation()}")


def gender_percentage(request) -> tuple[int, int, int]:
    genders = count_gender_percentage()
    return HttpResponse(
            "Gender percentage: "
            f"Male: {genders[0]:.2f}%, Female: {genders[1]:.2f}%, Other: {genders[2]:.2f}%")


def most_frequent_drug_before_operation(request):
    drug, doze = count_most_frequent_drug_before_operation()
    return HttpResponse(f"Pretretment drug name: {drug}, doze: {doze:.2f}")


def most_frequent_drug_after_operation(request):
    drug, doze = count_most_frequent_drug_after_operation()
    return HttpResponse(f"Treatment drug name: {drug}, doze: {doze:.2f}")


def most_frequent_operation_type(request):
    result = count_most_frequent_operation_type()
    return HttpResponse(f"Most frequent operation type: {result}")


def most_frequent_pathology_name(request):
    result = count_most_frequent_pathology_name()
    return HttpResponse(f"Most frequent pathology name: {result}")


