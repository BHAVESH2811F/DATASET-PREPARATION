#!/usr/bin/env python
# coding: utf-8

# In[68]:


import pandas as pd


# # FINAL TEAM STATS PROCESSING

# In[552]:


## PROCESSING TEAMSTATS OF ALL TEAMS AND MANAGING COLUMNS ##
all_teams_full_name = ["Anaheim Ducks","Ottawa Senators","New Jersey Devils","Vancouver Canucks","Boston Bruins","Edmonton Oilers","Dallas Stars","Florida Panthers","Detroit Red Wings","Nashville Predators","Los Angeles Kings","Pittsburgh Penguins","Minnesota Wild","New York Rangers","Columbus Blue Jackets","Buffalo Sabres","Chicago Blackhawks","Montreal Canadiens","Arizona Coyotes","Philadelphia Flyers","St. Louis Blues","Colorado Avalanche","Calgary Flames","Winnipeg Jets","Carolina Hurricanes","Vegas Golden Knights","San Jose Sharks","Toronto Maple Leafs","Washington Capitals","New York Islanders","Tampa Bay Lightning"]
reg_seas_2018_19_all_team_stats = pd.read_excel(r"C:\NHL DATA\SEASON WISE TEAM STATISTICS\NHL REG SEASON 2018-19 ALL TEAM STATISTICS.xlsx")

# reg_seas_2018_19_all_team_stats.loc[0]
team_stats_column_names = ['Rk','Team','AvAge','GP','W','L','OL','PTS','PTS%','GF','GA','SOW','SOL','SRS','SOS','GF/G','GF/G','PP','PPO','PP%','PPA','PPOA','PK%','SH','SHA','PIM/G','oPIM/G','S','S%','SA','SV%','SO']
reg_seas_2018_19_all_team_stats.drop([0], axis = 0,inplace = True)
reg_seas_2018_19_all_team_stats.columns = team_stats_column_names
reg_seas_2018_19_all_team_stats["Team"] = ['Tampa Bay Lightning','Boston Bruins','Calgary Flames','Washington Capitals','New York Islanders','San Jose Sharks','Toronto Maple Leafs','Pittsburgh Penguins','Nashville Predators','Winnipeg Jets','Carolina Hurricanes','St. Louis Blues','Columbus Blue Jackets','Montreal Canadiens','Vegas Golden Knights', 'Dallas Stars','Colorado Avalanche','Arizona Coyotes','Florida Panthers','Chicago Blackhawks','Minnesota Wild','Philadelphia Flyers','Vancouver Canucks','Anaheim Ducks','Edmonton Oilers','New York Rangers','Buffalo Sabres','Detroit Red Wings','New Jersey Devils','Los Angeles Kings','Ottawa Senators','League Average']
reg_seas_2018_19_all_team_stats.set_index('Team', inplace = True)
reg_seas_2018_19_all_team_stats


# # MATCHUPS OF A RESPECTIVE SEASON

# In[199]:


## READING 2018-19 REG SEASON MATCHUPS
## length of game needs processing  and needs to be converted into minutes ##
reg_seas_2018_19_all_matchups = pd.read_excel(r"C:\NHL DATA\SEASON WISE ALL MATCHUPS\NHL REGULAR SEASON 2018-19 ALL MATCHUPS.xlsx")
reg_seas_2018_19_all_matchups['Total_goal'] = reg_seas_2018_19_all_matchups['G'] + reg_seas_2018_19_all_matchups['G.1']
reg_seas_2018_19_all_matchups.drop(['Unnamed: 5','Notes','G.1','G','LOG'], axis = 1,inplace = True)
reg_seas_2018_19_all_matchups


# # TEAMWISE GOALIES AVERAGE STATS PROCESSING 

# In[559]:


