import pandas as pd
Blotter=pd.read_csv(r'C:\Users\yuanq\Desktop\Blotter.csv')
his_data = pd.read_csv(r'C:\Users\yuanq\Desktop\his_data.csv')
transaction=pd.read_csv(r'C:\Users\yuanq\Desktop\transaction.csv')

#initial cash=$1000000

transaction['Portofolio_value']=transaction['Close']*transaction['IVV_Position']+transaction['Cash']

ledger=transaction

ledger['Portofolio_return']=ledger['Portofolio_value'].pct_change()

ledger.to_csv('Ledger.csv')

Portofolio_value_1=ledger[['Portofolio_value']]

Portofolio_value_1

Date_Porto=ledger[['Date']]

Portfolio_value_result=pd.DataFrame(columns=['Date','Portfolio_value'])

for i in range(len(ledger)):
    Portfolio_value_result=Portfolio_value_result.append({'Date': ledger.loc[i]['Date'],'Portfolio_': ledger.loc[i]['Portofolio_value']},ignore_index=True)


Portfolio_value_result.to_csv('Portfolio_value_result.csv')


#n=837

#regular_mean=ledger["Portofolio_return"].mean()

#gmrr=ledger.Portofolio_return.astype(object).product()**(1/n)

#vol=ledger['Portofolio_return'].std()

#rf=0.0001

#sharpe_ratio= (regular_mean-rf)/vol