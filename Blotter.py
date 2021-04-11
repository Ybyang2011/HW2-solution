import pandas as pd
blotter = pd.DataFrame(columns = ['dt','symb','actn','size','Price','Type'])
raw = pd.read_csv('action_with_price.csv')
canbuy = True
cost = 0
for i in range(len(raw)):
    if raw['buy_or_sell'][i] == 'buy' and canbuy == True:
        cost -= raw['end_price'][i] * 100
        canbuy = False
        blotter = blotter.append({'dt': raw['end_date'][i], 'symb': 'IVV',
                                          'actn': raw['buy_or_sell'][i], 'size': 100,
                                  'Price': raw['end_price'][i],'Type':'LMT'},ignore_index =True)
    if raw['buy_or_sell'][i] == 'buy' and canbuy == False:
        continue
    if raw['buy_or_sell'][i] == 'sell' and canbuy == True:
        continue
    if raw['buy_or_sell'][i] == 'sell' and canbuy ==False:
        cost += raw['end_price'][i] * 100
        canbuy = True
        blotter = blotter.append({'dt': raw['end_date'][i], 'symb': 'IVV',
                                  'actn': raw['buy_or_sell'][i], 'size': 100,
                                  'Price': raw['end_price'][i], 'Type': 'LMT'}, ignore_index=True)

blotter.to_csv('Blotter.csv')
print(cost)
