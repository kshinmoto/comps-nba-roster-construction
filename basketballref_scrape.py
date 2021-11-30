# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:49:35 2021

@author: kshin
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import re
import numpy as np
import pickle
import re
import numpy as np
import unidecode
import json

headers = {'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9'}

team_names = [
    'ATL',
    'BOS',
    'BRK',
    'CHO',
    'CHI',
    'CLE',
    'DAL',
    'DEN',
    'DET',
    'GSW',
    'HOU',
    'IND',
    'LAC',
    'LAL',
    'MEM',
    'MIA',
    'MIL',
    'MIN',
    'NOP',
    'NYK',
    'OKC',
    'ORL',
    'PHI',
    'PHO',
    'POR',
    'SAC',
    'SAS',
    'TOR',
    'UTA',
    'WAS',
]

team_playoff_names_2021 = [
    'ATL',
    'BOS',
    'BRK',
    'DAL',
    'DEN',
    'LAC',
    'LAL',
    'MEM',
    'MIA',
    'MIL',
    'NYK',
    'PHI',
    'PHO',
    'POR',
    'UTA',
    'WAS',
]

team_playoff_names_2020 = [
    'LAL',
    'POR',
    'HOU',
    'OKC',
    'DEN',
    'UTA',
    'LAC',
    'DAL',
    'MIL',
    'ORL',
    'IND',
    'MIA',
    'BOS',
    'PHI',
    'TOR',
    'BRK',
]

team_playoff_names_2019 = [
    'GSW',
    'LAC',
    'HOU',
    'UTA',
    'POR',
    'OKC',
    'DEN',
    'SAS',
    'MIL',
    'DET',
    'BOS',
    'IND',
    'PHI',
    'BRK',
    'TOR',
    'ORL',
]

team_playoff_names_2018 = [
    'HOU',
    'MIN',
    'OKC',
    'UTA',
    'POR',
    'NOP',
    'GSW',
    'SAS',
    'TOR',
    'WAS',
    'CLE',
    'IND',
    'PHI',
    'MIA',
    'BOS',
    'MIL',
]

# scrape roster stats from basketball-reference (per game stats)
def get_roster(team):
    
    team_url = (f'https://www.basketball-reference.com/teams/{team}/2021.html')

    team_res = requests.get(team_url)

    #BeautifulSoup Library parses the content of an HTML document, in this case clips_res
    team_soup = BeautifulSoup(team_res.content, 'lxml')

    team_per_game = team_soup.find(name = 'table', attrs = {'id' : 'per_game'})

    #create list of dictionaries
    team_stats = []

    print(team + ' per game regular 2021')
    for row in team_per_game('tr')[1:]:
        player = {}
        player['Name'] = row.find('a').text.strip()
        player['Age'] = row.find('td', {'data-stat' : 'age'}).text
        player['Games'] = row.find('td', {'data-stat' : 'g'}).text
        player['GS'] = row.find('td', {'data-stat' : 'gs'}).text
        player['Min PG'] = row.find('td', {'data-stat' : 'mp_per_g'}).text
        player['FGM PG'] = row.find('td', {'data-stat' : 'fg_per_g'}).text
        player['FGA PG'] = row.find('td', {'data-stat' : 'fga_per_g'}).text
        player['Field Goal %'] = row.find('td', {'data-stat' : 'fg_pct'}).text
        player['3pt PG'] = row.find('td', {'data-stat' : 'fg3_per_g'}).text
        player['3ptA PG'] = row.find('td', {'data-stat' : 'fg3a_per_g'}).text
        player['3pt %'] = row.find('td', {'data-stat' : 'fg3_pct'}).text
        player['2pt PG'] = row.find('td', {'data-stat' : 'fg2_per_g'}).text
        player['2ptA PG'] = row.find('td', {'data-stat' : 'fg2a_per_g'}).text
        player['2pt %'] = row.find('td', {'data-stat' : 'fg2_pct'}).text
        player['EFG %'] = row.find('td', {'data-stat' : 'efg_pct'}).text
        player['FTM PG'] = row.find('td', {'data-stat' : 'ft_per_g'}).text
        player['FTA PG'] = row.find('td', {'data-stat' : 'fta_per_g'}).text
        player['FT %'] = row.find('td', {'data-stat' : 'ft_pct'}).text
        player['ORbPG'] = row.find('td', {'data-stat' : 'orb_per_g'}).text
        player['DRbPG'] = row.find('td', {'data-stat' : 'drb_per_g'}).text
        player['Rebounds PG'] = row.find('td', {'data-stat' : 'trb_per_g'}).text
        player['Assists PG'] = row.find('td', {'data-stat' : 'ast_per_g'}).text
        player['Steals PG'] = row.find('td', {'data-stat' : 'stl_per_g'}).text
        player['Blocks PG'] = row.find('td', {'data-stat' : 'blk_per_g'}).text
        player['Turnovers PG'] = row.find('td', {'data-stat' : 'tov_per_g'}).text
        player['PF PG'] = row.find('td', {'data-stat' : 'pf_per_g'}).text
        player['Points PG'] = row.find('td', {'data-stat' : 'pts_per_g'}).text
        team_stats.append(player)
    
    team_roster_df = pd.DataFrame(team_stats)
    return team_roster_df