## FOR GOALIES STATS ##
nhl_reg_seas_2018_19_GOALIES_STATS =  pd.read_excel(r"C:\NHL DATA\SEASON WISE GOALIES STATS\NHL REGULAR SEASON 2018-19 GOALIES STATS.xlsx")
all_columns_goalies_stats = ['Rk','Player','Age','Tm','GP','GS','W','L','T/O','GA','SA','SV','SV%','GAA','SO','GPS','MIN','QS','QS%','RBS','GA%','GSAA','G','A','PTS','PIM']
nhl_reg_seas_2018_19_GOALIES_STATS.columns = all_columns_goalies_stats
nhl_reg_seas_2018_19_GOALIES_STATS.drop([0], inplace = True ) ## BEWARE WHILE RUNNING
by_teams_goalies_stats = nhl_reg_seas_2018_19_GOALIES_STATS.groupby('Tm')
nhl_reg_seas_2018_19_GOALIES_STATS.head()
nhl_reg_seas_2018_19_GOALIES_STATS.loc[1]
all_teams_full_name = ["Anaheim Ducks","Ottawa Senators","New Jersey Devils","Vancouver Canucks","Boston Bruins","Edmonton Oilers","Dallas Stars","Florida Panthers","Detroit Red Wings","Nashville Predators","Los Angeles Kings","Pittsburgh Penguins","Minnesota Wild","New York Rangers","Columbus Blue Jackets","Buffalo Sabres","Chicago Blackhawks","Montreal Canadiens","Arizona Coyotes","Philadelphia Flyers","St. Louis Blues","Colorado Avalanche","Calgary Flames","Winnipeg Jets","Carolina Hurricanes","Vegas Golden Knights","San Jose Sharks","Toronto Maple Leafs","Washington Capitals","New York Islanders","Tampa Bay Lightning"]
all_columns_mean_GOALIES_STATS_dataframe =['Rk','Age','GP','GS','W','L','T/O','GA','SA','SV','SV%','GAA','SO','GPS','MIN','QS','QS%','RBS','GA%','GSAA','G','A','PTS','PIM']
all_teams = ["ANA","OTT","NJD","VAN","BOS","EDM","DAL","FLA","DET","NSH","LAK","PIT","MIN","NYR","CBJ","BUF","CHI","MTL","ARI","PHI","STL","COL","CGY","WPG","CAR","VEG","SJS","TOR","WSH","NYI","TBL"]
nhl_reg_seas_2018_19_GOALIES_STATS_mean = pd.DataFrame(columns = all_columns_mean_GOALIES_STATS_dataframe, index = all_teams_full_name)

for i in range(0,31):
    temp_adv = by_teams_goalies_stats.get_group(all_teams[i]).mean()
    average_goalies_stats_of_team = temp_adv.tolist()
    (nhl_reg_seas_2018_19_GOALIES_STATS_mean.loc[all_teams_full_name[i]]) = average_goalies_stats_of_team
nhl_reg_seas_2018_19_GOALIES_STATS_mean.to_csv("C:\\NHL DATA\SEASON WISE AGGREGATED DATA\\2018-19\\REG_SES_2018-19_AVERAGE_GOALIES_STATS.csv")    
nhl_reg_seas_2018_19_GOALIES_STATS_mean


# # ALL TEAMS NAMES

# In[557]:


all_teams_full_name = ["Anaheim Ducks","Ottawa Senators","New Jersey Devils","Vancouver Canucks","Boston Bruins","Edmonton Oilers","Dallas Stars","Florida Panthers","Detroit Red Wings","Nashville Predators","Los Angeles Kings","Pittsburgh Penguins","Minnesota Wild","New York Rangers","Columbus Blue Jackets","Buffalo Sabres","Chicago Blackhawks","Montreal Canadiens","Arizona Coyotes","Philadelphia Flyers","St. Louis Blues","Colorado Avalanche","Calgary Flames","Winnipeg Jets","Carolina Hurricanes","Vegas Golden Knights","San Jose Sharks","Toronto Maple Leafs","Washington Capitals","New York Islanders","Tampa Bay Lightning"]
all_teams = ["ANA","OTT","NJD","VAN","BOS","EDM","DAL","FLA","DET","NSH","LAK","PIT","MIN","NYR","CBJ","BUF","CHI","MTL","ARI","PHI","STL","COL","CGY","WPG","CAR","VEG","SJS","TOR","WSH","NYI","TBL"]
team_full_names_list = ["Anaheim Ducks","Ottawa Senators","New Jersey Devils","Vancouver Canucks","Boston Bruins","Edmonton Oilers","Dallas Stars","Florida Panthers","Detroit Red Wings","Nashville Predators","Los Angeles Kings","Pittsburgh Penguins","Minnesota Wild","New York Rangers","Columbus Blue Jackets","Buffalo Sabres","Chicago Blackhawks","Montreal Canadiens","Arizona Coyotes","Philadelphia Flyers","St. Louis Blues","Colorado Avalanche","Calgary Flames","Winnipeg Jets","Carolina Hurricanes","Vegas Golden Knights","San Jose Sharks","Toronto Maple Leafs","Washington Capitals","New York Islanders","Tampa Bay Lightning"]


