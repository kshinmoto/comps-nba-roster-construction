# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 01:35:14 2021

@author: kshin
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
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

ssn = '2020-21'

def get_nba_stats(url):
    json_file = requests.get(url, headers=headers).json()

    data = json_file['resultSets'][0]['rowSet']
    columns = json_file['resultSets'][0]['headers']
    
    nba_stats = pd.DataFrame.from_records(data, columns=columns) 
    
    return(nba_stats)


# basic stats
df = get_nba_stats('https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight=')

# height and weight
db = get_nba_stats('https://stats.nba.com/stats/leaguedashplayerbiostats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=')

# deflections
df2 = get_nba_stats('https://stats.nba.com/stats/leaguehustlestatsplayer?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision=&Weight=')

# passing
df3 = get_nba_stats('https://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=Totals&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Passing&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=')

# speed / distance
df4 = get_nba_stats('https://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=Totals&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=SpeedDistance&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=')

# touches
df5 = get_nba_stats('https://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=Totals&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Possessions&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=')

# scoring
df6 = get_nba_stats('https://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=Totals&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Efficiency&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=')

# defense
df7 = get_nba_stats('https://stats.nba.com/stats/leaguedashptdefend?College=&Conference=&Country=&DateFrom=&DateTo=&DefenseCategory=Overall&Division=&DraftPick=&DraftYear=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=')

# advanced
df8 = get_nba_stats('https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Advanced&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight=')

# misc scoring
df9 = get_nba_stats('https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Misc&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight=')

# dws
df10 = get_nba_stats('https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Defense&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight=')

# rebounding 
df11 = get_nba_stats('https://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=Totals&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Rebounding&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=')

# shooting zones
url = 'https://stats.nba.com/stats/leaguedashplayershotlocations?College=&Conference=&Country=&DateFrom=&DateTo=&DistanceRange=By+Zone&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

json_file = requests.get(url, headers=headers).json()

data = json_file['resultSets']['rowSet']
columns = json_file['resultSets']['headers'][1]['columnNames']

df12 = pd.DataFrame.from_records(data, columns=columns) 

df12.columns = ['PLAYER_ID','PLAYER_NAME','TEAM_ID','TEAM_ABBREVIATION','AGE','NICKNAME','RAFGM','RAFGA','RAFG_PCT','PFGM','PFGA','PFG_PCT','MRFGM','MRFGA','MRFG_PCT','LCFG3M','LCFG3A','LCFG3_PCT','RCFG3M','RCFG3A','RCFG3_PCT','CFG3M','CFG3A','CFG3_PCT','ABFG3M','ABFG3A','ABFG3_PCT','CFG3M','CFG3A','CFG3_PCT']

# assisted / unassisted scoring
df13 = get_nba_stats('https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Scoring&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight=')

# usage stats
df14 = get_nba_stats('https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Usage&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight=')

# isolation plays
df15 = get_nba_stats('https://stats.nba.com/stats/synergyplaytypes?LeagueID=00&PerMode=Totals&PlayType=Isolation&PlayerOrTeam=P&SeasonType=Regular+Season&SeasonYear=' + str(ssn) + '&TypeGrouping=offensive')

df15.rename(columns={'PTS':'ISO_PTS', 'POSS':'ISO_POSS_PCT', 'EFG_PCT':'ISO_EFG_PCT'}, inplace=True)

# pnr ball handler
df16 = get_nba_stats('https://stats.nba.com/stats/synergyplaytypes?LeagueID=00&PerMode=Totals&PlayType=PRBallHandler&PlayerOrTeam=P&SeasonType=Regular+Season&SeasonYear=' + str(ssn) + '&TypeGrouping=offensive')

df16.rename(columns={'POSS_PCT':'PRBH_POSS_PCT','EFG_PCT':'PRBH_EFG_PCT','PTS':'PRBH_PTS'}, inplace=True)

g = df16.groupby(['PLAYER_NAME'])

df16 = pd.merge(g.apply(lambda x: pd.Series(np.average(x[['PRBH_POSS_PCT','PRBH_EFG_PCT']],weights=x['POSS'],axis=0),['PRBH_POSS_PCT','PRBH_EFG_PCT'])).reset_index(drop=False),pd.DataFrame(g.sum()['PRBH_PTS']).reset_index(drop=False),on='PLAYER_NAME')

##################################

# pnr man
df17 = get_nba_stats('https://stats.nba.com/stats/synergyplaytypes?LeagueID=00&PerMode=Totals&PlayType=PRRollMan&PlayerOrTeam=P&SeasonType=Regular+Season&SeasonYear=' + str(ssn) + '&TypeGrouping=offensive')

df17.rename(columns={'POSS_PCT':'PRRM_POSS_PCT','EFG_PCT':'PRRM_EFG_PCT','PTS':'PRRM_PTS'}, inplace=True)

g = df17.groupby(['PLAYER_NAME'])

df17 = pd.merge(g.apply(lambda x: pd.Series(np.average(x[['PRRM_POSS_PCT','PRRM_EFG_PCT']],weights=x['POSS'],axis=0),['PRRM_POSS_PCT','PRRM_EFG_PCT'])).reset_index(drop=False),pd.DataFrame(g.sum()['PRRM_PTS']).reset_index(drop=False),on='PLAYER_NAME')

##################################

# spot up
df18 = get_nba_stats('https://stats.nba.com/stats/synergyplaytypes?LeagueID=00&PerMode=Totals&PlayType=Spotup&PlayerOrTeam=P&SeasonType=Regular+Season&SeasonYear=' + str(ssn) + '&TypeGrouping=offensive')

df18.rename(columns={'POSS_PCT':'SU_POSS_PCT','EFG_PCT':'SU_EFG_PCT','PTS':'SU_PTS'}, inplace=True)
                 
g = df18.groupby(['PLAYER_NAME'])

df18 = pd.merge(g.apply(lambda x: pd.Series(np.average(x[['SU_POSS_PCT','SU_EFG_PCT']],weights=x['POSS'],axis=0),['SU_POSS_PCT','SU_EFG_PCT'])).reset_index(drop=False),pd.DataFrame(g.sum()['SU_PTS']).reset_index(drop=False),on='PLAYER_NAME')

##################################

# drives
df19 = get_nba_stats('https://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=Totals&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Drives&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=')

# advanced value stats
df20 = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2021_advanced.html', header=0)[0][['Player','PER','OWS','DWS','WS','WS/48','OBPM','DBPM','BPM','VORP']]

df20.columns = ['PLAYER_NAME','PER','OWS','DWS','WS','WS/48','OBPM','DBPM','BPM','VORP']

df20 = df20[df20.PLAYER_NAME !='Player'].reset_index(drop=True)

