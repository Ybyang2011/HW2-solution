import pandas as pd

msci_df = pd.read_csv('MSCI_data_2.csv')
msci_df['Date'] = pd.to_datetime(msci_df['Date'],format ='%m/%d/%Y')
df_result = pd.DataFrame(columns = ['start_date','end_date','buy_or_sell'])

#This part add normal period first, that is at the end of the period, we sell the Index for profit
for index1, row1 in msci_df.iterrows():
    for index2, row2 in msci_df.iterrows():
        if index2 > index1 and (row2['Date'] - row1['Date']).days >= 7 and (
                row2['Health_care'] - row1['Health_care']) < 0 and (
                row2['Energy'] - row1['Energy']) < 0 and (
                row2['Utilities'] - row1['Utilities']) < 0 and (
                row2['Real_estate'] - row1['Real_estate']) > 0 and (
                row2['Consumer_Discretionary'] - row1['Consumer_Discretionary']) > 0 and (
                row2['Information_techology'] - row1['Information_techology']) > 0 and (
                row2['Industrials'] - row1['Industrials']) > 0:
            df_result = df_result.append({'start_date': row1['Date'], 'end_date': row2['Date'],
                                          'buy_or_sell':'sell'},ignore_index =True)

df_result.drop_duplicates(subset=['end_date'])
idx1 = df_result.groupby(['start_date'],sort=False)['end_date'].transform(max)==df_result['end_date']
df_result=df_result[idx1]
df_result['start_date'] =pd.to_datetime(df_result['start_date'])
df_result['end_date']=pd.to_datetime(df_result['end_date'])
df_result.reset_index(drop = True)


df_to_merge_normal = pd.DataFrame(columns = ['start_date','end_date','buy_or_sell'])
for i in range(len(df_result) -1):
    if (df_result.iloc[i+1]['start_date'] - df_result.iloc[i]['end_date']).days > 0:
        df_to_merge_normal = df_to_merge_normal.append({'start_date':df_result.iloc[i]['start_date'],'end_date':df_result.iloc[i]['end_date'],
                            'buy_or_sell':df_result.iloc[i]['buy_or_sell']},ignore_index=True)

df_result1 = pd.DataFrame(columns = ['start_date','end_date','buy_or_sell'])
for index1, row1 in msci_df.iterrows():
    for index2, row2 in msci_df.iterrows():
        if index2>index1 and (row2['Date']-row1['Date']).days>=7 and (
                row2['Health_care']-row1['Health_care'])>0 and (
                row2['Energy']-row1['Energy'])>0 and (
                row2['Utilities']-row1['Utilities'])>0 and (
                row2['Real_estate']-row1['Real_estate'])<0 and (
                row2['Consumer_Discretionary']-row1['Consumer_Discretionary'])<0 and (
                row2['Information_techology']-row1['Information_techology'])<0 and (
                row2['Industrials']-row1['Industrials'])<0 :
            df_result1= df_result1.append({'start_date': row1['Date'],'end_date': row2['Date'],
                                         'buy_or_sell':'buy'},ignore_index=True)

df_result1.drop_duplicates(inplace=True)
idx = df_result1.groupby(['start_date'],sort=False)['end_date'].transform(max)==df_result1['end_date']
df_result1=df_result1[idx]
df_result1['start_date'] =pd.to_datetime(df_result1['start_date'])
df_result1['end_date']=pd.to_datetime(df_result1['end_date'])
df_result1.reset_index(drop = True)

df_to_merge_recession = pd.DataFrame(columns = ['start_date','end_date','buy_or_sell'])
for i in range(len(df_result1) -1):
    if (df_result1.iloc[i+1]['start_date'] - df_result1.iloc[i]['end_date']).days > 0:
        df_to_merge_recession = df_to_merge_recession.append({'start_date':df_result1.iloc[i]['start_date'],'end_date':df_result1.iloc[i]['end_date'],
                            'buy_or_sell':df_result1.iloc[i]['buy_or_sell']},ignore_index=True)

df_merge = pd.concat([df_to_merge_normal,df_to_merge_recession],axis = 0, ignore_index=True,sort = True)
df_merge = df_merge.sort_values(by="start_date")
df_merge.to_csv("action.csv",index=None)