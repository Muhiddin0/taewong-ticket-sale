import json

from django.shortcuts import render
from django.http import JsonResponse

from amadeus import Client, ResponseError, Location
from data import offers

from prettytable import PrettyTable

amadeus = Client(
    client_id="ECnxgFlA8NG1rolz4kGnHAKKSEZKJOrA", client_secret="l1ZV7KXA1bSnq1hg"
)


def test(request):

    return render(request, 'results/go-result.html', {
        'offers':offers
    })


def IATA(request):
    q = request.GET.get("query", "")  # Get the 'q' parameter, default to an empty string if not provided

    try:
        response = amadeus.reference_data.locations.get(
            keyword={q},
            subType=Location.AIRPORT
        )
        return JsonResponse({
            "status":True,
            "data":response.data
        })
    except ResponseError as error:
        return JsonResponse({
            "status": False,
            "data": str(error)
        })


def go_form(request):

    if request.method == "GET":
        return render(
            request=request,
            template_name='forms/go.html',
            context={}
        )
    if request.method == 'POST':
        data = request.POST
        print("🚀 ~ file: views.py:52 ~ data:", data)
        
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode="TAS",
            destinationLocationCode="IST",
            departureDate="2025-04-10",
            adults=1,
            children=1,
            infants=1,
            currencyCode="USD",
        )
        
        # response = amadeus.shopping.flight_offers_search.get(
        #     originLocationCode=data.get('from'),
        #     destinationLocationCode=data.get('to'),
        #     departureDate=data.get('date'),
        #     adults=data.get('adults'),
        #     children=data.get('children'),
        #     infants=data.get('infants'),
        #     currencyCode="USD",
        # )
        
        print("🚀 ~ file: views.py:55 ~ response:", response)

        return render(
            request=request,
            template_name='results/go-result.html',
            context={
                'offers': offers,
            }
        )

# Create your views here.
def go_and_come_form(request):

    return render(
        request=request,
        template_name='forms/go-and-come.html',
        context={}
    )


def hard_roudemap_form(request):

    return render(
        request=request,
        template_name='forms/hard-roudmap.html',
        context={}
    )