df20 = df20.drop_duplicates(subset=['PLAYER_NAME'],keep='first').reset_index(drop=True)

# basketball-reference names sometime differ from stats.nba.com names, so these discrepancies must be fixed
def remove_accents(a):
    return unidecode.unidecode(a)
df20['PLAYER_NAME'] = df20['PLAYER_NAME'].apply(remove_accents)

df20['PLAYER_NAME'].replace({'Robert Williams':'Robert Williams III','Marcus Morris':'Marcus Morris Sr.','Derrick Walton':'Derrick Walton Jr.','Juan Hernangomez':'Juancho Hernangomez','Sviatoslav Mykhailiuk':'Svi Mykhailiuk','Zach Norvell':'Zach Norvell Jr.','Lonnie Walker':'Lonnie Walker IV','Charlie Brown':'Charles Brown Jr.','C.J. Miles':'CJ Miles','Wesley Iwundu':'Wes Iwundu','J.J. Redick':'JJ Redick','B.J. Johnson':'BJ Johnson','Melvin Frazier':'Melvin Frazier Jr.','Otto Porter':'Otto Porter Jr.','James Ennis':'James Ennis III','Danuel House':'Danuel House Jr.','Brian Bowen':'Brian Bowen II','Kevin Knox':'Kevin Knox II','Frank Mason III':'Frank Mason','Harry Giles':'Harry Giles III','T.J. Leaf':'TJ Leaf','J.R. Smith':'JR Smith','Vince Edwards':'Vincent Edwards','D.J. Stephens':'DJ Stephens','Mitch Creek':'Mitchell Creek','R.J. Hunter':'RJ Hunter','Wade Baldwin':'Wade Baldwin IV'},inplace=True)

###################################