# scrape player totals from basketball-reference
def get_totals(team, year):
    
    team_url = (f'https://www.basketball-reference.com/teams/{team}/{year}.html')

    team_res = requests.get(team_url)

    #BeautifulSoup Library parses the content of an HTML document, in this case clips_res
    team_soup = BeautifulSoup(team_res.content, 'lxml')

    team_per_game = team_soup.find(name = 'table', attrs = {'id' : 'totals'})

    #create list of dictionaries
    team_stats = []

    print(team + f' totals {year}')
    for row in team_per_game('tr')[1:]:
        player = {}
        player['Name'] = row.find('td', {'data-stat' : 'player'}).text
        print(row.find('td', {'data-stat' : 'player'}).text)
        player['Age'] = row.find('td', {'data-stat' : 'age'}).text
        player['Games'] = int(row.find('td', {'data-stat' : 'g'}).text)
        try:
            player['GS'] = int(row.find('td', {'data-stat' : 'gs'}).text)
        except:
            player['GS'] = 0
        player['Min'] = int(row.find('td', {'data-stat' : 'mp'}).text)
        player['FGM'] = int(row.find('td', {'data-stat' : 'fg'}).text)
        player['FGA'] = int(row.find('td', {'data-stat' : 'fga'}).text)
        try:
            player['Field Goal %'] = float(row.find('td', {'data-stat' : 'fg_pct'}).text)
        except:
            player['Field Goal %'] = 0
        player['3pt'] = int(row.find('td', {'data-stat' : 'fg3'}).text)
        player['3ptA'] = int(row.find('td', {'data-stat' : 'fg3a'}).text)
        try:
            player['3pt %'] = float(row.find('td', {'data-stat' : 'fg3_pct'}).text)
        except:
            player['3pt %'] = 0
        player['2pt'] = int(row.find('td', {'data-stat' : 'fg2'}).text)
        player['2ptA'] = int(row.find('td', {'data-stat' : 'fg2a'}).text)
        try:
            player['2pt %'] = float(row.find('td', {'data-stat' : 'fg2_pct'}).text)
        except:
            player['2pt %'] = 0
        try:
            player['EFG %'] = float(row.find('td', {'data-stat' : 'efg_pct'}).text)
        except:
            player['EFG %'] = 0
        player['FTM'] = int(row.find('td', {'data-stat' : 'ft'}).text)
        player['FTA'] = int(row.find('td', {'data-stat' : 'fta'}).text)
        try:
            player['FT %'] = float(row.find('td', {'data-stat' : 'ft_pct'}).text)
        except:
            player['FT %'] = 0
        player['ORb'] = int(row.find('td', {'data-stat' : 'orb'}).text)
        player['DRb'] = int(row.find('td', {'data-stat' : 'drb'}).text)
        player['Rebounds'] = int(row.find('td', {'data-stat' : 'trb'}).text)
        player['Assists'] = int(row.find('td', {'data-stat' : 'ast'}).text)
        player['Steals'] = int(row.find('td', {'data-stat' : 'stl'}).text)
        player['Blocks'] = int(row.find('td', {'data-stat' : 'blk'}).text)
        player['Turnovers'] = int(row.find('td', {'data-stat' : 'tov'}).text)
        player['PF'] = int(row.find('td', {'data-stat' : 'pf'}).text)
        player['Points'] = int(row.find('td', {'data-stat' : 'pts'}).text)
        if player['Min'] < 10000:
            team_stats.append(player)
    
    team_roster_df = pd.DataFrame(team_stats)
    return team_roster_df

def get_playoff_totals(team, year):
    
    team_url = (f'https://www.basketball-reference.com/teams/{team}/{year}.html')

    team_res = requests.get(team_url)

    #BeautifulSoup Library parses the content of an HTML document, in this case clips_res
    team_soup = BeautifulSoup(team_res.content, 'lxml')

    team_per_game = team_soup.find(name = 'table', attrs = {'id' : 'playoffs_totals'})

    #create list of dictionaries
    team_stats = []

    print(team + f' playoff totals {year}')
    for row in team_per_game('tr')[1:]:
        player = {}
        player['Name'] = row.find('td', {'data-stat' : 'player'}).text
        print(row.find('td', {'data-stat' : 'player'}).text)
        player['Age'] = row.find('td', {'data-stat' : 'age'}).text
        player['Games'] = int(row.find('td', {'data-stat' : 'g'}).text)
        try:
            player['GS'] = int(row.find('td', {'data-stat' : 'gs'}).text)
        except:
            player['GS'] = 0
        player['Min'] = int(row.find('td', {'data-stat' : 'mp'}).text)
        player['FGM'] = int(row.find('td', {'data-stat' : 'fg'}).text)
        player['FGA'] = int(row.find('td', {'data-stat' : 'fga'}).text)
        try:
            player['Field Goal %'] = float(row.find('td', {'data-stat' : 'fg_pct'}).text)
        except:
            player['Field Goal %'] = 0
        player['3pt'] = int(row.find('td', {'data-stat' : 'fg3'}).text)
        player['3ptA'] = int(row.find('td', {'data-stat' : 'fg3a'}).text)
        try:
            player['3pt %'] = float(row.find('td', {'data-stat' : 'fg3_pct'}).text)
        except:
            player['3pt %'] = 0
        player['2pt'] = int(row.find('td', {'data-stat' : 'fg2'}).text)
        player['2ptA'] = int(row.find('td', {'data-stat' : 'fg2a'}).text)
        try:
            player['2pt %'] = float(row.find('td', {'data-stat' : 'fg2_pct'}).text)
        except:
            player['2pt %'] = 0
        try:
            player['EFG %'] = float(row.find('td', {'data-stat' : 'efg_pct'}).text)
        except:
            player['EFG %'] = 0
        player['FTM'] = int(row.find('td', {'data-stat' : 'ft'}).text)
        player['FTA'] = int(row.find('td', {'data-stat' : 'fta'}).text)
        try:
            player['FT %'] = float(row.find('td', {'data-stat' : 'ft_pct'}).text)
        except:
            player['FT %'] = 0
        player['ORb'] = int(row.find('td', {'data-stat' : 'orb'}).text)
        player['DRb'] = int(row.find('td', {'data-stat' : 'drb'}).text)
        player['Rebounds'] = int(row.find('td', {'data-stat' : 'trb'}).text)
        player['Assists'] = int(row.find('td', {'data-stat' : 'ast'}).text)
        player['Steals'] = int(row.find('td', {'data-stat' : 'stl'}).text)
        player['Blocks'] = int(row.find('td', {'data-stat' : 'blk'}).text)
        player['Turnovers'] = int(row.find('td', {'data-stat' : 'tov'}).text)
        player['PF'] = int(row.find('td', {'data-stat' : 'pf'}).text)
        player['Points'] = int(row.find('td', {'data-stat' : 'pts'}).text)
        if player['Min'] < 10000:
            team_stats.append(player)
    
    team_roster_df = pd.DataFrame(team_stats)
    return team_roster_df

