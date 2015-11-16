"""

      task1_1_starter.py   -   Python Basics Overview

      Reads data from resources/cities15000.txt (a tsv file).
      Determines the largest city and highest city.
      Allows for searching by city names to determine a city population.


      Helpful hints:
      1. Examine the file cities15000.txt.  Choose an appropriate data structure to hold
         the data to be read.  Declare this variable near the top of the module.

      2. Read from the data file into this data structure.  Be sure to use proper error handling
         as discussed in the materials.  The data you choose to store in your data structure
         is up to you, however, at a minimum, you should store the population and elevation
         within the data structure.  These are the 15th and 16th fields (columns) respectively.
         Also note: you will need to read a record and split on a TAB ('\t') since this file is
         a tab-separated value file.

      3. To find the largest city, sort the data structure by population and take the first element.

      4. To find the highest city, sort the data structure by elevation and take the first element.

         Tip: As an example of sorting, the following would sort by country:

                key=lambda k: cities[k][8]      <-- where cities is a dictionary containing the
                                                    cities (organized by city name, k)
                                                    and 8 is the 9th column, containing the country.

      5. To create a search(), ask for user input to input a city name.  You can use
         the string method: capitalize() to capitalize the city name.

      6. Pass the name of the city into your data structure to return the data record.

      7. Display the results.

"""