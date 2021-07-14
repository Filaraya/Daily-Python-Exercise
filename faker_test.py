"""Faker is a Python package that generates fake data for you."""
from faker import Faker
fake = Faker()
# create a list of names
names = []
for name in range(1, 4):
    name = fake.name()
    names.append(name)
print("list of names:\n", names)
# create a list of countries
countries = []
for country in range(1, 4):
    country = fake.country()
    countries.append(country)
print("list of countries:\n", countries)
# create a sample of emails
emails = []
for email in range(1, 4):
    email = fake.email()
    emails.append(email)
print("list of emails:\n", emails)
# create a sample of address
addresses = []
for address in range(1, 4):
    address = fake.address()
    addresses.append(address)
print("list of addresses:\n", addresses)
# create a sample of text
print("sample of text:\n", fake.text())
