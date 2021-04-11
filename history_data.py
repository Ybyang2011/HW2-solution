from datetime import datetime
from Helper import *

action = pd.read_csv("action.csv")
action['start_price'] = 0.0
action['end_price'] = 0.0
for i in range(len(action) -1):
    price_df = fetch_GSPC_data(action['start_date'][i],action['end_date'][i])
    action['end_price'][i] = price_df['Close*'][0]
    action['start_price'][i] = price_df['Close*'][len(price_df) -1]

price_df = fetch_GSPC_data(action['start_date'][len(action) -1 ],action['end_date'][len(action) -1 ])
action['end_price'][len(action) -1 ] = price_df['Close*'][0]
action['start_price'][len(action) -1 ] = price_df['Close*'][len(price_df) -1]
action.to_csv('action_with_price.csv')