# positions
# centers
c_df = get_nba_stats('https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=C&PlusMinus=N&Rank=N&Season=' +str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight=')

# guards
g_df = get_nba_stats('https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=G&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight=')

# forwards
f_df = get_nba_stats('https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=F&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight=')

c_df['position'] = 'C'
g_df['position'] = 'G'
f_df['position'] = 'F'

pf = pd.concat([c_df,g_df,f_df]).reset_index(drop=True)
pf = pf[['PLAYER_NAME','PLAYER_ID','AGE','MIN','position']]
pf.columns = ['player','player_id','age','mp','position']

row_list = []

for n in pf.player.unique():
    
    tf = pf[pf.player == n].reset_index(drop=True)
    posf = pd.DataFrame(tf.groupby('position')['mp'].sum()).sort_values(by='mp',ascending=False).reset_index(drop=False)
    
    pos1 = posf.position[0]

    if posf.shape[0] > 1:
        pos2 = posf.position[1]
    else:
        pos2 = None
    if posf.shape[0] > 2:
        pos3 = posf.position[2]
    else:
        pos3 = None
    
    dict1 = {'player':n,'pos1':pos1,'pos2':pos2,'pos3':pos3}
    
    row_list.append(dict1)
    
pfin = pd.DataFrame(row_list)[['player','pos1','pos2','pos3']]
pfin.columns = ['PLAYER_NAME','POSITION','pos2','pos3']

#############################
# now, all 22 dataframes can be merged into one: df

df = df[['PLAYER_NAME','AGE','GP','MIN','FGM','FGA','FG3M','FG3A','FTM','FTA','OREB','DREB','REB','AST','TOV','STL','BLK','BLKA','PF','PFD','PTS']]

df = pd.merge(df,pfin[['PLAYER_NAME','POSITION']],on='PLAYER_NAME')

df = pd.merge(df,pd.get_dummies(df.POSITION), left_index=True, right_index=True) # one-hot encoding on position to create three columns: C, G, F

df = pd.merge(df,db[['PLAYER_NAME','PLAYER_HEIGHT_INCHES','PLAYER_WEIGHT','NET_RATING','OREB_PCT','DREB_PCT','USG_PCT','TS_PCT','AST_PCT']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df2[['PLAYER_NAME','CONTESTED_SHOTS','CONTESTED_SHOTS_2PT','CONTESTED_SHOTS_3PT','DEFLECTIONS','CHARGES_DRAWN','SCREEN_ASSISTS','SCREEN_AST_PTS','OFF_LOOSE_BALLS_RECOVERED','DEF_LOOSE_BALLS_RECOVERED','LOOSE_BALLS_RECOVERED','OFF_BOXOUTS','DEF_BOXOUTS','BOX_OUT_PLAYER_TEAM_REBS','BOX_OUT_PLAYER_REBS','BOX_OUTS']],on='PLAYER_NAME',how='left')
    
df = pd.merge(df,df3[['PLAYER_NAME','PASSES_MADE','PASSES_RECEIVED','FT_AST','SECONDARY_AST','POTENTIAL_AST','AST_PTS_CREATED']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df4[['PLAYER_NAME','DIST_MILES','DIST_MILES_OFF','DIST_MILES_DEF','AVG_SPEED','AVG_SPEED_OFF','AVG_SPEED_DEF']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df5[['PLAYER_NAME','TOUCHES','FRONT_CT_TOUCHES','TIME_OF_POSS','AVG_SEC_PER_TOUCH','AVG_DRIB_PER_TOUCH','PTS_PER_TOUCH','ELBOW_TOUCHES','POST_TOUCHES']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df6[['PLAYER_NAME','DRIVE_PTS','DRIVE_FG_PCT','CATCH_SHOOT_PTS','CATCH_SHOOT_FG_PCT','PULL_UP_PTS','PULL_UP_FG_PCT','PAINT_TOUCH_PTS','PAINT_TOUCH_FG_PCT','POST_TOUCH_PTS','POST_TOUCH_FG_PCT','ELBOW_TOUCH_PTS','ELBOW_TOUCH_FG_PCT']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df7[['PLAYER_NAME','D_FGM','D_FGA','D_FG_PCT']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df8[['PLAYER_NAME','OFF_RATING','DEF_RATING','AST_RATIO','PACE','PIE']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df9[['PLAYER_NAME','PTS_OFF_TOV','PTS_2ND_CHANCE','PTS_FB','PTS_PAINT']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df10[['PLAYER_NAME','DEF_WS']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df11[['PLAYER_NAME','AVG_REB_DIST','REB_CHANCE_PCT','REB_CHANCE_PCT_ADJ','REB_CHANCES','REB_CONTEST_PCT']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df12[['PLAYER_NAME','RAFGM','RAFGA','RAFG_PCT','PFGM','PFGA','PFG_PCT','MRFGM','MRFGA','MRFG_PCT','LCFG3M','LCFG3A','LCFG3_PCT','RCFG3M','RCFG3A','RCFG3_PCT','CFG3M','CFG3A','CFG3_PCT','ABFG3M','ABFG3A','ABFG3_PCT']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df13[['PLAYER_NAME','PCT_FGA_2PT','PCT_FGA_3PT','PCT_PTS_2PT','PCT_PTS_2PT_MR','PCT_PTS_3PT','PCT_PTS_FB','PCT_PTS_FT','PCT_PTS_OFF_TOV','PCT_PTS_PAINT','PCT_AST_2PM','PCT_UAST_2PM','PCT_AST_3PM','PCT_UAST_3PM', 'PCT_AST_FGM', 'PCT_UAST_FGM']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df14[['PLAYER_NAME','PCT_FGM','PCT_FGA','PCT_FG3M','PCT_FG3A','PCT_FTM','PCT_FTA','PCT_OREB','PCT_DREB','PCT_REB','PCT_AST','PCT_TOV','PCT_STL','PCT_BLK','PCT_BLKA','PCT_PF','PCT_PFD','PCT_PTS']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df15[['PLAYER_NAME','ISO_POSS_PCT','ISO_EFG_PCT','ISO_PTS']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df16[['PLAYER_NAME','PRBH_POSS_PCT','PRBH_EFG_PCT','PRBH_PTS']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df17[['PLAYER_NAME','PRRM_POSS_PCT','PRRM_EFG_PCT','PRRM_PTS']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df18[['PLAYER_NAME','SU_POSS_PCT','SU_EFG_PCT','SU_PTS']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df19[['PLAYER_NAME','DRIVES','DRIVE_AST_PCT','DRIVE_PASSES_PCT']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df20[['PLAYER_NAME','PER','OWS','WS','WS/48','OBPM','DBPM','BPM','VORP']],on='PLAYER_NAME',how='left')

#############################
# feature engineering

df['TIME_OF_POSS_36'] = 36*(df['TIME_OF_POSS']/df.MIN)
df['OFB_PCT'] = 1-(df['TIME_OF_POSS']/df.MIN)
df['PCT_PTS_ISO'] = df.ISO_PTS / df.PTS
df['PCT_PTS_PRBH'] = df.PRBH_PTS / df.PTS
df['PCT_PTS_PRRM'] = df.PRRM_PTS / df.PTS
df['PCT_PTS_SU'] = df.SU_PTS / df.PTS
df['PCT_PTS_DRIVES'] = df.DRIVE_PTS / df.PTS

df['FG2M'] = df.FGM - df.FG3M
df['FG2A'] = df.FGA - df.FG3A

df['FG_PCT'] = df.FGM/df.FGA
df['FG2_PCT'] = df.FG2M/df.FG2A
df['FG3_PCT'] = df.FG3M/df.FG3A
df['FT_PCT'] = df.FTM/df.FTA

df['AST_TO'] = df.AST/df.TOV
df['MPG'] = df.MIN/df.GP
df['EFG'] = (df.FG2M + 1.5*df.FG3M) / df.FGA
df['FTR'] = df.FTA/df.FGA

# final cleaning up

df['PLAYER_WEIGHT'] = pd.to_numeric(df['PLAYER_WEIGHT'])
df['PER'] = pd.to_numeric(df['PER'])
df['OWS'] = pd.to_numeric(df['OWS'])
df['WS'] = pd.to_numeric(df['WS'])
df['WS/48'] = pd.to_numeric(df['WS/48'])
df['OBPM'] = pd.to_numeric(df['OBPM'])
df['BPM'] = pd.to_numeric(df['DBPM'])
df['DBPM'] = pd.to_numeric(df['BPM'])
df['VORP'] = pd.to_numeric(df['VORP'])

df.fillna(0, inplace=True)
    

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import scipy.cluster.hierarchy as shc
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import silhouette_score
from sklearn.mixture import GaussianMixture
from matplotlib import ticker
import networkx as nx



testdf = df[(df.MPG > 8) & (df.GP > 15)].reset_index(drop=True) # minimum requirements

# PRINCIPAL COMPONENT ANALYSIS

features = [x for x in df.columns if (x != 'PLAYER_NAME') &  (x != 'POSITION')]

x = testdf.loc[:, features].values
y = testdf.loc[:,['PLAYER_NAME']].values

x = StandardScaler().fit_transform(x) # standardize all values

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents, columns = ['pc1', 'pc2'])

final = pd.concat([principalDf, testdf[['PLAYER_NAME']]], axis=1)

final = final[['PLAYER_NAME','pc1','pc2']]
final.columns = ['player','pc1','pc2']

# FINDING OPTIMAL NUMBER OF CLUSTERS (K) FOR K-MEANS CLUSTERING

fig = plt.figure(figsize=(8,4))

plt.subplots_adjust(wspace=0.3, hspace=None)

plt.subplot(1,2,1)

wcss = []
for n_clusters in range(2, 21):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(principalComponents)
    wcss.append(kmeans.inertia_)
plt.plot(range(2, 21), wcss)
plt.scatter(range(2, 21), wcss)
plt.title('elbow method')
plt.xlabel('number of clusters')
plt.ylabel('wcss')

plt.subplot(1,2,2)

score_list = []
for n_clusters in range(2, 21):
    local_score = []
    for n in range(1,10):
        clusterer = KMeans(n_clusters=n_clusters)
        preds = clusterer.fit_predict(principalComponents)
        score = silhouette_score(principalComponents, preds)
        local_score.append(score)
    score_list.append(sum(local_score)/len(local_score))
plt.plot(range(2, 21), score_list)
plt.scatter(range(2, 21), score_list)
plt.title('silhouette method')
plt.xlabel('number of clusters')
plt.ylabel('silhouette score')

fig.tight_layout()


# KMEANS MODEL
kmeans = KMeans(n_jobs = -1, n_clusters = 8, init='k-means++')
kmeans.fit(principalComponents)
pred0 = kmeans.predict(principalComponents)

frame = pd.DataFrame(principalComponents)
frame['cluster'] = pred0
final['cluster'] = pred0
frame['cluster'].value_counts()
principalDf['pred'] = pred0


#redo clustering

features = [x for x in df.columns if (x != 'PLAYER_NAME') &  (x != 'POSITION')]

x = testdf.loc[:, features].values
y = testdf.loc[:,['PLAYER_NAME']].values

x = StandardScaler().fit_transform(x) # standardize all values

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents, columns = ['pc1', 'pc2'])

kmeans = KMeans(n_jobs = -1, n_clusters = 8, init='k-means++')
kmeans.fit(principalComponents)
pred1 = kmeans.predict(principalComponents)

frame = pd.DataFrame(principalComponents)
frame['cluster'] = pred1
final['cluster2'] = pred1
frame['cluster'].value_counts()
principalDf['pred1'] = pred1

#redo clustering

features = [x for x in df.columns if (x != 'PLAYER_NAME') &  (x != 'POSITION')]

x = testdf.loc[:, features].values
y = testdf.loc[:,['PLAYER_NAME']].values

x = StandardScaler().fit_transform(x) # standardize all values

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents, columns = ['pc1', 'pc2'])

kmeans = KMeans(n_jobs = -1, n_clusters = 8, init='k-means++')
kmeans.fit(principalComponents)
pred1 = kmeans.predict(principalComponents)

frame = pd.DataFrame(principalComponents)
frame['cluster'] = pred1
final['cluster3'] = pred1
frame['cluster'].value_counts()
principalDf['pred1'] = pred1

#redo clustering

features = [x for x in df.columns if (x != 'PLAYER_NAME') &  (x != 'POSITION')]

x = testdf.loc[:, features].values
y = testdf.loc[:,['PLAYER_NAME']].values

x = StandardScaler().fit_transform(x) # standardize all values

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents, columns = ['pc1', 'pc2'])

kmeans = KMeans(n_jobs = -1, n_clusters = 8, init='k-means++')
kmeans.fit(principalComponents)
pred1 = kmeans.predict(principalComponents)

frame = pd.DataFrame(principalComponents)
frame['cluster'] = pred1
final['cluster4'] = pred1
frame['cluster'].value_counts()
principalDf['pred1'] = pred1

# redo clustering

features = [x for x in df.columns if (x != 'PLAYER_NAME') &  (x != 'POSITION')]

x = testdf.loc[:, features].values
y = testdf.loc[:,['PLAYER_NAME']].values

x = StandardScaler().fit_transform(x) # standardize all values

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents, columns = ['pc1', 'pc2'])

kmeans = KMeans(n_jobs = -1, n_clusters = 8, init='k-means++')
kmeans.fit(principalComponents)
pred = kmeans.predict(principalComponents)

frame = pd.DataFrame(principalComponents)
frame['cluster'] = pred
final['cluster5'] = pred
frame['cluster'].value_counts()
principalDf['pred'] = pred

u_labels = np.unique(pred)

# create lists of groups of players

cluster1_0 = []

for index, row in final.iterrows():
    if row['cluster'] == 0:
        cluster1_0.append(row['player'])

cluster1_1 = []

for index, row in final.iterrows():
    if row['cluster'] == 1:
        cluster1_1.append(row['player'])
        
cluster1_2 = [] 

for index, row in final.iterrows():
    if row['cluster'] == 2:
        cluster1_2.append(row['player'])
        
cluster1_3 = []
        
for index, row in final.iterrows():
    if row['cluster'] == 3:
        cluster1_3.append(row['player'])

cluster1_4 = []

for index, row in final.iterrows():
    if row['cluster'] == 4:
        cluster1_4.append(row['player'])
        
cluster1_5 = []

for index, row in final.iterrows():
    if row['cluster'] == 5:
        cluster1_5.append(row['player'])
        
cluster1_6 = []

for index, row in final.iterrows():
    if row['cluster'] == 6:
        cluster1_6.append(row['player'])
        
cluster1_7 = []

for index, row in final.iterrows():
    if row['cluster'] == 7:
        cluster1_7.append(row['player'])
        
#########################################
        
cluster2_0 = []

for index, row in final.iterrows():
    if row['cluster2'] == 0:
        cluster2_0.append(row['player'])

cluster2_1 = []

for index, row in final.iterrows():
    if row['cluster2'] == 1:
        cluster2_1.append(row['player'])
        
cluster2_2 = [] 

for index, row in final.iterrows():
    if row['cluster2'] == 2:
        cluster2_2.append(row['player'])
        
cluster2_3 = []
        
for index, row in final.iterrows():
    if row['cluster2'] == 3:
        cluster2_3.append(row['player'])

cluster2_4 = []

for index, row in final.iterrows():
    if row['cluster2'] == 4:
        cluster2_4.append(row['player'])
        
cluster2_5 = []

for index, row in final.iterrows():
    if row['cluster2'] == 5:
        cluster2_5.append(row['player'])
        
cluster2_6 = []

for index, row in final.iterrows():
    if row['cluster2'] == 6:
        cluster2_6.append(row['player'])
        
cluster2_7 = []

for index, row in final.iterrows():
    if row['cluster2'] == 7:
        cluster2_7.append(row['player'])
        
########################################

cluster3_0 = []

for index, row in final.iterrows():
    if row['cluster3'] == 0:
        cluster3_0.append(row['player'])

cluster3_1 = []

for index, row in final.iterrows():
    if row['cluster3'] == 1:
        cluster3_1.append(row['player'])
        
cluster3_2 = [] 

for index, row in final.iterrows():
    if row['cluster3'] == 2:
        cluster3_2.append(row['player'])
        
cluster3_3 = []
        
for index, row in final.iterrows():
    if row['cluster3'] == 3:
        cluster3_3.append(row['player'])

cluster3_4 = []

for index, row in final.iterrows():
    if row['cluster3'] == 4:
        cluster3_4.append(row['player'])
        
cluster3_5 = []

for index, row in final.iterrows():
    if row['cluster3'] == 5:
        cluster3_5.append(row['player'])
        
cluster3_6 = []

for index, row in final.iterrows():
    if row['cluster3'] == 6:
        cluster3_6.append(row['player'])
        
cluster3_7 = []

for index, row in final.iterrows():
    if row['cluster3'] == 7:
        cluster3_7.append(row['player'])
        


#### get counts of clusters/ create final groupings of players

list_role_big = []

for player in cluster1_0:
    if 'Alex Len' in cluster1_0:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_role_big.append(new_player)
        
for player in cluster1_1:
    if 'Alex Len' in cluster1_1:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_role_big.append(new_player)
        
for player in cluster1_2:
    if 'Alex Len' in cluster1_2:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_role_big.append(new_player)
        
for player in cluster1_3:
    if 'Alex Len' in cluster1_3:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_role_big.append(new_player)
        
for player in cluster1_4:
    if 'Alex Len' in cluster1_4:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_role_big.append(new_player)
        
for player in cluster1_5:
    if 'Alex Len' in cluster1_5:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_role_big.append(new_player)
        
for player in cluster1_6:
    if 'Alex Len' in cluster1_6:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_role_big.append(new_player)
        
for player in cluster1_7:
    if 'Alex Len' in cluster1_7:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_role_big.append(new_player)
        
for player in cluster2_0:
    if 'Alex Len' in cluster2_0:
        i = 0
        for player2 in list_role_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_role_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_role_big.append(new_player)
                
for player in cluster2_1:
    if 'Alex Len' in cluster2_1:
        i = 0
        for player2 in list_role_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_role_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_role_big.append(new_player)

for player in cluster2_2:
    if 'Alex Len' in cluster2_2:
        i = 0
        for player2 in list_role_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_role_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_role_big.append(new_player)
                
for player in cluster2_3:
    if 'Alex Len' in cluster2_3:
        i = 0
        for player2 in list_role_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_role_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_role_big.append(new_player)
                
for player in cluster2_4:
    if 'Alex Len' in cluster2_4:
        i = 0
        for player2 in list_role_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_role_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_role_big.append(new_player)
                
for player in cluster2_4:
    if 'Alex Len' in cluster2_4:
        i = 0
        for player2 in list_role_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_role_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_role_big.append(new_player)
                
for player in cluster2_5:
    if 'Alex Len' in cluster2_5:
        i = 0
        for player2 in list_role_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_role_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_role_big.append(new_player)
                
for player in cluster2_6:
    if 'Alex Len' in cluster2_6:
        i = 0
        for player2 in list_role_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_role_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_role_big.append(new_player)
                
for player in cluster2_7:
    if 'Alex Len' in cluster2_7:
        i = 0
        for player2 in list_role_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_role_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_role_big.append(new_player)
                
for player in cluster3_0:
    if 'Alex Len' in cluster3_0:
        i = 0
        for player2 in list_role_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_role_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_role_big.append(new_player) 
                
for player in cluster3_1:
    if 'Alex Len' in cluster3_1:
        i = 0
        for player2 in list_role_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_role_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_role_big.append(new_player) 

for player in cluster3_2:
    if 'Alex Len' in cluster3_2:
        i = 0
        for player2 in list_role_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_role_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_role_big.append(new_player)   
                
for player in cluster3_3:
    if 'Alex Len' in cluster3_3:
        i = 0
        for player2 in list_role_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_role_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_role_big.append(new_player)   
                
for player in cluster3_4:
    if 'Alex Len' in cluster3_4:
        i = 0
        for player2 in list_role_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_role_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_role_big.append(new_player)   
                
for player in cluster3_5:
    if 'Alex Len' in cluster3_5:
        i = 0
        for player2 in list_role_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_role_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_role_big.append(new_player)   
                
for player in cluster3_6:
    if 'Alex Len' in cluster3_6:
        i = 0
        for player2 in list_role_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_role_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_role_big.append(new_player)   
                
for player in cluster3_7:
    if 'Alex Len' in cluster3_7:
        i = 0
        for player2 in list_role_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_role_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_role_big.append(new_player)
                
                
                
list_trad_big = []

for player in cluster1_0:
    if 'Andre Drummond' in cluster1_0:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_trad_big.append(new_player)
        
for player in cluster1_1:
    if 'Andre Drummond' in cluster1_1:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_trad_big.append(new_player)
        
for player in cluster1_2:
    if 'Andre Drummond' in cluster1_2:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_trad_big.append(new_player)
        
for player in cluster1_3:
    if 'Andre Drummond' in cluster1_3:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_trad_big.append(new_player)
        
for player in cluster1_4:
    if 'Andre Drummond' in cluster1_4:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_trad_big.append(new_player)
        
for player in cluster1_5:
    if 'Andre Drummond' in cluster1_5:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_trad_big.append(new_player)
        
for player in cluster1_6:
    if 'Andre Drummond' in cluster1_6:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_trad_big.append(new_player)
        
for player in cluster1_7:
    if 'Andre Drummond' in cluster1_7:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_trad_big.append(new_player)
        
for player in cluster2_0:
    if 'Andre Drummond' in cluster2_0:
        i = 0
        for player2 in list_trad_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_trad_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_trad_big.append(new_player)
                
for player in cluster2_1:
    if 'Andre Drummond' in cluster2_1:
        i = 0
        for player2 in list_trad_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_trad_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_trad_big.append(new_player)

for player in cluster2_2:
    if 'Andre Drummond' in cluster2_2:
        i = 0
        for player2 in list_trad_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_trad_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_trad_big.append(new_player)
                
for player in cluster2_3:
    if 'Andre Drummond' in cluster2_3:
        i = 0
        for player2 in list_trad_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_trad_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_trad_big.append(new_player)
                
for player in cluster2_4:
    if 'Andre Drummond' in cluster2_4:
        i = 0
        for player2 in list_trad_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_trad_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_trad_big.append(new_player)
                
for player in cluster2_4:
    if 'Andre Drummond' in cluster2_4:
        i = 0
        for player2 in list_trad_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_trad_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_trad_big.append(new_player)
                
for player in cluster2_5:
    if 'Andre Drummond' in cluster2_5:
        i = 0
        for player2 in list_trad_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_trad_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_trad_big.append(new_player)
                
for player in cluster2_6:
    if 'Andre Drummond' in cluster2_6:
        i = 0
        for player2 in list_trad_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_trad_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_trad_big.append(new_player)
                
for player in cluster2_7:
    if 'Andre Drummond' in cluster2_7:
        i = 0
        for player2 in list_trad_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_trad_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_trad_big.append(new_player)
                
for player in cluster3_0:
    if 'Andre Drummond' in cluster3_0:
        i = 0
        for player2 in list_trad_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_trad_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_trad_big.append(new_player) 

for player in cluster3_1:
    if 'Andre Drummond' in cluster3_1:
        i = 0
        for player2 in list_trad_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_trad_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_trad_big.append(new_player)   
                
for player in cluster3_2:
    if 'Andre Drummond' in cluster3_2:
        i = 0
        for player2 in list_trad_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_trad_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_trad_big.append(new_player)   
                
for player in cluster3_3:
    if 'Andre Drummond' in cluster3_3:
        i = 0
        for player2 in list_trad_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_trad_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_trad_big.append(new_player)   
                
for player in cluster3_4:
    if 'Andre Drummond' in cluster3_4:
        i = 0
        for player2 in list_trad_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_trad_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_trad_big.append(new_player)   
                
for player in cluster3_5:
    if 'Andre Drummond' in cluster3_5:
        i = 0
        for player2 in list_trad_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_trad_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_trad_big.append(new_player)   
                
for player in cluster3_6:
    if 'Andre Drummond' in cluster3_6:
        i = 0
        for player2 in list_trad_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_trad_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_trad_big.append(new_player)   
                
for player in cluster3_7:
    if 'Andre Drummond' in cluster3_7:
        i = 0
        for player2 in list_trad_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_trad_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_trad_big.append(new_player)
                
                
list_ball_dom = []

for player in cluster1_0:
    if 'LeBron James' in cluster1_0:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_ball_dom.append(new_player)
        
for player in cluster1_1:
    if 'LeBron James' in cluster1_1:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_ball_dom.append(new_player)
        
for player in cluster1_2:
    if 'LeBron James' in cluster1_2:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_ball_dom.append(new_player)
        
for player in cluster1_3:
    if 'LeBron James' in cluster1_3:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_ball_dom.append(new_player)
        
for player in cluster1_4:
    if 'LeBron James' in cluster1_4:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_ball_dom.append(new_player)
        
for player in cluster1_5:
    if 'LeBron James' in cluster1_5:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_ball_dom.append(new_player)
        
for player in cluster1_6:
    if 'LeBron James' in cluster1_6:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_ball_dom.append(new_player)
        
for player in cluster1_7:
    if 'LeBron James' in cluster1_7:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_ball_dom.append(new_player)
        
for player in cluster2_0:
    if 'LeBron James' in cluster2_0:
        i = 0
        for player2 in list_ball_dom:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_ball_dom)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_ball_dom.append(new_player)
                
for player in cluster2_1:
    if 'LeBron James' in cluster2_1:
        i = 0
        for player2 in list_ball_dom:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_ball_dom)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_ball_dom.append(new_player)

for player in cluster2_2:
    if 'LeBron James' in cluster2_2:
        i = 0
        for player2 in list_ball_dom:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_ball_dom)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_ball_dom.append(new_player)
                
for player in cluster2_3:
    if 'LeBron James' in cluster2_3:
        i = 0
        for player2 in list_ball_dom:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_ball_dom)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_ball_dom.append(new_player)
                
for player in cluster2_4:
    if 'LeBron James' in cluster2_4:
        i = 0
        for player2 in list_ball_dom:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_ball_dom)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_ball_dom.append(new_player)
                
                
for player in cluster2_5:
    if 'LeBron James' in cluster2_5:
        i = 0
        for player2 in list_ball_dom:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_ball_dom)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_ball_dom.append(new_player)
                
for player in cluster2_6:
    if 'LeBron James' in cluster2_6:
        i = 0
        for player2 in list_ball_dom:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_ball_dom)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_ball_dom.append(new_player)
                
for player in cluster2_7:
    if 'LeBron James' in cluster2_7:
        i = 0
        for player2 in list_ball_dom:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_ball_dom)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_ball_dom.append(new_player)
                
for player in cluster3_0:
    if 'LeBron James' in cluster3_0:
        i = 0
        for player2 in list_ball_dom:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_ball_dom)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_ball_dom.append(new_player) 

for player in cluster3_1:
    if 'LeBron James' in cluster3_1:
        i = 0
        for player2 in list_ball_dom:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_ball_dom)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_ball_dom.append(new_player)   
                
for player in cluster3_2:
    if 'LeBron James' in cluster3_2:
        i = 0
        for player2 in list_ball_dom:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_ball_dom)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_ball_dom.append(new_player)   
                
for player in cluster3_3:
    if 'LeBron James' in cluster3_3:
        i = 0
        for player2 in list_ball_dom:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_ball_dom)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_ball_dom.append(new_player)   
                
for player in cluster3_4:
    if 'LeBron James' in cluster3_4:
        i = 0
        for player2 in list_ball_dom:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_ball_dom)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_ball_dom.append(new_player)   
                
for player in cluster3_5:
    if 'LeBron James' in cluster3_5:
        i = 0
        for player2 in list_ball_dom:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_ball_dom)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_ball_dom.append(new_player)   
                
