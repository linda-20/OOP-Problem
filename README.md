
# Competitive Eating Competition Scoreboard

You are the judge at a competitive eating competition, where participants consume three types of food: chicken wings, hamburgers, and hotdogs. Each type of food is worth a different amount of points:

- Chickenwings: 5 points
- Hamburgers: 3 points
- Hotdogs: 2 points

## Function Description

Write a Python function that helps you create a scoreboard for the competition. The function should take a list of participant objects as a parameter. Each participant object contains the following properties:

- `name`: The name of the participant.
- `chickenwings`: The number of chicken wings consumed by the participant.
- `hamburgers`: The number of hamburgers consumed by the participant.
- `hotdogs`: The number of hotdogs consumed by the participant.

The function should return a list of participant objects with their names and scores sorted by score. If two participants have the same score, they should be sorted alphabetically by name.

Example Input:
[
{"name": "Habanero Hillary", "chickenwings": 5, "hamburgers": 17, "hotdogs": 11},
{"name": "Big Bob", "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}
]

Example Output:
[
{"name": "Big Bob", "score": 134},
{"name": "Habanero Hillary", "score": 98}
]



