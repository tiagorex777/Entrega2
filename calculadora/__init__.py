def max_scorer(players_list):
    max_goals = 0
    for player in players_list:
        if player["goals"] > max_goals:
         max_goals = player["goals"]
         max_name_goals = player["name"]
    return max_goals, max_name_goals


def most_infuential(players_list):
    max = 0
    for player in players_list:
       total = (player["goals"] * 1.5 + player["goals_avoides"] * 1.25 + player["assists"])/ 3 
       if total > max:
          max = total
          max_influential = player["name"]
    return max, max_influential


def prom(players_list):
   return sum([player["goals"]for player in players_list]) / 25


def prom_scorer(goals):
   return goals / 25