# empty list for player stats
list_stats = []

# loop through list of teams to get teams 2020-21 player stats
for team in team_names:
    list_stats.append(get_roster(team))

list_totals_2021 = []

for team in team_names:
    list_totals_2021.append(get_totals(team, 2021))
    
list_playoff_totals_2021 = []

for team in team_playoff_names_2021:
    list_playoff_totals_2021.append(get_playoff_totals(team, 2021))
    
list_playoff_totals_2020 = []

for team in team_playoff_names_2020:
    list_playoff_totals_2020.append(get_playoff_totals(team, 2020))
    
list_playoff_totals_2019 = []

for team in team_playoff_names_2019:
    list_playoff_totals_2019.append(get_playoff_totals(team, 2019))
    
list_playoff_totals_2018 = []

for team in team_playoff_names_2018:
    list_playoff_totals_2018.append(get_playoff_totals(team, 2018))
    
list_totals_2020 = []

for team in team_names:
    list_totals_2020.append(get_totals(team, 2020))
    
list_totals_2019 = []

for team in team_names:
    list_totals_2019.append(get_totals(team, 2019))
    
list_totals_2018 = []

for team in team_names:
    list_totals_2018.append(get_totals(team, 2018))
    
list_totals_2022 = []

for team in team_names:
    list_totals_2022.append(get_totals(team, 2022))

# panda concat of all player stats
all_player_stats = pd.concat(list_stats, ignore_index=True)

all_player_totals_2022 = pd.concat(list_totals_2022, ignore_index=True)

all_player_totals_2021 = pd.concat(list_totals_2021, ignore_index=True)

all_playoff_totals_2021 = pd.concat(list_playoff_totals_2021, ignore_index=True)

all_player_totals_2020 = pd.concat(list_totals_2020, ignore_index=True)

all_playoff_totals_2020 = pd.concat(list_playoff_totals_2020, ignore_index=True)

all_player_totals_2019 = pd.concat(list_totals_2019, ignore_index=True)

all_playoff_totals_2019 = pd.concat(list_playoff_totals_2019, ignore_index=True)

all_player_totals_2018 = pd.concat(list_totals_2018, ignore_index=True)

all_playoff_totals_2018 = pd.concat(list_playoff_totals_2018, ignore_index=True)

new_player_totals = all_player_totals_2021

new_player_totals = new_player_totals.sort_values(by='Name')

# we can get specific team from list using index (ex. ATL)
roster_ATL = list_stats[0]

# function to retrieve current roster
def get_current_roster(team):
    
    team_url = (f'https://www.basketball-reference.com/teams/{team}/2022.html')
    
    team_res = requests.get(team_url)

    #BeautifulSoup Library parses the content of an HTML document, in this case clips_res
    team_soup = BeautifulSoup(team_res.content, 'lxml')

    team_roster = team_soup.find(name = 'table', attrs = {'id' : 'roster'})

    #create list of dictionaries
    team_players = []
    
    print(team)
    
    for row in team_roster('tr')[1:]:
        player = {}
        player['Name'] = row.find('a').text.strip()
        player['Position'] = row.find('td', {'data-stat' : 'pos'}).text
        player['Number'] = row.find('th', {'data-stat' : 'number'}).text
        team_players.append(player)
        
    current_roster_df = pd.DataFrame(team_players)
    return(current_roster_df)

# loop through teams again to make list of current rosters
list_current_rosters = []
for team in team_names:
    list_current_rosters.append(get_current_roster(team))

    
# for loop in for loop (in for loop lol) of players for each team, match them with players in concat list

current_roster_list = []

for i in range(len(team_names)):
    print(team_names[i])
    loop_roster = list_current_rosters[i]
    
    loop_cur_roster = []

    for index, row in loop_roster.iterrows():
        for index2, row2 in all_player_stats.iterrows():
            if row2['Name'] == row['Name']:
                loop_cur_roster.append(all_player_stats.loc[index2,:])
    
    current_roster_list.append(loop_cur_roster)
    

