from django.shortcuts import render
from .models import Airport, priceType, priceTemplate
from .forms import FlightSearchForm
import requests
import json

# Create your views here.
def home(request):
    return render(request, 'base.html', {})

def flight_search_form(request):
    form = FlightSearchForm(request.POST)
    if request.method == 'POST':
        departureStation = request.POST.get('departureStation')
    return render(request, 'wizz/search_form.html', {
        'form': form
})

def wizz(request):
    # request to wizzair website
    # request_url = "https://be.wizzair.com/7.5.2/Api/search/timetable"
    # head = {'content-type': 'application/json'}
    # payload = {"flightList":[{"departureStation":"IEV","arrivalStation":"BUD","from":"2017-11-20","to":"2017-12-03"},{"departureStation":"BUD","arrivalStation":"IEV","from":"2017-11-27","to":"2017-12-31"}],"priceType":"regular"}
    # req = requests.post(request_url, headers=head, data=json.dumps(payload))
    # req_content1 = req.content

    data = {"outboundFlights":[{"departureStation":"IEV","arrivalStation":"BUD","departureDate":"2017-11-20T00:00:00","price":{"amount":2619.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-11-20T07:10:00"],"classOfService":"J","hasMacFlight":False},{"departureStation":"IEV","arrivalStation":"BUD","departureDate":"2017-11-22T00:00:00","price":{"amount":1889.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-11-22T07:10:00"],"classOfService":"KL","hasMacFlight":False},{"departureStation":"IEV","arrivalStation":"BUD","departureDate":"2017-11-24T00:00:00","price":{"amount":1599.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-11-24T07:10:00"],"classOfService":"LB","hasMacFlight":False},{"departureStation":"IEV","arrivalStation":"BUD","departureDate":"2017-11-25T00:00:00","price":{"amount":1449.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-11-25T07:10:00"],"classOfService":"B","hasMacFlight":False},{"departureStation":"IEV","arrivalStation":"BUD","departureDate":"2017-11-26T00:00:00","price":{"amount":1449.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-11-26T07:10:00"],"classOfService":"B","hasMacFlight":False},{"departureStation":"IEV","arrivalStation":"BUD","departureDate":"2017-11-27T00:00:00","price":{"amount":2319.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-11-27T07:10:00"],"classOfService":"JK","hasMacFlight":False},{"departureStation":"IEV","arrivalStation":"BUD","departureDate":"2017-11-29T00:00:00","price":{"amount":2909.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-11-29T07:10:00"],"classOfService":"IJ","hasMacFlight":False},{"departureStation":"IEV","arrivalStation":"BUD","departureDate":"2017-12-01T00:00:00","price":{"amount":1749.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-01T07:10:00"],"classOfService":"L","hasMacFlight":False},{"departureStation":"IEV","arrivalStation":"BUD","departureDate":"2017-12-02T00:00:00","price":{"amount":1449.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-02T07:10:00"],"classOfService":"B","hasMacFlight":False},{"departureStation":"IEV","arrivalStation":"BUD","departureDate":"2017-12-03T00:00:00","price":{"amount":2039.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-03T07:10:00"],"classOfService":"K","hasMacFlight":False}],"returnFlights":[{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-11-27T00:00:00","price":{"amount":1889.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-11-27T08:20:00"],"classOfService":"KL","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-11-29T00:00:00","price":{"amount":1749.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-11-29T08:20:00"],"classOfService":"L","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-01T00:00:00","price":{"amount":999.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-01T08:20:00"],"classOfService":"OP","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-02T00:00:00","price":{"amount":1749.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-02T08:20:00"],"classOfService":"L","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-03T00:00:00","price":{"amount":1599.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-03T08:20:00"],"classOfService":"LB","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-04T00:00:00","price":{"amount":2039.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-04T08:20:00"],"classOfService":"K","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-06T00:00:00","price":{"amount":2619.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-06T08:20:00"],"classOfService":"J","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-07T00:00:00","price":{"amount":1599.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-07T08:20:00"],"classOfService":"LB","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-08T00:00:00","price":{"amount":799.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-08T08:20:00"],"classOfService":"PR","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-09T00:00:00","price":{"amount":1149.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-09T08:20:00"],"classOfService":"O","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-10T00:00:00","price":{"amount":1749.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-10T08:20:00"],"classOfService":"L","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-11T00:00:00","price":{"amount":1599.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-11T08:20:00"],"classOfService":"LB","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-12T00:00:00","price":{"amount":1449.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-12T08:20:00"],"classOfService":"B","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-13T00:00:00","price":{"amount":1149.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-13T08:20:00"],"classOfService":"O","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-15T00:00:00","price":{"amount":1149.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-15T08:20:00"],"classOfService":"O","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-16T00:00:00","price":{"amount":1149.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-16T08:20:00"],"classOfService":"O","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-17T00:00:00","price":{"amount":2039.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-17T08:20:00"],"classOfService":"K","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-18T00:00:00","price":{"amount":1889.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-18T08:20:00"],"classOfService":"KL","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-19T00:00:00","price":{"amount":1599.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-19T08:20:00"],"classOfService":"LB","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-20T00:00:00","price":{"amount":1889.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-20T08:20:00"],"classOfService":"KL","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-21T00:00:00","price":{"amount":2039.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-21T08:20:00"],"classOfService":"K","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-22T00:00:00","price":{"amount":1749.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-22T08:20:00"],"classOfService":"L","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-23T00:00:00","price":{"amount":1889.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-23T08:20:00"],"classOfService":"KL","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-24T00:00:00","price":{"amount":1889.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-24T08:20:00"],"classOfService":"KL","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-26T00:00:00","price":{"amount":2319.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-26T08:20:00"],"classOfService":"JK","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-27T00:00:00","price":{"amount":2619.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-27T08:20:00"],"classOfService":"J","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-28T00:00:00","price":{"amount":1889.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-28T08:20:00"],"classOfService":"KL","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-29T00:00:00","price":{"amount":1889.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-29T08:20:00"],"classOfService":"KL","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-30T00:00:00","price":{"amount":1749.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-30T08:20:00"],"classOfService":"L","hasMacFlight":False},{"departureStation":"BUD","arrivalStation":"IEV","departureDate":"2017-12-31T00:00:00","price":{"amount":1599.00,"currencyCode":"UAH"},"priceType":"price","departureDates":["2017-12-31T08:20:00"],"classOfService":"LB","hasMacFlight":False}]}

    dict1 = json.dumps(data)
    req_content = json.loads(dict1)
    return render(request, 'wizz/results.html', {
        'req_content': req_content,
        })
