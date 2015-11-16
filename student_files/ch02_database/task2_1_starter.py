"""

      task2_1_starter.py   -   Python Database API 2.0

      Reads data from school.db by providing a get_location() function and a partial or full
      name of a school.

      Data returned from the search of the database returns name, city, and state for all
      matching results.

      Uses a named tuple to store school data.



      Instructions:
      1. Begin by creating a named tuple.  Refer back to chapter 1 in the notes about named
         tuples for specifics on how to create a named tuple.  The named tuple should contain
         fields such as: school_id, name, city, state, country

      2. Within the provided get_location function, you should:
         a) Obtain a connection to the database.
         b) Obtain a cursor.
         c) Execute a query.  Use the following SQL to help generate results:

         "SELECT fullname, city, state FROM schools WHERE fullname like '%{0}%'".format(school_name)

         d) Fetch the records.
         e) Convert the results into a list of named tuples and return the list from get_location.

         Refer to the slide within the student manual entitled "Accessing Data" for
         help with proper db API syntax--including proper exception handling

      3. Ask the user for a school name, invoke the get_location() function and pass the user's
         input value into it.  Verify it returns expected results and display the results.

"""


def get_location(school_name):
    school_data = []
    connection = None


    # place db query solution here

    return school_data


# retrieve user school name input, perform db query

# display results