for player in cluster3_6:
    if 'LeBron James' in cluster3_6:
        i = 0
        for player2 in list_ball_dom:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_ball_dom)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_ball_dom.append(new_player)   
                
for player in cluster3_7:
    if 'LeBron James' in cluster3_7:
        i = 0
        for player2 in list_ball_dom:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_ball_dom)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_ball_dom.append(new_player)
                

list_high_usg_big = []

for player in cluster1_0:
    if 'Giannis Antetokounmpo' in cluster1_0:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_high_usg_big.append(new_player)
        
for player in cluster1_1:
    if 'Giannis Antetokounmpo' in cluster1_1:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_high_usg_big.append(new_player)
        
for player in cluster1_2:
    if 'Giannis Antetokounmpo' in cluster1_2:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_high_usg_big.append(new_player)
        
for player in cluster1_3:
    if 'Giannis Antetokounmpo' in cluster1_3:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_high_usg_big.append(new_player)
        
for player in cluster1_4:
    if 'Giannis Antetokounmpo' in cluster1_4:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_high_usg_big.append(new_player)
        
for player in cluster1_5:
    if 'Giannis Antetokounmpo' in cluster1_5:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_high_usg_big.append(new_player)
        
for player in cluster1_6:
    if 'Giannis Antetokounmpo' in cluster1_6:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_high_usg_big.append(new_player)
        
