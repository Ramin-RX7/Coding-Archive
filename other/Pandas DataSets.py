import pandas as pnd
'''#nba = pnd.read_csv("nba_all_elo.csv")
#pd.set_option("display.max.columns", None)
#pd.set_option("display.precision", 2)
#print(nba.loc[nba['team_id']=='BOS', 'pts'].sum())
#print(list(nba.axes[1]).index('pts'))
#ers = nba[nba["fran_id"].str.endswith("ers")]
#ers= nba[(nba["_iscopy"]==0) & (nba["pts"] > 100) & (nba["opp_pts"] > 100) & (nba["team_id"] == "BLB")]
#print(nba.groupby('fran_id',sort=False)['pts'].sum())
#print(nba[(nba['fran_id']=='Warriors') & (nba['year_id']==2015)].groupby(["game_result"])["game_id"].count())
#nba["difference"] = nba.pts - nba.opp_pts
#nba["game_location"] = pnd.Categorical(nba["game_location"])
#print(nba.info())
#nba["notes"].fillna(value="no notes at all",inplace=True)
##import matplotlib.pyplot as plt
#nba[nba["fran_id"] == "Knicks"].groupby("year_id")["pts"].sum().plot()
#nba["fran_id"].value_counts().head(10).plot(kind="bar")
#nba[(nba["fran_id"] == "Heat") & (nba["year_id"] == 2013)]["game_result"].value_counts().plot(kind="pie")
#plt.show()'''

'''#revenues = pnd.Series([5555, 7000, 1980])
city_revenues = pnd.Series([4200, 8000, 6500],index=["Amsterdam", "Toronto", "Tokyo"])
city_employee_count = pnd.Series({"Amsterdam": 5, "Tokyo": 8})
city_data = pnd.DataFrame({"revenue": city_revenues,"employee_count": city_employee_count})
#print(city_revenues.mean())
further_city_data = pnd.DataFrame(
    {"revenue": [7000, 3400], "employee_count":[2, 2]},
    index=["New York", "Barcelona"])
all_city_data = pnd.concat([city_data, further_city_data], sort=False,axis=0)
city_countries = pnd.DataFrame({
    "country": ["Holland", "Japan", "Holland", "Canada", "Spain"],
    "capital": [1, 1, 0, 0, 0]},
    index=["Amsterdam", "Tokyo", "Rotterdam", "Toronto", "Barcelona"])
countries = pnd.DataFrame({
    "population_millions": [17, 127, 37],
    "continent": ["Europe", "Asia", "North America"]
}, index= ["Holland", "Japan", "Canada"])
cities = pnd.concat([all_city_data, city_countries], axis=1, sort=False,join='inner')
countries = pnd.DataFrame({
    "population_millions": [17, 127, 37],
    "continent": ["Europe", "Asia", "North America"]
}, index= ["Holland", "Japan", "Canada"])
merge= pnd.merge(cities, countries, left_on="country", right_index=True)'''

'''import pandas as pnd
dic= {
    'ramin':{'age':15,'city':'qom'},
    'ali':{'age':16,'book':'HryPtr'},
    'majid':{'major':'humanities','age':17}
      }
cols=('age',) #,index=cols
df = pnd.DataFrame(data=dic,).T#transpose()
#df.to_csv('test')

for df_chunk in pnd.read_csv('test', index_col=0, chunksize=2):
    print(df_chunk, end='\n\n')
'''