# create a function to add stats of each year together for each player
def get_player_stats(player, seasons):
    player_stats = []
    age = 0
    
    #loop through totals of past nba seasons and add to list
    if seasons == 4:
        for index, row in all_player_totals_2022.iterrows():
            if player == row['Name']:
                player_stats.append(all_player_totals_2022.loc[index,:])
                age = row['Age']
        for index, row in all_player_totals_2021.iterrows():
            if player == row['Name']:
                player_stats.append(all_player_totals_2021.loc[index,:])
                if age == 0:
                    age = row['Age']
        for index, row in all_playoff_totals_2021.iterrows():
            if player == row['Name']:
                player_stats.append(all_playoff_totals_2021.loc[index,:])
        for index2, row2 in all_player_totals_2020.iterrows():
            if player == row2['Name']:
                player_stats.append(all_player_totals_2020.loc[index2,:])
        for index, row in all_playoff_totals_2020.iterrows():
            if player == row['Name']:
                player_stats.append(all_playoff_totals_2020.loc[index,:])
        for index3, row3 in all_player_totals_2019.iterrows():
            if player == row3['Name']:
                player_stats.append(all_player_totals_2019.loc[index3,:])
        for index, row in all_playoff_totals_2019.iterrows():
            if player == row['Name']:
                player_stats.append(all_playoff_totals_2019.loc[index,:])
        for index4, row4 in all_player_totals_2018.iterrows():
            if player == row4['Name']:
                player_stats.append(all_player_totals_2018.loc[index4,:])
        for index, row in all_playoff_totals_2018.iterrows():
            if player == row['Name']:
                player_stats.append(all_playoff_totals_2018.loc[index,:])
    
    elif seasons == 3:
        for index, row in all_player_totals_2022.iterrows():
            if player == row['Name']:
                player_stats.append(all_player_totals_2022.loc[index,:])
                age = row['Age']
        for index, row in all_player_totals_2021.iterrows():
            if player == row['Name']:
                player_stats.append(all_player_totals_2021.loc[index,:])
                if age == 0:
                    age = row['Age']
        for index, row in all_playoff_totals_2021.iterrows():
            if player == row['Name']:
                player_stats.append(all_playoff_totals_2021.loc[index,:])
        for index2, row2 in all_player_totals_2020.iterrows():
            if player == row2['Name']:
                player_stats.append(all_player_totals_2020.loc[index2,:])
        for index, row in all_playoff_totals_2020.iterrows():
            if player == row['Name']:
                player_stats.append(all_playoff_totals_2020.loc[index,:])
        for index3, row3 in all_player_totals_2019.iterrows():
            if player == row3['Name']:
                player_stats.append(all_player_totals_2019.loc[index3,:])
        for index, row in all_playoff_totals_2019.iterrows():
            if player == row['Name']:
                player_stats.append(all_playoff_totals_2019.loc[index,:])
                
    elif seasons == 2:
        for index, row in all_player_totals_2022.iterrows():
            if player == row['Name']:
                player_stats.append(all_player_totals_2022.loc[index,:])
                age = row['Age']
        for index, row in all_player_totals_2021.iterrows():
            if player == row['Name']:
                player_stats.append(all_player_totals_2021.loc[index,:])
                if age == 0:
                    age = row['Age']
        for index, row in all_playoff_totals_2021.iterrows():
            if player == row['Name']:
                player_stats.append(all_playoff_totals_2021.loc[index,:])
        for index2, row2 in all_player_totals_2020.iterrows():
            if player == row2['Name']:
                player_stats.append(all_player_totals_2020.loc[index2,:])
        for index, row in all_playoff_totals_2020.iterrows():
            if player == row['Name']:
                player_stats.append(all_playoff_totals_2020.loc[index,:])
                
    else:
        for index, row in all_player_totals_2022.iterrows():
            if player == row['Name']:
                player_stats.append(all_player_totals_2022.loc[index,:])
                age = row['Age']
        for index, row in all_player_totals_2021.iterrows():
            if player == row['Name']:
                player_stats.append(all_player_totals_2021.loc[index,:])
                if age == 0:
                    age = row['Age']
        for index, row in all_playoff_totals_2021.iterrows():
            if player == row['Name']:
                player_stats.append(all_playoff_totals_2021.loc[index,:])
                
    #turn list into df
    player_totals_df = pd.DataFrame(player_stats)
    
    if len(player_totals_df) >= 1:
    
        player_totals_df = player_totals_df.append(player_totals_df.sum(axis = 0, skipna = True), ignore_index= True)
        
        final_stats = {}
        
        final_stats['Name'] = player
        final_stats['Age'] = age
        final_stats['Games'] = player_totals_df.loc[len(player_totals_df)-1, 'Games']
        gp = player_totals_df.loc[len(player_totals_df)-1, 'Games']
        final_stats['GS'] = player_totals_df.loc[len(player_totals_df)-1, 'GS']
        final_stats['Min'] = round(float(player_totals_df.loc[len(player_totals_df)-1, 'Min'] / gp),2)
        final_stats['FGM'] = round(float(player_totals_df.loc[len(player_totals_df)-1, 'FGM'] / gp),2)
        final_stats['FGA'] = round(float(player_totals_df.loc[len(player_totals_df)-1, 'FGA'] / gp),2)
        fga = (player_totals_df.loc[len(player_totals_df)-1, 'FGA'])
        final_stats['FG %'] = round(float(player_totals_df.loc[len(player_totals_df)-1, 'FGM'] / fga),2)
        final_stats['3pt'] = round(float(player_totals_df.loc[len(player_totals_df)-1, '3pt'] / gp),2)
        final_stats['3ptA'] = round(float(player_totals_df.loc[len(player_totals_df)-1, '3ptA'] / gp),2)
        threeptA = (player_totals_df.loc[len(player_totals_df)-1, '3ptA'])
        final_stats['3pt %'] = round(float(player_totals_df.loc[len(player_totals_df)-1, '3pt'] / threeptA),2)
        final_stats['2pt'] = round(float(player_totals_df.loc[len(player_totals_df)-1, '2pt'] / gp),2)
        final_stats['2ptA'] = round(float(player_totals_df.loc[len(player_totals_df)-1, '2ptA'] / gp),2)
        twoptA = (player_totals_df.loc[len(player_totals_df)-1, '2ptA'])
        final_stats['2pt %'] = round(float(player_totals_df.loc[len(player_totals_df)-1, '2pt'] / twoptA),2)
        fgm = (player_totals_df.loc[len(player_totals_df)-1, 'FGM'])
        efg_threes = 1.5 * (player_totals_df.loc[len(player_totals_df)-1, '3pt'])
        final_stats['EFG %'] = round(float((fgm + efg_threes) / fga),2)
        final_stats['FTM'] = round(float(player_totals_df.loc[len(player_totals_df)-1, 'FTM'] / gp),2)
        final_stats['FTA'] = round(float(player_totals_df.loc[len(player_totals_df)-1, 'FTA'] / gp),2)
        fta = (player_totals_df.loc[len(player_totals_df)-1, 'FTA'])
        final_stats['FT %'] = round(float(player_totals_df.loc[len(player_totals_df)-1, 'FTM'] / fta),2)
        final_stats['ORb'] = round(float(player_totals_df.loc[len(player_totals_df)-1, 'ORb'] / gp),2)
        final_stats['DRb'] = round(float(player_totals_df.loc[len(player_totals_df)-1, 'DRb'] / gp),2)
        final_stats['Rebounds'] = round(float(player_totals_df.loc[len(player_totals_df)-1, 'Rebounds'] / gp),2)
        final_stats['Assists'] = round(float(player_totals_df.loc[len(player_totals_df)-1, 'Assists'] / gp),2)
        final_stats['Steals'] = round(float(player_totals_df.loc[len(player_totals_df)-1, 'Steals'] / gp),2)
        final_stats['Blocks'] = round(float(player_totals_df.loc[len(player_totals_df)-1, 'Blocks'] / gp),2)
        final_stats['Turnovers'] = round(float(player_totals_df.loc[len(player_totals_df)-1, 'Turnovers'] / gp),2)
        final_stats['PF'] = round(float(player_totals_df.loc[len(player_totals_df)-1, 'PF'] / gp),2)
        final_stats['PPG'] = round(float(player_totals_df.loc[len(player_totals_df)-1, 'Points'] / gp),2)
   
    else:
        final_stats = {}
        
        final_stats['Name'] = player
        
        return(final_stats)
    
    return(final_stats)


