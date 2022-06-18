import pytest
from brownie.test import given, strategy
from brownie import accounts

#basic sample fuzz test using hypothesis
#it runs the function with random values for  number to store and random account for storing!
#the amount of times it runs depends on the number specified in the brownie config.
#The longer the runs the longer the tests
@given(number=strategy("uint256"), acct=strategy("address"))
def test_store_your_number(SimpleStorage, number, acct):
    simple_storage = SimpleStorage.deploy({"from": accounts[0]})

    store_tx = simple_storage.storeYourNumber(number, {"from": acct})
    store_tx.wait(1)

    number_for_address = simple_storage.retrieveYourNumber(acct.address)

    assert number_for_address == number
