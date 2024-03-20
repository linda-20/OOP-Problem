def create_scoreboard(participants):
    def participant_score(participant):
        return participant["chickenwings"] * 5 + participant["hamburgers"] * 3 + participant["hotdogs"] * 2

    scoreboard = [{"name": participant["name"], "score": participant_score(participant)} for participant in participants]
    scoreboard.sort(key=lambda x: (x["score"], x["name"]), reverse=True)

    return scoreboard

    # test cases
participants = [
  {"name": "Habanero Hillary", "chickenwings": 5, "hamburgers": 17, "hotdogs": 11},
  {"name": "Big Bob", "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}
]

scoreboard = create_scoreboard(participants)
print(scoreboard)