all_player_final_stats_4 = []

for i in range(len(team_names)):
    print(team_names[i])
    loop_roster = list_current_rosters[i]
    
    list_all_current_stats = []

    for index, row in loop_roster.iterrows():
        list_all_current_stats.append(get_player_stats(row['Name'], 4))
        print(row['Name'])
        
    df_list = pd.DataFrame(list_all_current_stats)
        
    all_player_final_stats_4.append(df_list)
    
# make dataframes for past 3 seasons    
all_player_final_stats_3 = []

for i in range(len(team_names)):
    print(team_names[i])
    loop_roster = list_current_rosters[i]
    
    list_all_current_stats = []

    for index, row in loop_roster.iterrows():
        list_all_current_stats.append(get_player_stats(row['Name'], 3))
        print(row['Name'])
        
    df_list = pd.DataFrame(list_all_current_stats)
        
    all_player_final_stats_3.append(df_list)

# make dataframes for past 2 seasons    
all_player_final_stats_2 = []

for i in range(len(team_names)):
    print(team_names[i])
    loop_roster = list_current_rosters[i]
    
    list_all_current_stats = []

    for index, row in loop_roster.iterrows():
        list_all_current_stats.append(get_player_stats(row['Name'], 2))
        print(row['Name'])
        
    df_list = pd.DataFrame(list_all_current_stats)
        
    all_player_final_stats_2.append(df_list)
    
# make dataframes for past season    
all_player_final_stats_1 = []

for i in range(len(team_names)):
    print(team_names[i])
    loop_roster = list_current_rosters[i]
    
    list_all_current_stats = []

    for index, row in loop_roster.iterrows():
        list_all_current_stats.append(get_player_stats(row['Name'], 1))
        print(row['Name'])
        
    df_list = pd.DataFrame(list_all_current_stats)
        
    all_player_final_stats_1.append(df_list)
    

# add year span column to dataframes
'''
for roster in all_player_final_stats_4:
    roster['Seasons'] = '17-18:20-21'
    
for roster in all_player_final_stats_3:
    roster['Seasons'] = '18-19:20-21'
    
for roster in all_player_final_stats_2:
    roster['Seasons'] = '19-20:20-21'
    
for roster in all_player_final_stats_1:
    roster['Seasons'] = '20-21'
    '''
    

# add team name to dataframes
team_index = 0
for roster in all_player_final_stats_4:
    loop_team = team_names[team_index]
    roster['Team'] = loop_team
    team_index = team_index + 1
    
team_index = 0
for roster in all_player_final_stats_3:
    loop_team = team_names[team_index]
    roster['Team'] = loop_team
    team_index = team_index + 1
    
team_index = 0
for roster in all_player_final_stats_2:
    loop_team = team_names[team_index]
    roster['Team'] = loop_team
    team_index = team_index + 1
    
team_index = 0
for roster in all_player_final_stats_1:
    loop_team = team_names[team_index]
    roster['Team'] = loop_team
    team_index = team_index + 1
    
# next steps:
# combine all final stats into one dataframe?
# combine all stats of each year spans into their own separate dataframe

concat_final_4 = pd.concat(all_player_final_stats_4, ignore_index=True)

concat_final_3 = pd.concat(all_player_final_stats_3, ignore_index=True)

concat_final_2 = pd.concat(all_player_final_stats_2, ignore_index=True)

concat_final_1 = pd.concat(all_player_final_stats_1, ignore_index=True)


#######################################################################

# get defensive stats from nba website

ssn = '2020-21'

def get_nba_stats(url):
    json_file = requests.get(url, headers=headers).json()

    data = json_file['resultSets'][0]['rowSet']
    columns = json_file['resultSets'][0]['headers']
    
    nba_stats = pd.DataFrame.from_records(data, columns=columns) 
    
    return(nba_stats)

defense_stats = get_nba_stats('https://stats.nba.com/stats/leaguedashptdefend?College=&Conference=&Country=&DateFrom=&DateTo=&DefenseCategory=Overall&Division=&DraftPick=&DraftYear=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&Season=2020-21&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=')

defense_stats = defense_stats.drop(columns=['CLOSE_DEF_PERSON_ID', 'PLAYER_LAST_TEAM_ID', 'PLAYER_LAST_TEAM_ABBREVIATION', 'PLAYER_POSITION', 'AGE', 'GP', 'G', 'FREQ'])