# # TEAMWISE NORMAL SKATER  STATS AVERAGE PROCESSING

# In[554]:


## FOR NORMAL SKATER STATS

nhl_reg_seas_2018_19_SKATER_STATS = pd.read_excel(r'C:\NHL DATA\SEASON WISE SKATERS STATS\2018-19  NHL REGULAR SEASON  SKATER STATS.xlsx')
all_columns_skater_stats = ['Rk','Player','Age','Tm','Pos','GP','G','A','PTS','+/-','PIM','PS','EV','PP','SH','GW','Assist-EV','PP','Assist-SH','S','S%','TOI','ATOI','BLK','HIT','FOW','FOL','FO%']
nhl_reg_seas_2018_19_SKATER_STATS.columns = all_columns_skater_stats
nhl_reg_seas_2018_19_SKATER_STATS.drop([0], inplace = True ) ## BEWARE WHILE RUNNING
by_teams = nhl_reg_seas_2018_19_SKATER_STATS.groupby('Tm')
all_teams_full_name = ["Anaheim Ducks","Ottawa Senators","New Jersey Devils","Vancouver Canucks","Boston Bruins","Edmonton Oilers","Dallas Stars","Florida Panthers","Detroit Red Wings","Nashville Predators","Los Angeles Kings","Pittsburgh Penguins","Minnesota Wild","New York Rangers","Columbus Blue Jackets","Buffalo Sabres","Chicago Blackhawks","Montreal Canadiens","Arizona Coyotes","Philadelphia Flyers","St. Louis Blues","Colorado Avalanche","Calgary Flames","Winnipeg Jets","Carolina Hurricanes","Vegas Golden Knights","San Jose Sharks","Toronto Maple Leafs","Washington Capitals","New York Islanders","Tampa Bay Lightning"]
# MAKING MEAN DATAFRAME FOR NORMAL SKATER STATISTICS
## PLEASE NOTE THAT TIME ON ICE and AVERAGE TIME ON ICE STATS HAS BEEN REMOVED, NEED TO BE CONVERTED INTO MINUTES AND THEN ADD IN MEAN TABLE

all_columns_mean_dataframe = ['Rk','Age','GP','G','A','PTS','+/-','PIM','PS','EV','PP','SH','GW','Assist-EV','PP','Assist-SH','S','S%','TOI','BLK','HIT','FOW','FOL','FO%']
all_teams = ["ANA","OTT","NJD","VAN","BOS","EDM","DAL","FLA","DET","NSH","LAK","PIT","MIN","NYR","CBJ","BUF","CHI","MTL","ARI","PHI","STL","COL","CGY","WPG","CAR","VEG","SJS","TOR","WSH","NYI","TBL"]
nhl_reg_seas_2018_19_skaters_stats_mean = pd.DataFrame(columns = all_columns_mean_dataframe, index = all_teams_full_name)
for i in range(0,31):
    temp = by_teams.get_group(all_teams[i]).mean()
    average_of_team = temp.tolist()
    nhl_reg_seas_2018_19_skaters_stats_mean.loc[all_teams_full_name[i]] = average_of_team
    nhl_reg_seas_2018_19_skaters_stats_mean
    
