# Utilities

This contains the utility functions that are used across the application. The processing logic of the application can be defined here.

Create a module for a group of utility functions. For example, if you have utility functions for working with files, create a `files` module.

Define the processing logics in this module. Eg fetch data from the database then process it and return the result.

## The structure of the module

The structure can be as follows:

    - utilities
        - user
            - user.py
            - user_validation.py
            - analytics.py
        - formatter
        - Other files
