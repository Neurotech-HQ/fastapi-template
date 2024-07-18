# Schemas

Schemas are used to validate the data that is sent to the API. The schemas are defined as pydantic models. The schemas can be used to validate the request body, query parameters, and response data.

Schemas help in defining the structure of the data that is sent to the API. They help in ensuring that the data is in the correct format and that it meets the requirements of the API.

Create a module for a group of schemas. For example, if you have schemas for user data, create a `user` module.

## The structure of the module

- schemas
  - user
  - business
  - Other schemas