#nhl_reg_seas_2018_19_skaters_stats_mean.to_csv("C:\\NHL DATA\\SEASON WISE AGGREGATED DATA\\2018-19\\REG_SES_2018-19_AVERAGE_NORMAL_SKATER_STATS.csv")      
nhl_reg_seas_2018_19_skaters_stats_mean    


# # TEAMWISE ADVANCED SKATER  STATS AVERAGE PROCESSING

# In[556]:


# FOR ADVANCED SKATER STATS
nhl_reg_seas_2018_19_ADVANCED_SKATER_STATS =  pd.read_excel(r"C:\NHL DATA\SEASON WISE SKATERS ADVANCED STATS\NHL 2018-19 REG SEAS SKATER ADVANCED STATS.xlsx")
nhl_reg_seas_2018_19_ADVANCED_SKATER_STATS.head()
nhl_reg_seas_2018_19_ADVANCED_SKATER_STATS.drop([0], inplace = True )
all_columns_advanced_skater_stats = ['Rk','Player','Age','Tm','Pos','GP',"CF","CA","CF%","CF% rel","FF","FA","FF%","FF rel","oiSH%","oiSV%","PDO","oZS%","dZS%","TOI/60","TOI(EV)","TK","GV","E+/-","SAtt","Thru%"]
nhl_reg_seas_2018_19_ADVANCED_SKATER_STATS.columns = all_columns_advanced_skater_stats
by_teams_advanced_skater_stats = nhl_reg_seas_2018_19_ADVANCED_SKATER_STATS.groupby("Tm")
# nhl_reg_seas_2018_19_ADVANCED_SKATER_STATS["Tm"].value_counts()
# MAKING MEAN DATAFRAME FOR ADVANCED SKATER STATISTICS
#all_columns_mean_advanced_skater_stats_dataframe = ['Rk','Age','GP',"CF","CA","CF%","CF% rel","FF","FA","FF%","FF rel","oiSH%","oiSV%","PDO","oZS%","dZS%","TOI/60","TOI(EV)","TK","GV","E+/-","SAtt","Thru%"]
### "TOI/60","TOI(EV)" Removes because of unit problem, needs to be converted into numeric format.
all_teams = ["ANA","OTT","NJD","VAN","BOS","EDM","DAL","FLA","DET","NSH","LAK","PIT","MIN","NYR","CBJ","BUF","CHI","MTL","ARI","PHI","STL","COL","CGY","WPG","CAR","VEG","SJS","TOR","WSH","NYI","TBL"]
all_columns_mean_advanced_skater_stats_dataframe = ['Rk','Age','GP',"CF","CA","CF%","CF% rel","FF","FA","FF%","FF rel","oiSH%","oiSV%","PDO","oZS%","dZS%","TK","GV","E+/-","SAtt","Thru%"]
nhl_reg_seas_2018_19_ADVANCED_SKATERS_STATS_MEAN = pd.DataFrame(columns = all_columns_mean_advanced_skater_stats_dataframe, index = all_teams_full_name)
for i in range(0,31):
    temp_adv = by_teams_advanced_skater_stats.get_group(all_teams[i]).mean()
    average_of_team = temp_adv.tolist()
    (nhl_reg_seas_2018_19_ADVANCED_SKATERS_STATS_MEAN.loc[all_teams_full_name[i]]) = average_of_team
#len(average_of_team)
#nhl_reg_seas_2018_19_ADVANCED_SKATERS_STATS_MEAN.to_csv("C:\\NHL DATA\\SEASON WISE AGGREGATED DATA\\2018-19\\REG_SES_2018-19_AVERAGE_ADVANCED_SKATER_STATS.csv")
#nhl_reg_seas_2018_19_ADVANCED_SKATERS_STATS_MEAN.loc["Anaheim Ducks"]
nhl_reg_seas_2018_19_ADVANCED_SKATERS_STATS_MEAN


# # IDENTIFIER TO MATCH WITH THE MATCHUP COLUMNS
# 

# In[560]:


