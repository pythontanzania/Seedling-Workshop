from django.shortcuts import get_object_or_404, redirect, render

from .models import Fundraiser, Payment, Pledge


def home(request):
    fundraisers = Fundraiser.objects.order_by("-created")
    return render(request, "fundraisers/home.html", {"fundraisers": fundraisers})


def fundraiser_detail(request, fundraiser_id):
    fundraiser = get_object_or_404(Fundraiser, id=fundraiser_id)
    pledges = fundraiser.pledges.order_by("name")
    return render(request, "fundraisers/fundraiser_detail.html", {"fundraiser": fundraiser, "pledges": pledges})
