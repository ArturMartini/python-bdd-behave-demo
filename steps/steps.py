from behave import given, when, then
import requests
import json
import random

from assertpy import assert_that

url = "http://localhost:8080/v1/partners"

@given("I wanna create partner")
def create_partner(context):
    context.partner = {}


@given("The id is {id}")
def step_impl(context, id):
    if id == "random":
        id = str(random.randint(1000000000, 9999999999))
    context.partner.update({"id": id})


@given("The trading name is {tradingName}")
def step_impl(context, tradingName):
    context.partner.update({"tradingName": tradingName})


@given("The owner name is {ownerName}")
def step_impl(context, ownerName):
    context.partner.update({"ownerName": ownerName})


@given("The document is {document}")
def step_impl(context, document):
    if document == "random":
        document = str(random.randint(1000000000, 9999999999))
    context.partner.update({"document": document})


@given("The address is {lat} and {log}")
def step_impl(context, lat, log):
    context.partner.update({"address": {"type": "Point", "coordinates": [float(lat), float(log)]}})


@given("The coverage area is {coordinates}")
def step_impl(context, coordinates):
    arrayCoordinates = []
    for c in coordinates.replace("'", "").split(","):
        arrayCoordinates.append(float(c))

    context.partner.update({"coverageArea": {"type": "MultiPolygon", "coordinates": [[[arrayCoordinates]]]}})


@when("I send request to create partners")
def step_impl(context):
    print(json.dumps(context.partner))
    context.response = requests.post(url, data=json.dumps(context.partner))


@then("The result response code should be {code}")
def step_impl(context, code):
    try:
        assert_that(context.response.status_code).is_equal_to(int(code))
    except:
        print(context.response.json())
        assert False


@then("The result body must be")
def step_impl(context):
    resp = context.response.json()
    for row in context.table:
        assert_that(str(resp[row[0]].replace("'", ""))).is_equal_to(str(row[1]))
