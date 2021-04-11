import pandas as pd

normal_df = pd.read_csv(r'C:\Users\yuanq\Desktop\MSCI_normal_periods1.csv')

normal_df['start_date'] =pd.to_datetime(normal_df['start_date'])
normal_df['end_date']=pd.to_datetime(normal_df['end_date'])

result_normal=pd.DataFrame(columns=['start_date','end_date'])

for i in range(len(normal_df)-1):
   if (normal_df.loc[i+1]['start_date']-normal_df.loc[i]['end_date']).days>0:
       result_normal=result_normal.append({'start_date':normal_df.loc[i]['start_date'],'end_date':normal_df.loc[i]['end_date']},ignore_index=True)

recession_df = pd.read_csv(r'C:\Users\yuanq\Desktop\MSCI_recession_periods1.csv')

recession_df['start_date'] =pd.to_datetime(recession_df['start_date'])
recession_df['end_date']=pd.to_datetime(recession_df['end_date'])

result_recession=pd.DataFrame(columns=['start_date','end_date'])

for i in range(len(recession_df)-1):
   if ( recession_df.loc[i+1]['start_date']-recession_df.loc[i]['end_date']).days>0:
       result_recession = result_recession.append({'start_date':recession_df.loc[i]['start_date'],'end_date':recession_df.loc[i]['end_date']},ignore_index=True)


### sell at one day after the end date of the normal session
### First buy occurs after the first recession
result_normal_1=pd.DataFrame(columns=['start_date','end_date','buy_or_sell'])

for i in range(len(normal_df)-1):
   if (normal_df.loc[i+1]['start_date']-normal_df.loc[i]['end_date']).days>0:
       result_normal_1=result_normal_1.append({'start_date':normal_df.loc[i]['start_date'],'end_date':normal_df.loc[i]['end_date'],'buy_or_sell':'Sell'},ignore_index=True)


result_recession_1=pd.DataFrame(columns=['start_date','end_date','buy_or_sell'])

for i in range(len(recession_df)-1):
   if ( recession_df.loc[i+1]['start_date']-recession_df.loc[i]['end_date']).days>0:
       result_recession_1 = result_recession_1.append({'start_date':recession_df.loc[i]['start_date'],'end_date':recession_df.loc[i]['end_date'],'buy_or_sell':'Buy'},ignore_index=True)


df_bound_by_row = pd.concat([result_normal_1, result_recession_1], axis = 0, ignore_index=True)
### sort data by start_date:
df_startdate=df_bound_by_row.sort_values(by="start_date",ignore_index=True)