defense_stats['PLAYER_NAME'].replace({'Robert Williams':'Robert Williams III','Marcus Morris':'Marcus Morris Sr.','Derrick Walton':'Derrick Walton Jr.','Juan Hernangomez':'Juancho Hernangomez','Sviatoslav Mykhailiuk':'Svi Mykhailiuk','Zach Norvell':'Zach Norvell Jr.','Lonnie Walker':'Lonnie Walker IV','Charlie Brown':'Charles Brown Jr.','C.J. Miles':'CJ Miles','Wesley Iwundu':'Wes Iwundu','J.J. Redick':'JJ Redick','B.J. Johnson':'BJ Johnson','Melvin Frazier':'Melvin Frazier Jr.','Otto Porter':'Otto Porter Jr.','James Ennis':'James Ennis III','Danuel House':'Danuel House Jr.','Brian Bowen':'Brian Bowen II','Kevin Knox':'Kevin Knox II','Frank Mason III':'Frank Mason','Harry Giles':'Harry Giles III','T.J. Leaf':'TJ Leaf','J.R. Smith':'JR Smith','Vince Edwards':'Vincent Edwards','D.J. Stephens':'DJ Stephens','Mitch Creek':'Mitchell Creek','R.J. Hunter':'RJ Hunter','Wade Baldwin':'Wade Baldwin IV'},inplace=True)

result_names = [
    'Bogdan Bogdanovic',
    'Timothe Luwawu-Cabarrot',
    'Dennis Schroder',
    'Robert Williams III',
    'Juancho Hernangomez',
    'Nic Claxton',
    'Nikola Vucevic',
    'Luka Doncic',
    'Kristaps Porzingis',
    'Boban Marjanovic',
    'Nikola Jokic',
    'P.J. Dozier',
    'Vlatko Cancar',
    'Otto Porter Jr.',
    'Danuel House Jr.',
    'Marcus Morris Sr.',
    'Jonas Valanciunas',
    'Tomas Satoransky',
    'Willy Hernangomez',
    'Kevin Knox II',
    'Luka Samanic',
    'Theo Maledon',
    'Dario Saric',
    'Jusuf Nurkic',
    'Lonnie Walker IV',
    'Goran Dragic',
    'Bojan Bogdanovic',
    'Davis Bertans',
    ]

replacement_names = [
    'Bogdan Bogdanović',
    'Timothé Luwawu-Cabarrot',
    'Dennis Schröder',
    'Robert Williams',
    'Juan Hernangómez',
    'Nicolas Claxton',
    'Nikola Vučević',
    'Luka Dončić',
    'Kristaps Porziņģis',
    'Boban Marjanović',
    'Nikola Jokić',
    'PJ Dozier',
    'Vlatko Čančar',
    'Otto Porter',
    'Danuel House',
    'Marcus Morris',
    'Jonas Valančiūnas',
    'Tomáš Satoranský',
    'Willy Hernangómez',
    'Kevin Knox',
    'Luka Šamanić',
    'Théo Maledon',
    'Dario Šarić',
    'Jusuf Nurkić',
    'Lonnie Walker',
    'Goran Dragić',
    'Bojan Bogdanović',
    'Dāvis Bertāns'
]

i = 0
for name in result_names:
    for index, row in defense_stats.iterrows():
        if name == row['PLAYER_NAME']:
            defense_stats = defense_stats.replace(row['PLAYER_NAME'], replacement_names[i])
            print(replacement_names[i] + ' ' + row['PLAYER_NAME'])
    i+=1
    
for index, row in defense_stats.iterrows():
    is_in_result = False
    
    for index2, row2 in concat_final_4.iterrows():
        if row2['Name'] == row['PLAYER_NAME']:
            
            is_in_result = True
            
    if is_in_result != True:
        print(row['PLAYER_NAME'])
        defense_stats = defense_stats.drop(labels=index, axis=0)
        
#########################################################################
# attach player roles to stats dataframes

trad_big = pd.read_csv (r'C:\Users\kshin\trad_big.csv')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
ball_dom = pd.read_csv (r'C:\Users\kshin\ball_dom.csv')
high_usg_big = pd.read_csv (r'C:\Users\kshin\high_usg_big.csv')
off_bench = pd.read_csv (r'C:\Users\kshin\off_bench.csv')
role_big = pd.read_csv (r'C:\Users\kshin\role_big.csv')
role_guard = pd.read_csv (r'C:\Users\kshin\role_guard.csv')
secondary = pd.read_csv (r'C:\Users\kshin\secondary.csv')
vers_forwards = pd.read_csv (r'C:\Users\kshin\vers_forwards.csv')

trad_big['Role'] = 'Traditional Big'
ball_dom['Role'] = 'Ball Dominant'
high_usg_big['Role'] = 'High Usage Big'
off_bench['Role'] = 'Off Bench'
role_big['Role'] = 'Roleplayer Big'
role_guard['Role'] = 'Roleplayer Guard'
secondary['Role'] = 'Secondary Playmaker'
vers_forwards['Role'] = 'Versatile Forwards'


### replace names with correct versions

i = 0
for name in result_names:
    for index, row in trad_big.iterrows():
        if name == row['player']:
            trad_big = trad_big.replace(row['player'], replacement_names[i])
            print(replacement_names[i] + ' ' + row['player'])
    i+=1
    
i = 0
for name in result_names:
    for index, row in ball_dom.iterrows():
        if name == row['player']:
            ball_dom = ball_dom.replace(row['player'], replacement_names[i])
            print(replacement_names[i] + ' ' + row['player'])
    i+=1
    
i = 0
for name in result_names:
    for index, row in high_usg_big.iterrows():
        if name == row['player']:
            high_usg_big = high_usg_big.replace(row['player'], replacement_names[i])
            print(replacement_names[i] + ' ' + row['player'])
    i+=1

