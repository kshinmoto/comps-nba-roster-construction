# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 14:13:08 2021

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

### load in csv files of our scraped data
concat_4 = pd.read_csv (r'C:\Users\kshin\Desktop\Sports Comps\concat_4_ranks.csv') 
concat_4_defense = pd.read_csv(r'C:\Users\kshin\Desktop\Sports Comps\concat_4_def_ranks.csv')

four_factors = pd.read_csv(r'C:\Users\kshin\Desktop\Sports Comps\df_ff.csv')

### clean df
four_factors = four_factors.fillna(0)
four_factors = four_factors.drop(labels=[0,1], axis=0)

### turn df rank columns into numeric values
four_factors['Off Pts/Poss Rank'] = four_factors['Off Pts/Poss Rank'].astype(int)
four_factors['EFG% Rank'] = four_factors['EFG% Rank'].astype(int)
four_factors['TOV% Rank'] = four_factors['TOV% Rank'].astype(int)
four_factors['ORb% Rank'] = four_factors['ORb% Rank'].astype(int)
four_factors['FT Rate Rank'] = four_factors['FT Rate Rank'].astype(int)


########################################################################################

### test out comparing players and making algo

temp_values = {
    'temp_off_pts_poss' : 0,
    'temp_off_efg' : 0,
    'temp_off_tov' : 0,
    'temp_off_orb' : 0,
    'temp_off_ft' : 0,
    'temp_def_pts_poss' : 0,
    'temp_def_efg' : 0,
    'temp_def_tov' : 0,
    'temp_def_orb' : 0,
    'temp_def_ft' : 0,
    }

#######################
'''
temp_off_pts_poss = 0
temp_off_efg = 0
temp_off_tov = 0
temp_off_orb = 0
temp_off_ft = 0
temp_def_pts_poss = 0
temp_def_efg = 0
temp_def_tov = 0
temp_def_orb = 0
temp_def_ft = 0
'''
#######################

for index, row in four_factors.iterrows():
    if row['Team'] == 'Atlanta':
        if row['Off Pts/Poss Rank'] > 15:
            temp_values['temp_off_pts_poss'] = row['Off Pts/Poss Rank'] - 15
        if row['EFG% Rank'] > 15:
            temp_values['temp_off_efg'] = row['EFG% Rank'] - 15
        if row['TOV% Rank'] > 15:
            temp_values['temp_off_tov'] = row['TOV% Rank'] - 15
        if row['ORb% Rank'] > 15:
            temp_values['temp_off_orb'] = row['ORb% Rank'] - 15
        if row['FT Rate Rank'] > 15:
            temp_values['temp_off_ft'] = row['FT Rate Rank'] - 15
        if row['Def Pts/Poss Rank'] > 15:
            temp_values['temp_def_pts_poss'] = row['Def Pts/Poss Rank'] - 15
        if row['Def EFG% Ramk'] > 15:
            temp_values['temp_def_efg'] = row['Def EFG% Ramk'] - 15
        if row['Def TOV% Rank'] > 15:
            temp_values['temp_def_tov'] = row['Def TOV% Rank'] - 15
        if row['Def ORb% Rank'] > 15:
            temp_values['temp_def_orb'] = row['Def ORb% Rank'] - 15
        if row['Def FT Rate Rank'] > 15:
            temp_values['temp_def_ft'] = row['Def FT Rate Rank'] - 15
            
# create dataframe of team roster
team_roster = []

for index, row in concat_4.iterrows():
    if row['Team_x'] == 'ATL':
        team_roster.append(row)

team_roster = pd.DataFrame(team_roster)

### sort value dict in descending order
sorted_values = sorted(temp_values.items(), key=lambda x: x[1], reverse=True)


### loop through our sorted list and find weaknesses
weakness_list = []

for pair in sorted_values:
    if pair[1] > 0:
        weakness_list.append(pair[0])
        
### create variables that will hold the categories our team is weak in
first_weakness = ''
second_weakness = ''
third_weakness = ''
fourth_weakness = ''

if len(weakness_list) > 0:
    first_weakness = weakness_list[0]
if len(weakness_list) > 1:
    second_weakness = weakness_list[1]
if len(weakness_list) > 2:
    third_weakness = weakness_list[2]
if len(weakness_list) > 3:
    fourth_weakness = weakness_list[3] 

    
### create dataframe of weaknesses and which stat categories fall within them

# first create dictionaries of each weakness

off_pts_poss = ['EFG% Rank', 'PPG Rank', 'FGM Rank', 'FG% Rank']
off_efg = ['EFG% Rank', 'FG% Rank', '3pt% Rank', '2pt% Rank']
off_tov = ['TO Rank']
off_orb = ['ORb Rank', 'TRb Rank']
off_ft = ['FTM Rank', 'FTA Rank', 'FT% Rank']
def_pts_poss = ['PCT_PM Rank', 'D_FG% Rank', 'BLK Rank', 'STL Rank']
def_efg = ['PCT_PM Rank', 'D_FG% Rank', 'BLK Rank']
def_tov = ['STL Rank', 'BLK Rank']
def_orb = ['DRb Rank', 'TRb Rank']
def_ft = ['PF Rank', 'STL Rank']

weakness_stats_list = []
weakness_stats_list.append(off_pts_poss)
weakness_stats_list.append(off_efg)
weakness_stats_list.append(off_tov)
weakness_stats_list.append(off_orb)
weakness_stats_list.append(off_ft)
weakness_stats_list.append(def_pts_poss)
weakness_stats_list.append(def_efg)
weakness_stats_list.append(def_tov)
weakness_stats_list.append(def_orb)
weakness_stats_list.append(def_ft)











            








