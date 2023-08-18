from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Leads, Agent
from .forms import LeadModelFormReg


def home_page(request):
    return render(request, "index.html")


def view_leads(request):
    leads = Leads.objects.all()

    context = {
        'leads': leads
    }
    return render(request, "leads.html", context)


def get_lead_details_by_index(request, pk):
    lead = Leads.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, 'lead_detail.html', context)


def lead_create(request):
    form = LeadModelFormReg()
    if request.method == "POST":
        print("Receiving a post request")
        form = LeadModelFormReg(request.POST)
        if form.is_valid():
            form.save()
            print("A lead has been Created")
            return redirect("/leads")

    else:
        context = {
            "form": form
        }
    return render(request, "lead_create.html", context)


def lead_update_view(request, pk):
    lead = Leads.objects.get(id=pk)

    form = LeadModelFormReg(instance=lead)
    if request.method == "POST":
        form = LeadModelFormReg(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "lead": lead,
        "form": form
    }

    return render(request, "lead_update.html", context)


def lead_delete_view(request, pk):
    lead = Leads.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")