i = 0
for name in result_names:
    for index, row in off_bench.iterrows():
        if name == row['player']:
            off_bench = off_bench.replace(row['player'], replacement_names[i])
            print(replacement_names[i] + ' ' + row['player'])
    i+=1
    
i = 0
for name in result_names:
    for index, row in role_big.iterrows():
        if name == row['player']:
            role_big = role_big.replace(row['player'], replacement_names[i])
            print(replacement_names[i] + ' ' + row['player'])
    i+=1

i = 0
for name in result_names:
    for index, row in role_guard.iterrows():
        if name == row['player']:
            role_guard = role_guard.replace(row['player'], replacement_names[i])
            print(replacement_names[i] + ' ' + row['player'])
    i+=1

i = 0
for name in result_names:
    for index, row in secondary.iterrows():
        if name == row['player']:
            secondary = secondary.replace(row['player'], replacement_names[i])
            print(replacement_names[i] + ' ' + row['player'])
    i+=1

i = 0
for name in result_names:
    for index, row in vers_forwards.iterrows():
        if name == row['player']:
            vers_forwards = vers_forwards.replace(row['player'], replacement_names[i])
            print(replacement_names[i] + ' ' + row['player'])
    i+=1
    
    
### combine roles to stats datatframes
concat_final_4['Role'] = 'temp'

for index, row in trad_big.iterrows():
    i = 0
    for index2, row2 in concat_final_4.iterrows():
        if row['player'] == row2['Name']:
            concat_final_4.at[i, 'Role'] = 'Traditional Big'
        i+=1
        
for index, row in ball_dom.iterrows():
    i = 0
    for index2, row2 in concat_final_4.iterrows():
        if row['player'] == row2['Name']:
            concat_final_4.at[i, 'Role'] = 'Ball Dominant'
        i+=1
    
for index, row in high_usg_big.iterrows():
    i = 0
    for index2, row2 in concat_final_4.iterrows():
        if row['player'] == row2['Name']:
            concat_final_4.at[i, 'Role'] = 'High Usage Big'
        i+=1
        
for index, row in off_bench.iterrows():
    i = 0
    for index2, row2 in concat_final_4.iterrows():
        if row['player'] == row2['Name']:
            concat_final_4.at[i, 'Role'] = 'Off Bench'
        i+=1
    
for index, row in role_big.iterrows():
    i = 0
    for index2, row2 in concat_final_4.iterrows():
        if row['player'] == row2['Name']:
            concat_final_4.at[i, 'Role'] = 'Roleplaying Big'
        i+=1

for index, row in role_guard.iterrows():
    i = 0
    for index2, row2 in concat_final_4.iterrows():
        if row['player'] == row2['Name']:
            concat_final_4.at[i, 'Role'] = 'Roleplaying Guard'
        i+=1

for index, row in secondary.iterrows():
    i = 0
    for index2, row2 in concat_final_4.iterrows():
        if row['player'] == row2['Name']:
            concat_final_4.at[i, 'Role'] = 'Secondary Playmaker'
        i+=1

for index, row in vers_forwards.iterrows():
    i = 0
    for index2, row2 in concat_final_4.iterrows():
        if row['player'] == row2['Name']:
            concat_final_4.at[i, 'Role'] = 'Versatile Forward'
        i+=1
        


#######################################################################
### create defense tables/attach defense stats

concat_final_4_defense = pd.merge(concat_final_4, defense_stats, left_on='Name', right_on='PLAYER_NAME')

#######################################################################

# turn dataframes into sql databases
'''
import sqlite3

conn = sqlite3.connect('test_database')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS products (product_name text, price number)')
conn.commit()


concat_final_4.to_sql('players', conn, if_exists='replace', index = False)
 
c.execute('''''''  
SELECT * FROM players
          '''#


# scrape slary information using similar functions
def get_salary(team):
    
    team_url = (f'https://www.basketball-reference.com/contracts/{team}.html')

    team_res = requests.get(team_url)

    #BeautifulSoup Library parses the content of an HTML document, in this case clips_res
    team_soup = BeautifulSoup(team_res.content, 'lxml')

    team_salaries = team_soup.find(name = 'table', attrs = {'id' : 'contracts'})

    #create list of dictionaries
    salary_info = []

    print(team)
    for row in team_salaries('tr')[2:]:
        print(row)
        player = {}
        try:
            player['Name'] = row.find('th', {'data-stat' : 'player'}).text
            print(player['Name'])
            player['Age'] = row.find('td', {'data-stat' : 'age_today'}).text
            try:
                player['y1'] = row.find('td', {'data-stat' : 'y1'}).text
                remove_characters = '$,'
                salary_num = row.find('td', {'data-stat' : 'y1'}).text
                for character in remove_characters:
                    salary_num = salary_num.replace(character,"")
                player['Int'] = int(salary_num)
                    
                try:    
                    player['y2'] = row.find('td', {'data-stat' : 'y2'}).text
                    remove_characters = '$,'
                    salary_num = row.find('td', {'data-stat' : 'y2'}).text
                    for character in remove_characters:
                        salary_num = salary_num.replace(character,"")
                    player['Int2'] = int(salary_num)
                    if salary_num == 0:
                        player['Int2'] = 0
                except:
                    player['Int2'] = 0
                
                try:
                    player['y3'] = row.find('td', {'data-stat' : 'y3'}).text
                    remove_characters = '$,'
                    salary_num = row.find('td', {'data-stat' : 'y3'}).text
                    for character in remove_characters:
                        salary_num = salary_num.replace(character,"")
                    player['Int3'] = int(salary_num)
                    if salary_num == 0:
                            player['Int3'] = 0
                except:
                    player['Int3'] = 0
                
            except:
                player['Int'] = 0
                player['Int2'] = 0
                player['Int3'] = 0
            if player['Int'] == 0:
                player['Status'] = 'Two-Way'
            elif player['Int2'] == 0:
                player['Status'] = 'Upcoming FA'
            elif player['Int3'] == 0:
                player['Status'] = 'Future FA'
            elif player['Int'] > 78000000:
                player['Status'] = 'Team Totals'
            else:
                player['Status'] = 'Multiyear Player'
            player['Team'] = team
            salary_info.append(player)
        except:
            salary_info.append(player)
            
    team_salary_df = pd.DataFrame(salary_info)
    return team_salary_df

