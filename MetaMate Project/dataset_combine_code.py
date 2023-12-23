import pandas as pd
lck23_spring = pd.read_csv("LCK23_Spring_comp.csv")
lck23_spring_playoff = pd.read_csv("LCK23_Spring_Playoff_comp.csv")
lck23_summer = pd.read_csv("LCK23_Summer_comp.csv")
lck23_summer_playoff = pd.read_csv("LCK23_Summer_Playoff_comp.csv")
world23_playin = pd.read_csv("World23_Playins_comp.csv")
world23_stage = pd.read_csv("World23_MainEvents_comp.csv")
team_comp = pd.concat([lck23_spring, lck23_spring_playoff,lck23_summer,lck23_summer_playoff,world23_playin,world23_stage], axis=0, ignore_index=True)

team_comp.to_csv(r"C:\Users\Harry Trinh\Documents\GitHub\MetaMate\MetaMate Project\league_team_comp.csv",index=False)

# top = pd.read_csv("top.csv")
# jg = pd.read_csv("jungle.csv")
# mid = pd.read_csv("mid.csv")
# adc = pd.read_csv("adc.csv")
# sup = pd.read_csv("sup.csv")
# all_champ_stat = pd.concat([top, jg,mid,adc,sup], axis=0, ignore_index=True)

# all_champ_stat.to_csv(r"C:\Users\Harry Trinh\Documents\GitHub\MetaMate\MetaMate Project\all_champ_stat.csv",index=False)