for player in cluster1_7:
    if 'Giannis Antetokounmpo' in cluster1_7:
        new_player = {}
        new_player['player'] = player
        new_player['count'] = 1
        list_high_usg_big.append(new_player)
        
for player in cluster2_0:
    if 'Giannis Antetokounmpo' in cluster2_0:
        i = 0
        for player2 in list_high_usg_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_high_usg_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_high_usg_big.append(new_player)
                
for player in cluster2_1:
    if 'Giannis Antetokounmpo' in cluster2_1:
        i = 0
        for player2 in list_high_usg_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_high_usg_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_high_usg_big.append(new_player)

for player in cluster2_2:
    if 'Giannis Antetokounmpo' in cluster2_2:
        i = 0
        for player2 in list_high_usg_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_high_usg_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_high_usg_big.append(new_player)
                
for player in cluster2_3:
    if 'Giannis Antetokounmpo' in cluster2_3:
        i = 0
        for player2 in list_high_usg_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_high_usg_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_high_usg_big.append(new_player)
                
for player in cluster2_4:
    if 'Giannis Antetokounmpo' in cluster2_4:
        i = 0
        for player2 in list_high_usg_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_high_usg_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_high_usg_big.append(new_player)
                
                
for player in cluster2_5:
    if 'Giannis Antetokounmpo' in cluster2_5:
        i = 0
        for player2 in list_high_usg_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_high_usg_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_high_usg_big.append(new_player)
                
for player in cluster2_6:
    if 'Giannis Antetokounmpo' in cluster2_6:
        i = 0
        for player2 in list_high_usg_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_high_usg_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_high_usg_big.append(new_player)
                
for player in cluster2_7:
    if 'Giannis Antetokounmpo' in cluster2_7:
        i = 0
        for player2 in list_high_usg_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_high_usg_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_high_usg_big.append(new_player)
                
for player in cluster3_0:
    if 'Giannis Antetokounmpo' in cluster3_0:
        i = 0
        for player2 in list_high_usg_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_high_usg_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_high_usg_big.append(new_player) 

for player in cluster3_1:
    if 'Giannis Antetokounmpo' in cluster3_1:
        i = 0
        for player2 in list_high_usg_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_high_usg_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_high_usg_big.append(new_player)   
                
for player in cluster3_2:
    if 'Giannis Antetokounmpo' in cluster3_2:
        i = 0
        for player2 in list_high_usg_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_high_usg_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_high_usg_big.append(new_player)   
                
for player in cluster3_3:
    if 'Giannis Antetokounmpo' in cluster3_3:
        i = 0
        for player2 in list_high_usg_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_high_usg_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_high_usg_big.append(new_player)   
                
for player in cluster3_4:
    if 'Giannis Antetokounmpo' in cluster3_4:
        i = 0
        for player2 in list_high_usg_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_high_usg_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_high_usg_big.append(new_player)   
                
for player in cluster3_5:
    if 'Giannis Antetokounmpo' in cluster3_5:
        i = 0
        for player2 in list_high_usg_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_high_usg_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_high_usg_big.append(new_player)   
                
for player in cluster3_6:
    if 'Giannis Antetokounmpo' in cluster3_6:
        i = 0
        for player2 in list_high_usg_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_high_usg_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_high_usg_big.append(new_player)   
                
for player in cluster3_7:
    if 'Giannis Antetokounmpo' in cluster3_7:
        i = 0
        for player2 in list_high_usg_big:
            if player == player2['player']:
                player2['count'] = player2['count'] + 1
                break
            if i == len(list_high_usg_big)-1:
                new_player['player'] = player
                new_player['count'] = 1
                list_high_usg_big.append(new_player)

list_role_guard = []

def make_role_guard_list(cluster, glist):
    for player in cluster:
        if 'Aaron Holiday' in cluster:
            new_player = {}
            new_player['player'] = player
            new_player['count'] = 1
            glist.append(new_player)
            
make_role_guard_list(cluster1_0, list_role_guard)

make_role_guard_list(cluster1_1, list_role_guard)

make_role_guard_list(cluster1_2, list_role_guard)

make_role_guard_list(cluster1_3, list_role_guard)

make_role_guard_list(cluster1_4, list_role_guard)

make_role_guard_list(cluster1_5, list_role_guard)

make_role_guard_list(cluster1_6, list_role_guard)

make_role_guard_list(cluster1_7, list_role_guard)

def add_role_guard_list(cluster, glist):
    for player in cluster:
        if 'Aaron Holiday' in cluster:
            i = 0
            for player2 in glist:
                if player == player2['player']:
                    player2['count'] = player2['count'] + 1
                    break
                if i == len(glist)-1:
                    new_player['player'] = player
                    new_player['count'] = 1
                    glist.append(new_player)
                    
add_role_guard_list(cluster2_0, list_role_guard)

add_role_guard_list(cluster2_1, list_role_guard)

add_role_guard_list(cluster2_2, list_role_guard)

add_role_guard_list(cluster2_3, list_role_guard)

add_role_guard_list(cluster2_4, list_role_guard)

add_role_guard_list(cluster2_5, list_role_guard)

add_role_guard_list(cluster2_6, list_role_guard)

add_role_guard_list(cluster2_7, list_role_guard)

add_role_guard_list(cluster3_0, list_role_guard)

add_role_guard_list(cluster3_1, list_role_guard)

add_role_guard_list(cluster3_2, list_role_guard)

add_role_guard_list(cluster3_3, list_role_guard)

add_role_guard_list(cluster3_4, list_role_guard)

add_role_guard_list(cluster3_5, list_role_guard)

add_role_guard_list(cluster3_6, list_role_guard)

add_role_guard_list(cluster3_7, list_role_guard)


list_off_bench = []

def make_off_bench_list(cluster, glist):
    for player in cluster:
        if 'Yuta Watanabe' in cluster:
            new_player = {}
            new_player['player'] = player
            new_player['count'] = 1
            glist.append(new_player)
            
make_off_bench_list(cluster1_0, list_off_bench)

make_off_bench_list(cluster1_1, list_off_bench)

make_off_bench_list(cluster1_2, list_off_bench)

make_off_bench_list(cluster1_3, list_off_bench)

make_off_bench_list(cluster1_4, list_off_bench)

make_off_bench_list(cluster1_5, list_off_bench)

make_off_bench_list(cluster1_6, list_off_bench)

make_off_bench_list(cluster1_7, list_off_bench)

def add_off_bench_list(cluster, glist):
    for player in cluster:
        if 'Yuta Watanabe' in cluster:
            i = 0
            for player2 in glist:
                if player == player2['player']:
                    player2['count'] = player2['count'] + 1
                    break
                if i == len(glist)-1:
                    new_player['player'] = player
                    new_player['count'] = 1
                    glist.append(new_player)
                    
add_off_bench_list(cluster2_0, list_off_bench)

add_off_bench_list(cluster2_1, list_off_bench)

add_off_bench_list(cluster2_2, list_off_bench)

add_off_bench_list(cluster2_3, list_off_bench)

add_off_bench_list(cluster2_4, list_off_bench)

add_off_bench_list(cluster2_5, list_off_bench)

add_off_bench_list(cluster2_6, list_off_bench)

add_off_bench_list(cluster2_7, list_off_bench)

add_off_bench_list(cluster3_0, list_off_bench)

add_off_bench_list(cluster3_1, list_off_bench)

add_off_bench_list(cluster3_2, list_off_bench)

add_off_bench_list(cluster3_3, list_off_bench)

add_off_bench_list(cluster3_4, list_off_bench)

add_off_bench_list(cluster3_5, list_off_bench)

add_off_bench_list(cluster3_6, list_off_bench)

add_off_bench_list(cluster3_7, list_off_bench)



list_secondary = []

def make_secondary_list(cluster, glist):
    for player in cluster:
        if 'Bogdan Bogdanovic' in cluster:
            new_player = {}
            new_player['player'] = player
            new_player['count'] = 1
            glist.append(new_player)
            
make_secondary_list(cluster1_0, list_secondary)

make_secondary_list(cluster1_1, list_secondary)

make_secondary_list(cluster1_2, list_secondary)

make_secondary_list(cluster1_3, list_secondary)

make_secondary_list(cluster1_4, list_secondary)

make_secondary_list(cluster1_5, list_secondary)

make_secondary_list(cluster1_6, list_secondary)

make_secondary_list(cluster1_7, list_secondary)

def add_secondary_list(cluster, glist):
    for player in cluster:
        if 'Bogdan Bogdanovic' in cluster:
            i = 0
            for player2 in glist:
                if player == player2['player']:
                    player2['count'] = player2['count'] + 1
                    break
                if i == len(glist)-1:
                    new_player['player'] = player
                    new_player['count'] = 1
                    glist.append(new_player)
                    
add_secondary_list(cluster2_0, list_secondary)

add_secondary_list(cluster2_1, list_secondary)

add_secondary_list(cluster2_2, list_secondary)

add_secondary_list(cluster2_3, list_secondary)

