
def all_players(names, goals, goals_avoided, assists):
    names = names.split()
    players = zip(names, goals, goals_avoided, assists)
    players_list = []
    for player in players:
     players_list.append({
              "name" : player[0],
              "goals" : player[1], 
             "goals_avoides" : player[2],
                "assists" : player[3]
        })
    return players_list 

    
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
       total = player["goals"] * 1.5 + player["goals_avoides"] * 1.25 + player["assists"]
       if total > max:
          max = total
          max_influential = player["name"]
    return max, max_influential

def prom(players_list):
   return sum([player["goals"]for player in players_list]) / 25

def prom_scorer(goals):
   return goals / 25