# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 22:02:49 2021

@author: kshin
"""

import pandas as pd


### load in csv files of our scraped data
concat_4 = pd.read_csv (r'C:\Users\kshin\Desktop\Sports Comps\new_concat_4.csv') 
concat_4_defense = pd.read_csv(r'C:\Users\kshin\Desktop\Sports Comps\new_concat_4_defense.csv')

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


########################################################################################

### create percentile ranking for each player's stats in their role
def player_percentiles(role):
    role_list = []
    
    # loop through concat list and get role list
    for index, row in concat_4.iterrows():
        if row['Role'] == role: # role
            role_list.append(row)
    
    # turn list into dataframe
    role_df = pd.DataFrame(role_list)

    # create function that makes list of numbers 1 to len(ordered_list)
    def createList(r1, r2):
        return list(range(r1, r2+1))
    
    rank_list = createList(1, len(role_list))
    rank_list = sorted(rank_list, reverse=True)
    
    percentile_list = []
    
    for num in rank_list:
        percentile_list.append(round(num/len(role_list), 2))
    
    # insert player percentiles rank for each stat
    role_df = role_df.sort_values(by=['FGM'], ascending=False)
    role_df.insert(5, 'FGM Rank', percentile_list)
    
    # repeat for rest of stats
    role_df = role_df.sort_values(by=['FGA'], ascending=False)
    role_df.insert(7, 'FGA Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['FG %'], ascending=False)
    role_df.insert(9, 'FG% Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['3pt'], ascending=False)
    role_df.insert(11, '3ptM Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['3ptA'], ascending=False)
    role_df.insert(13, '3ptA Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['3pt %'], ascending=False)
    role_df.insert(15, '3pt% Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['2pt'], ascending=False)
    role_df.insert(17, '2ptM Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['2ptA'], ascending=False)
    role_df.insert(19, '2ptA Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['2pt %'], ascending=False)
    role_df.insert(21, '2pt% Rank', percentile_list)
        
    role_df = role_df.sort_values(by=['EFG %'], ascending=False)
    role_df.insert(23, 'EFG% Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['FTM'], ascending=False)
    role_df.insert(25, 'FTM Rank', percentile_list)
        
    role_df = role_df.sort_values(by=['FTA'], ascending=False)
    role_df.insert(27, 'FTA Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['FT %'], ascending=False)
    role_df.insert(29, 'FT% Rank', percentile_list)
        
    role_df = role_df.sort_values(by=['ORb'], ascending=False)
    role_df.insert(31, 'ORb Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['DRb'], ascending=False)
    role_df.insert(33, 'DRb Rank', percentile_list)
            
    role_df = role_df.sort_values(by=['Rebounds'], ascending=False)
    role_df.insert(35, 'TRb Rank', percentile_list)

    role_df = role_df.sort_values(by=['Assists'], ascending=False)
    role_df.insert(37, 'AST Rank', percentile_list)

    role_df = role_df.sort_values(by=['Steals'], ascending=False)
    role_df.insert(39, 'STL Rank', percentile_list)

    role_df = role_df.sort_values(by=['Blocks'], ascending=False)
    role_df.insert(41, 'BLK Rank', percentile_list)

    role_df = role_df.sort_values(by=['Turnovers'], ascending=False)
    role_df.insert(43, 'TO Rank', percentile_list)

    role_df = role_df.sort_values(by=['PF'], ascending=False)
    role_df.insert(45, 'PF Rank', percentile_list)

    role_df = role_df.sort_values(by=['PPG'], ascending=False)
    role_df.insert(47, 'PPG Rank', percentile_list)
    
    return role_df

### create df for each role
trad_big_df = player_percentiles('Traditional Big')
ball_dom_df = player_percentiles('Ball Dominant')
high_usg_big_df = player_percentiles('High Usage Big')
off_bench_df = player_percentiles('Off Bench')
role_big_df = player_percentiles('Roleplaying Big')
role_guard_df = player_percentiles('Roleplaying Guard')
secondary_df = player_percentiles('Secondary Playmaker')
vers_forwards_df = player_percentiles('Versatile Forward')

### add each df to a single list, then concat stats and sort by team name
concat_list_ranks = []

concat_list_ranks.append(trad_big_df)
concat_list_ranks.append(ball_dom_df)
concat_list_ranks.append(high_usg_big_df)
concat_list_ranks.append(off_bench_df)
concat_list_ranks.append(role_big_df)
concat_list_ranks.append(role_guard_df)
concat_list_ranks.append(secondary_df)
concat_list_ranks.append(vers_forwards_df)

concat_list_ranks = pd.concat(concat_list_ranks)

concat_list_ranks = concat_list_ranks.sort_index()

concat_list_ranks.to_csv('concat_4_ranks.csv', index=False, encoding='utf-8')


### repeat for defensive concat dataframe
def player_percentiles_def(role):
    role_list = []
    
    # loop through concat list and get role list
    for index, row in concat_4_defense.iterrows():
        if row['Role'] == role: # role
            role_list.append(row)
    
    # turn list into dataframe
    role_df = pd.DataFrame(role_list)

    # create function that makes list of numbers 1 to len(ordered_list)
    def createList(r1, r2):
        return list(range(r1, r2+1))
    
    rank_list = createList(1, len(role_list))
    rank_list = sorted(rank_list, reverse=True)
    
    percentile_list = []
    
    for num in rank_list:
        percentile_list.append(round(num/len(role_list), 2))
    
    # insert player percentiles rank for each stat
    role_df = role_df.sort_values(by=['FGM'], ascending=False)
    role_df.insert(5, 'FGM Rank', percentile_list)
    
    # repeat for rest of stats
    role_df = role_df.sort_values(by=['FGA'], ascending=False)
    role_df.insert(7, 'FGA Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['FG %'], ascending=False)
    role_df.insert(9, 'FG% Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['3pt'], ascending=False)
    role_df.insert(11, '3ptM Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['3ptA'], ascending=False)
    role_df.insert(13, '3ptA Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['3pt %'], ascending=False)
    role_df.insert(15, '3pt% Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['2pt'], ascending=False)
    role_df.insert(17, '2ptM Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['2ptA'], ascending=False)
    role_df.insert(19, '2ptA Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['2pt %'], ascending=False)
    role_df.insert(21, '2pt% Rank', percentile_list)
        
    role_df = role_df.sort_values(by=['EFG %'], ascending=False)
    role_df.insert(23, 'EFG% Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['FTM'], ascending=False)
    role_df.insert(25, 'FTM Rank', percentile_list)
        
    role_df = role_df.sort_values(by=['FTA'], ascending=False)
    role_df.insert(27, 'FTA Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['FT %'], ascending=False)
    role_df.insert(29, 'FT% Rank', percentile_list)
        
    role_df = role_df.sort_values(by=['ORb'], ascending=False)
    role_df.insert(31, 'ORb Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['DRb'], ascending=False)
    role_df.insert(33, 'DRb Rank', percentile_list)
            
    role_df = role_df.sort_values(by=['Rebounds'], ascending=False)
    role_df.insert(35, 'TRb Rank', percentile_list)

    role_df = role_df.sort_values(by=['Assists'], ascending=False)
    role_df.insert(37, 'AST Rank', percentile_list)

    role_df = role_df.sort_values(by=['Steals'], ascending=False)
    role_df.insert(39, 'STL Rank', percentile_list)

    role_df = role_df.sort_values(by=['Blocks'], ascending=False)
    role_df.insert(41, 'BLK Rank', percentile_list)

    role_df = role_df.sort_values(by=['Turnovers'], ascending=False)
    role_df.insert(43, 'TO Rank', percentile_list)

    role_df = role_df.sort_values(by=['PF'], ascending=False)
    role_df.insert(45, 'PF Rank', percentile_list)

    role_df = role_df.sort_values(by=['PPG'], ascending=False)
    role_df.insert(47, 'PPG Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['D_FGM'], ascending=True)
    role_df.insert(51, 'D_FGM Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['D_FGA'], ascending=True)
    role_df.insert(53, 'D_FGA Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['D_FG_PCT'], ascending=True)
    role_df.insert(55, 'D_FG% Rank', percentile_list)
    
    role_df = role_df.sort_values(by=['PCT_PLUSMINUS'], ascending=True)
    role_df.insert(58, 'PCT_PM Rank', percentile_list)
    
    return role_df


### create df for each role
trad_big_def_df = player_percentiles_def('Traditional Big')
ball_dom_def_df = player_percentiles_def('Ball Dominant')
high_usg_big_def_df = player_percentiles_def('High Usage Big')
off_bench_def_df = player_percentiles_def('Off Bench')
role_big_def_df = player_percentiles_def('Roleplaying Big')
role_guard_def_df = player_percentiles_def('Roleplaying Guard')
secondary_def_df = player_percentiles_def('Secondary Playmaker')
vers_forwards_def_df = player_percentiles_def('Versatile Forward')

### add each df to a single list, then concat stats and sort by team name
concat_def_list_ranks = []

concat_def_list_ranks.append(trad_big_def_df)
concat_def_list_ranks.append(ball_dom_def_df)
concat_def_list_ranks.append(high_usg_big_def_df)
concat_def_list_ranks.append(off_bench_def_df)
concat_def_list_ranks.append(role_big_def_df)
concat_def_list_ranks.append(role_guard_def_df)
concat_def_list_ranks.append(secondary_def_df)
concat_def_list_ranks.append(vers_forwards_def_df)

concat_def_list_ranks = pd.concat(concat_def_list_ranks)

concat_def_list_ranks = concat_def_list_ranks.sort_index()

concat_def_list_ranks.to_csv('concat_4_def_ranks.csv', index=False, encoding='utf-8')