add_secondary_list(cluster2_4, list_secondary)

add_secondary_list(cluster2_5, list_secondary)

add_secondary_list(cluster2_6, list_secondary)

add_secondary_list(cluster2_7, list_secondary)

add_secondary_list(cluster3_0, list_secondary)

add_secondary_list(cluster3_1, list_secondary)

add_secondary_list(cluster3_2, list_secondary)

add_secondary_list(cluster3_3, list_secondary)

add_secondary_list(cluster3_4, list_secondary)

add_secondary_list(cluster3_5, list_secondary)

add_secondary_list(cluster3_6, list_secondary)

add_secondary_list(cluster3_7, list_secondary)


list_versatile_forwards = []

def make_versatile_list(cluster, glist):
    for player in cluster:
        if 'Aaron Gordon' in cluster:
            new_player = {}
            new_player['player'] = player
            new_player['count'] = 1
            glist.append(new_player)
            
make_versatile_list(cluster1_0, list_versatile_forwards)

make_versatile_list(cluster1_1, list_versatile_forwards)

make_versatile_list(cluster1_2, list_versatile_forwards)

make_versatile_list(cluster1_3, list_versatile_forwards)

make_versatile_list(cluster1_4, list_versatile_forwards)

make_versatile_list(cluster1_5, list_versatile_forwards)

make_versatile_list(cluster1_6, list_versatile_forwards)

make_versatile_list(cluster1_7, list_versatile_forwards)

def add_versatile_list(cluster, glist):
    for player in cluster:
        if 'Aaron Gordon' in cluster:
            i = 0
            for player2 in glist:
                if player == player2['player']:
                    player2['count'] = player2['count'] + 1
                    break
                if i == len(glist)-1:
                    new_player['player'] = player
                    new_player['count'] = 1
                    glist.append(new_player)
                    
add_versatile_list(cluster2_0, list_versatile_forwards)

add_versatile_list(cluster2_1, list_versatile_forwards)

add_versatile_list(cluster2_2, list_versatile_forwards)

add_versatile_list(cluster2_3, list_versatile_forwards)

add_versatile_list(cluster2_4, list_versatile_forwards)

add_versatile_list(cluster2_5, list_versatile_forwards)

add_versatile_list(cluster2_6, list_versatile_forwards)

add_versatile_list(cluster2_7, list_versatile_forwards)

add_versatile_list(cluster3_0, list_versatile_forwards)

add_versatile_list(cluster3_1, list_versatile_forwards)

add_versatile_list(cluster3_2, list_versatile_forwards)

add_versatile_list(cluster3_3, list_versatile_forwards)

add_versatile_list(cluster3_4, list_versatile_forwards)

add_versatile_list(cluster3_5, list_versatile_forwards)

add_versatile_list(cluster3_6, list_versatile_forwards)

add_versatile_list(cluster3_7, list_versatile_forwards)


# get rid of players in each list that have a count of less than 2

index = 0
for player in list_ball_dom:
    if player['count'] < 2:
        print(index)
        del list_ball_dom[index]
    index+=1
    
index = 0
for player in list_high_usg_big:
    if player['count'] < 2:
        print(index)
        del list_high_usg_big[index]
    index+=1
    
index = 0    
for player in list_off_bench:
    if player['count'] < 2:
        print(index)
        del list_off_bench[index]
    index+=1
    
index = 0        
for player in list_role_big:
    if player['count'] < 2:
        print(index)
        del list_role_big[index]
    index+=1

index = 0        
for player in list_role_guard:
    if player['count'] < 2:
        print(index)
        del list_role_guard[index]
    index+=1

index = 0        
for player in list_secondary:
    if player['count'] < 2:
        print(index)
        del list_secondary[index]
    index+=1

index = 0        
for player in list_trad_big:
    if player['count'] < 2:
        print(index)
        del list_trad_big[index]
    index+=1

index = 0        
for player in list_versatile_forwards:
    if player['count'] < 2:
        print(index)
        del list_versatile_forwards[index]
    index+=1

# turn lists into dataframes
df_ball_dom = pd.DataFrame(list_ball_dom)
df_high_usg_big = pd.DataFrame(list_high_usg_big)
df_off_bench = pd.DataFrame(list_off_bench)
df_role_big = pd.DataFrame(list_role_big)
df_role_guard = pd.DataFrame(list_role_guard)
df_secondary = pd.DataFrame(list_secondary)
df_trad_big = pd.DataFrame(list_trad_big)
df_versatile_forwards = pd.DataFrame(list_versatile_forwards)

# turn df of players in csv files
df_ball_dom.to_csv('ball_dom.csv', index=False, encoding='utf-8')
df_high_usg_big.to_csv('high_usg_big.csv', index=False, encoding='utf-8')
df_off_bench.to_csv('off_bench.csv', index=False, encoding='utf-8')
df_role_big.to_csv('role_big.csv', index=False, encoding='utf-8')
df_role_guard.to_csv('role_guard.csv', index=False, encoding='utf-8')
df_secondary.to_csv('secondary.csv', index=False, encoding='utf-8')
df_trad_big.to_csv('trad_big.csv', index=False, encoding='utf-8')
df_versatile_forwards.to_csv('vers_forwards.csv', index=False, encoding='utf-8')



#plotting the results:
 
filtered_label0 = principalDf[pred == 0]

plt.scatter(filtered_label0.iloc[:,0] , filtered_label0.iloc[:,1])
plt.show()

filtered_label1 = principalDf[pred == 1]
filtered_label2 = principalDf[pred == 2]
filtered_label3 = principalDf[pred == 3]
filtered_label4 = principalDf[pred == 4]
filtered_label5 = principalDf[pred == 5]
filtered_label6 = principalDf[pred == 6]
filtered_label7 = principalDf[pred == 7]
 
#Plotting the results
plt.scatter(filtered_label0.iloc[:,0] , filtered_label0.iloc[:,1] , color = 'red')
plt.scatter(filtered_label1.iloc[:,0] , filtered_label1.iloc[:,1] , color = 'black')
plt.scatter(filtered_label2.iloc[:,0] , filtered_label2.iloc[:,1] , color = 'green')
plt.scatter(filtered_label3.iloc[:,0] , filtered_label3.iloc[:,1] , color = 'blue')
plt.scatter(filtered_label4.iloc[:,0] , filtered_label4.iloc[:,1] , color = 'yellow')
plt.scatter(filtered_label5.iloc[:,0] , filtered_label5.iloc[:,1] , color = 'brown')
plt.scatter(filtered_label6.iloc[:,0] , filtered_label6.iloc[:,1] , color = 'pink')
plt.scatter(filtered_label7.iloc[:,0] , filtered_label7.iloc[:,1] , color = 'orange')
plt.show()