## VISITOR SIDE
iterator = list(range(0,len(visitor_matchups_order_list)))
visitor_matchups_order_list = reg_seas_2018_19_all_matchups["Visitor"].tolist()
all_columns_mean_advanced_skater_stats_dataframe = ['Rk','Age','GP',"CF","CA","CF%","CF% rel","FF","FA","FF%","FF rel","oiSH%","oiSV%","PDO","oZS%","dZS%","TK","GV","E+/-","SAtt","Thru%"]
visitorwise_MATCHUPS_arranged_adv_skater_stats = pd.DataFrame(columns = all_columns_mean_advanced_skater_stats_dataframe)
all_columns_mean_dataframe = ['Rk','Age','GP','G','A','PTS','+/-','PIM','PS','EV','PP','SH','GW','Assist-EV','PP','Assist-SH','S','S%','TOI','BLK','HIT','FOW','FOL','FO%']
visitorwise_MATCHUPS_arranged_skater_stats = pd.DataFrame(columns = all_columns_mean_dataframe)
team_stats_column_names = ['Rk','AvAge','GP','W','L','OL','PTS','PTS%','GF','GA','SOW','SOL','SRS','SOS','GF/G','GF/G','PP','PPO','PP%','PPA','PPOA','PK%','SH','SHA','PIM/G','oPIM/G','S','S%','SA','SV%','SO']
visitorwise_MATCHUPS_arranged_teams_stats = pd.DataFrame(columns = team_stats_column_names)
for i in iterator  :
    ##FOR ADVANCED SKATER STATS##
    i_th_row_matchup_wise_adv_skater_stats = nhl_reg_seas_2018_19_ADVANCED_SKATERS_STATS_MEAN.loc[visitor_matchups_order_list[i]]
    visitorwise_MATCHUPS_arranged_adv_skater_stats = visitorwise_MATCHUPS_arranged_adv_skater_stats.append(i_th_row_matchup_wise_adv_skater_stats, ignore_index=True, )
    ##FOR NORMAL SKATER STATS##
    i_th_row_matchup_wise_normal_skater_stats = nhl_reg_seas_2018_19_skaters_stats_mean.loc[visitor_matchups_order_list[i]]
    visitorwise_MATCHUPS_arranged_skater_stats = visitorwise_MATCHUPS_arranged_skater_stats.append(i_th_row_matchup_wise_normal_skater_stats , ignore_index=True) 
    ## FOR FINAL TEAM STATS##
    i_th_row_matchup_wise_team_stats = reg_seas_2018_19_all_team_stats.loc[visitor_matchups_order_list[i]]
    visitorwise_MATCHUPS_arranged_teams_stats = visitorwise_MATCHUPS_arranged_teams_stats.append(i_th_row_matchup_wise_team_stats , ignore_index=True)



# In[565]:


## HOME SIDE
home_side_matchups_order_list = reg_seas_2018_19_all_matchups["Home"].tolist()
iterator = list(range(0,len(home_side_matchups_order_list)))
all_columns_mean_advanced_skater_stats_dataframe = ['Rk','Age','GP',"CF","CA","CF%","CF% rel","FF","FA","FF%","FF rel","oiSH%","oiSV%","PDO","oZS%","dZS%","TK","GV","E+/-","SAtt","Thru%"]
home_side_wise_MATCHUPS_arranged_adv_skater_stats = pd.DataFrame(columns = all_columns_mean_advanced_skater_stats_dataframe)
all_columns_mean_dataframe = ['Rk','Age','GP','G','A','PTS','+/-','PIM','PS','EV','PP','SH','GW','Assist-EV','PP','Assist-SH','S','S%','TOI','BLK','HIT','FOW','FOL','FO%']
home_side_wise_MATCHUPS_arranged_skater_stats = pd.DataFrame(columns = all_columns_mean_dataframe)
team_stats_column_names = ['Rk','AvAge','GP','W','L','OL','PTS','PTS%','GF','GA','SOW','SOL','SRS','SOS','GF/G','GF/G','PP','PPO','PP%','PPA','PPOA','PK%','SH','SHA','PIM/G','oPIM/G','S','S%','SA','SV%','SO']
home_side_wise_MATCHUPS_arranged_teams_stats = pd.DataFrame(columns = team_stats_column_names)
for i in iterator  :
    ##MATCHING FOR ADVANCED SKATER STATS##
    i_th_row_matchup_wise_adv_skater_stats = nhl_reg_seas_2018_19_ADVANCED_SKATERS_STATS_MEAN.loc[home_side_matchups_order_list[i]]
    home_side_wise_MATCHUPS_arranged_adv_skater_stats = home_side_wise_MATCHUPS_arranged_adv_skater_stats.append(i_th_row_matchup_wise_adv_skater_stats, ignore_index=True )
    ##MATCHING FOR NORMAL SKATER STATS##
    i_th_row_matchup_wise_normal_skater_stats = nhl_reg_seas_2018_19_skaters_stats_mean.loc[home_side_matchups_order_list[i]]
    home_side_wise_MATCHUPS_arranged_skater_stats = home_side_wise_MATCHUPS_arranged_skater_stats.append(i_th_row_matchup_wise_normal_skater_stats , ignore_index=True) 
    ##MATCHING FOR FINAL TEAM STATS##
    i_th_row_matchup_wise_team_stats = reg_seas_2018_19_all_team_stats.loc[home_side_matchups_order_list[i]]
    home_side_wise_MATCHUPS_arranged_teams_stats = home_side_wise_MATCHUPS_arranged_teams_stats.append(i_th_row_matchup_wise_team_stats , ignore_index=True)


