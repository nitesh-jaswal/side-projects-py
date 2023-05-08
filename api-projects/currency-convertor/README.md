# Currency Convertor

Your aim is to create an API that performs currency conversions from various supported currencies. The API should be dynamic and must have two endpoints. 

1. `GET /convert/{from}/{to}?=value`
  This endpoint should support only a `GET` operation and should be in the format specified above. It must return the converted value of the currency based on the `from` and `to` path parameters

2. `POST /update/{from}/{to}?=value`
  This endpoint must perform Basic Authentication and if the auth succeeds then automatically update the values for the currency conversion

The above requirement is the end goal of the project excercise. But the project will be built in steps with increasing complexity based on the version number starting with the simplest way to re-imagine the problem.

## Versions

1. **Version 1**: 
  * Make a python module that has hard-coded values for INR to USD and USD to INR conversion. Feel free to add as many other combinations of currencies that you want. 
  * The module must have a function called convert that takes in two string parameters indicating `from` and `to` values of the currency to exchange and a non-negative integer `value` of the amount to be converted.
  * Return the converted value(`float`) along with the rate of conversion(`float`)