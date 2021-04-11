import pandas as pd

msci_df = pd.read_csv('MSCI_data_2.csv')

msci_df['Date'] =pd.to_datetime(msci_df['Date'], format='%m/%d/%Y')
#check days
(msci_df.loc[2]['Date']-msci_df.loc[0]['Date']).days

# Find normal period when "group_1 goes up and group_2 goes down".
# The period should be a long cycle. Therefore, I set the length between the start date to the end date is not less than 7.

df_result_2=pd.DataFrame(columns=['start_date','end_date'])

for index1, row1 in msci_df.iterrows():
    for index2, row2 in msci_df.iterrows():
        if index2>index1 and (row2['Date']-row1['Date']).days>=7 and (row2['Health_care']-row1['Health_care'])<0 and (row2['Energy']-row1['Energy'])<0 and (row2['Utilities']-row1['Utilities'])<0 and (row2['Real_estate']-row1['Real_estate'])>0 and (row2['Consumer_Discretionary']-row1['Consumer_Discretionary'])>0 and  (row2['Information_techology']-row1['Information_techology'])>0 and (row2['Industrials']-row1['Industrials'])>0 :
            #if ((df_result_2['end_date'].end() - row1['Date']).days()):
            df_result_2=df_result_2.append({'start_date': row1['Date'],'end_date': row2['Date']},ignore_index=True)

df_result_2.drop_duplicates(inplace=True)
idx1 = df_result_2.groupby(['start_date'],sort=False)['end_date'].transform(max)==df_result_2['end_date']
df1_result_2=df_result_2[idx1]

df1_result_2.to_csv("MSCI_normal_periods.csv",index=None)

# Find recession or late period when "group_2 goes up and group_1 goes down".
# The period should be a long cycle. Therefore, I set the length between the start date to the end date is not less than 7.
df_result_3=pd.DataFrame(columns=['start_date','end_date'])

for index1, row1 in msci_df.iterrows():
    for index2, row2 in msci_df.iterrows():
        if index2>index1 and (row2['Date']-row1['Date']).days>=7 and (row2['Health_care']-row1['Health_care'])>0 and (row2['Energy']-row1['Energy'])>0 and (row2['Utilities']-row1['Utilities'])>0 and (row2['Real_estate']-row1['Real_estate'])<0 and (row2['Consumer_Discretionary']-row1['Consumer_Discretionary'])<0 and  (row2['Information_techology']-row1['Information_techology'])<0 and (row2['Industrials']-row1['Industrials'])<0 :
            df_result_3=df_result_3.append({'start_date': row1['Date'],'end_date': row2['Date']},ignore_index=True)

df_result_3.drop_duplicates(inplace=True)
idx = df_result_3.groupby(['start_date'],sort=False)['end_date'].transform(max)==df_result_3['end_date']
df1_result_3=df_result_3[idx]
df1_result_3.to_csv("MSCI_recession_periods.csv",index=None)

