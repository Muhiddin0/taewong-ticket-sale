import amadeus
from amadeus import Client, ResponseError

amadeus_client = Client(
    client_id="ECnxgFlA8NG1rolz4kGnHAKKSEZKJOrA", client_secret="l1ZV7KXA1bSnq1hg"
)



response = amadeus_client.shopping.flight_offers_search.get(
    originLocationCode="TAS",
    destinationLocationCode="IST",
    departureDate="2025-04-10",
    adults=1,
    children=1,
    infants=1,
    currencyCode="USD",
)

print(response.body)  # JSON javobni ko'rish




# def search_flights(
#     origin: str,
#     destination: str,
#     departure_date: str,
#     adults: int = 1,
#     currency: str = "USD",
# ):
#     """
#     Amadeus API orqali aviachipta qidirish funksiyasi.

#     :param origin: Boshlang'ich aeroport IATA kodi (masalan: 'TAS' - Toshkent).
#     :param destination: Borish aeroport IATA kodi (masalan: 'IST' - Istanbul).
#     :param departure_date: Uchish sanasi ('YYYY-MM-DD' formatida).
#     :param adults: Yo'lovchilar soni (standart: 1).
#     :param currency: Narx valyutasi (standart: USD).
#     :return: Aviachipta variantlari JSON formatida.
#     """
#     amadeus_client = Client(
#         client_id="ECnxgFlA8NG1rolz4kGnHAKKSEZKJOrA", client_secret="l1ZV7KXA1bSnq1hg"
#     )

#     try:
#         response = amadeus_client.shopping.flight_offers_search.get(
#             originLocationCode=origin,
#             destinationLocationCode=destination,
#             departureDate=departure_date,
#             adults=adults,
#             currencyCode=currency,
#         )

#         return response.data
#     except ResponseError as error:
#         return {"error": str(error)}


# # Foydalanish misoli:
# if __name__ == "__main__":
#     flights = search_flights("TAS", "IST", "2025-04-10", 1)
#     print(flights)