# loop through teams and get all player salaries
team_salaries = []

for team in team_names:
    salaries = get_salary(team)
    team_salaries.append(salaries)
    
concat_salary = pd.concat(team_salaries, ignore_index=True)


concat_final_4_defense = pd.merge(concat_final_4_defense, concat_salary, left_on='Name', right_on='Name')

concat_final_4 = pd.merge(concat_final_4, concat_salary, left_on='Name', right_on='Name')

concat_final_4_defense = concat_final_4_defense.drop(columns = 'Age_y')
concat_final_4_defense = concat_final_4_defense.drop(columns = 'Team_y')
concat_final_4_defense = concat_final_4_defense.drop(columns = 'PLAYER_NAME')

concat_final_4 = concat_final_4.drop(columns = 'Age_y')
concat_final_4 = concat_final_4.drop(columns = 'Team_y')




####################################################################
#turn dataframes into csv files to use DBbrowser and make database
concat_final_4.to_csv('new_concat_4.csv', index=False, encoding='utf-8')

concat_final_3.to_csv('new_concat_3.csv', index=False, encoding='utf-8')

concat_final_2.to_csv('new_concat_2.csv', index=False, encoding='utf-8')

concat_final_1.to_csv('new_concat_1.csv', index=False, encoding='utf-8')

concat_final_4_defense.to_csv('new_concat_4_defense.csv', index=False, encoding='utf-8')







    
#get rid of players who haven't played enough
fa_stats_4 = concat_final_4
loop_index = 0
for index, row in fa_stats_4.iterrows():
    if row['Min'] < 6 or row['Games'] < 40:
        print(row['Name'])
        print(loop_index)
        fa_stats_4 = fa_stats_4.drop(loop_index)
    loop_index = loop_index+1

# create list for player roles    
role_list = []

# assign each player temporary role
for index, row in fa_stats_4.iterrows():
    if row['PPG'] > 15:
        role = 'Star Player'
    elif row['Rebounds'] > row['Assists']:
        role = 'Big Man'
    else:
        role = 'Facilitator'
    role_list.append(role)

# create role column in df
fa_stats_4['Role'] = role_list

list_star_player = []
list_big_man = []
list_facilitator =[]

for index, row in fa_stats_4.iterrows():
    if row['Role'] == 'Star Player':
        list_star_player.append(row['Name'])
    elif row['Role'] == 'Big Man':
        list_big_man.append(row['Name'])
    else:
        list_facilitator.append(row['Name'])
        
input_team = input("Which team would you like to analyze: ")

input_roster = []

for index, row in concat_final_4.iterrows():
    if row['Team'] == input_team:
        input_roster.append(row)
    
input_df = pd.DataFrame(input_roster)



########################################################
# get four factor stats for each team

def get_four_factors():
    
    team_url = ('https://cleaningtheglass.com/stats/league/fourfactors#')
    
    team_res = requests.get(team_url)

    #BeautifulSoup Library parses the content of an HTML document
    team_soup = BeautifulSoup(team_res.content, 'lxml')
    
    league_stats = team_soup.find(name = 'table', attrs = {'id' : 'league_four_factors'})
    
    four_factors = []
    
    index = 0
    for row in league_stats('tr')[0:]:
        stats = {}
        for col in row:
            print(col.string)
            
            if index == 3:
                stats['Team'] = col.string
            elif index == 5:
                stats['Wins'] = col.string
            elif index == 7:
                stats['Losses'] = col.string
            elif index == 11:
                stats['Diff Rank'] = col.string
            elif index == 13:
                stats['Diff'] = col.string
            elif index == 17:
                stats['Off Pts/Poss Rank'] = col.string
            elif index == 19:
                stats['Off Pts/Poss'] = col.string
            elif index == 21:
                stats['EFG% Rank'] = col.string
            elif index == 23:
                stats['EFG%'] = col.string
            elif index == 25:
                stats['TOV% Rank'] = col.string
            elif index == 27:
                stats['TOV%'] = col.string
            elif index == 29:
                stats['ORb% Rank'] = col.string
            elif index == 31:
                stats['ORb%'] = col.string
            elif index == 33:
                stats['FT Rate Rank'] = col.string
            elif index == 35:
                stats['FT Rate'] = col.string
            elif index == 39:
                stats['Def Pts/Poss Rank'] = col.string
            elif index == 41:
                stats['Def Pts/Poss'] = col.string
            elif index == 43:
                stats['Def EFG% Ramk'] = col.string
            elif index == 45:
                stats['Def EFG%'] = col.string
            elif index == 47:
                stats['Def TOV% Rank'] = col.string
            elif index == 49:
                stats['Def TOV%'] = col.string
            elif index == 51:
                stats['Def ORb% Rank'] = col.string
            elif index == 53:
                stats['Def ORb%'] = col.string
            elif index == 55:
                stats['Def FT Rate Rank'] = col.string
            elif index == 57:
                stats['Def FT Rate'] = col.string
            
                
            index += 1
            print(index)
            
        four_factors.append(stats)    
        index = 0
            
    fourfactors_df = pd.DataFrame(four_factors)
    return(fourfactors_df)
    
df_ff = get_four_factors()

print(df_ff)

df_ff.to_csv('df_ff.csv', index=False, encoding='utf-8')


