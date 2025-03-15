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
    return render(request, 'results/go-result.html')


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
        # data = json.loads(request.body)
        
        # for offer in offers:
        #     table = PrettyTable()
        #     table.field_names = ["Flight No", "From", "To", "Departure", "Arrival", "Duration", "Aircraft", "Stops"]

        #     for itinerary in offer["itineraries"]:
        #         for segment in itinerary["segments"]:
        #             table.add_row([
        #                 f"{segment['carrierCode']}{segment['number']}",
        #                 segment["departure"]["iataCode"],
        #                 segment["arrival"]["iataCode"],
        #                 segment["departure"]["at"],
        #                 segment["arrival"]["at"],
        #                 segment["duration"],
        #                 segment["aircraft"]["code"],
        #                 segment["numberOfStops"]
        #             ])

        #     # Pricing details
        #     table_price = PrettyTable()
        #     table_price.field_names = ["Currency", "Base Price", "Total Price"]
        #     table_price.add_row([offer["price"]["currency"], offer["price"]["base"], offer["price"]["total"]])

        #     print("Flight Information")
        #     print(table)
        #     print("\nPricing Information")
        #     print(table_price)

        # Mock data (keyin database bilan almashtirish mumkin)
        mock_flights = [
            {
                "id": 1,
                "departure": "TAS",
                "arrival": "LHR",
                "departure_time": "2023-10-15 08:00",
                "arrival_time": "2023-10-15 14:00",
                "duration": "6h",
                "airline": "Uzbekistan Airways",
                "flight_number": "UZ123",
                "price": 450,
                "baggage": "20kg",
                "hand_luggage": "7kg",
            },
            {
                "id": 2,
                "departure": "TAS",
                "arrival": "JFK",
                "departure_time": "2023-10-15 10:00",
                "arrival_time": "2023-10-15 22:00",
                "duration": "12h",
                "airline": "Turkish Airlines",
                "flight_number": "TK456",
                "price": 750,
                "baggage": "30kg",
                "hand_luggage": "8kg",
            },
        ]
        
        
        return render(
            request=request,
            template_name='results/go-result.html',
            context={
                'offers':offers,
                'flights':mock_flights
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