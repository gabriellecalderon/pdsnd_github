### Date created
June 6, 2019

### Project Title
Analyzing Bikeshare Data

### Description
This project generates some summary statistics about bikeshare usage in the cities of Chicago, New York City, and Washington using raw data of individual trips as input.
Some statistics generated are:

 - The most popular hour for rides to start
 - The average travel time for bikeshare trips
 - A breakdown of the gender of bikeshare users

The script allows users to filter data by month or day of the week if desired.

### Files used

- `bikeshare.py`: The python script that users interact with to view the summary data
- `chicago.csv`: Bikeshare data from Chicago
- `washington.csv`: Bikeshare data from Washington
- `new_york_city.csv`: Bikeshare data from New York City

### Credits
I used the pandas documentation to refresh on some functions, particularly `df.sample()` to get the random rows of user data.
I used Stack Overflow to learn how to join two pandas string columns together into one.

All the pages I visited are:
[https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.weekday.html]
[https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mode.html]
[http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.to_dict.html]
[https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.sample.html]

[https://stackoverflow.com/questions/11858472/string-concatenation-of-two-pandas-columns]
