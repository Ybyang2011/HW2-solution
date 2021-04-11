import pandas as pd
df_result = pd.read_csv('MSCI_normal_periods.csv')
df_result.drop_duplicates(subset=['end_date'])
idx1 = df_result.groupby(['start_date'],sort=False)['end_date'].transform(max)==df_result['end_date']
df_result=df_result[idx1]
df_result['start_date'] =pd.to_datetime(df_result['start_date'])
df_result['end_date']=pd.to_datetime(df_result['end_date'])
df_result.reset_index(drop = True)
#print(df_result)

df_to_merge_normal = pd.DataFrame(columns = ['start_date','end_date'])
end = df_result.iloc[0]['end_date']

for i in range(len(df_result) -1):
    if (df_result.iloc[i+1]['start_date'] - df_result.iloc[i]['end_date']).days > 0:
        df_to_merge_normal = df_to_merge_normal.append({'start_date':df_result.iloc[i+1]['start_date'],
                                   'end_date':df_result.iloc[i+1]['end_date']},ignore_index=True)

print(df_to_merge_normal)