# In[568]:


home_side_wise_MATCHUPS_arranged_teams_stats


# # TAKING DIFFERENCE BETWEEN STATS OF HOME AND VISITOR (Always performing [VISITOR -- HOME]

# # EXPERIMENTATION WITH EULER AND MANHATTAN DIFFERENCE LEFT

# In[583]:


column_list_for_final_dataframe = list(reg_seas_2018_19_all_matchups.columns) + list(visitorwise_MATCHUPS_arranged_teams_stats.columns) + list(visitorwise_MATCHUPS_arranged_adv_skater_stats.columns) + list(visitorwise_MATCHUPS_arranged_skater_stats.columns)
FINAL_2018_19_MODEL_FEEDING_DATASET_ATTEMPTED_BY_DIFFERENCE = pd.DataFrame(columns = column_list_for_final_dataframe)
matchup_wise_final_difference_skater_ADVANCED_stats = pd.DataFrame(columns = list(visitorwise_MATCHUPS_arranged_adv_skater_stats.columns))
matchup_wise_final_difference_skater_NORMAL_stats = pd.DataFrame(columns = list(visitorwise_MATCHUPS_arranged_skater_stats.columns))
matchup_wise_final_difference_TEAM_stats = pd.DataFrame(columns = list(visitorwise_MATCHUPS_arranged_teams_stats.columns))
matchup_wise_final_difference_skater_ADVANCED_stats = (visitorwise_MATCHUPS_arranged_adv_skater_stats) - (home_side_wise_MATCHUPS_arranged_adv_skater_stats)
matchup_wise_final_difference_skater_NORMAL_stats =  (visitorwise_MATCHUPS_arranged_skater_stats) - (home_side_wise_MATCHUPS_arranged_skater_stats)
matchup_wise_final_difference_TEAM_stats = (visitorwise_MATCHUPS_arranged_teams_stats) - (home_side_wise_MATCHUPS_arranged_teams_stats)
FINAL_2018_19_MODEL_FEEDING_DATASET_ATTEMPTED_BY_DIFFERENCE = pd.concat([reg_seas_2018_19_all_matchups, matchup_wise_final_difference_TEAM_stats, matchup_wise_final_difference_skater_ADVANCED_stats, matchup_wise_final_difference_skater_NORMAL_stats] ,axis = 1)
FINAL_2018_19_MODEL_FEEDING_DATASET_ATTEMPTED_BY_DIFFERENCE.to_csv("C:\\NHL DATA\\FINAL MODEL FEEDING DATASET (V - H) direct difference\\FINAL_2018_19_MODEL_FEEDING_DATASET_ATTEMPTED_BY_DIFFERENCE.csv")


# In[584]:


FINAL_2018_19_MODEL_FEEDING_DATASET_ATTEMPTED_BY_DIFFERENCE.shape


# In[ ]:




