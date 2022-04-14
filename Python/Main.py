import pandas as pd
import numpy as np
import featuretools as ft

clients = pd.read_csv('data/clients.csv')
es = ft.EntitySet(id='clients')

es = es.entity_from_dataframe(entity_id='clients', dataframe=clients, index='client_id', time_index='joined')

payments = pd.read_csv('data/payments.csv')

es = es.entity_from_dataframe(entity_id='payments', dataframe=payments, variable_types={'missed':ft.variable_types.Categorical}, 
        make_index=True, index='payment_id', time_index='payment_date')

loans = pd.read_csv('data/loans.csv')

print(loans.head(5))

es = es.entity_from_dataframe(entity_id='loans', dataframe=loans, index='loan_id', time_index='loan_start')

# Group loans by client id and calculate mean, max, min of loans
stats = loans.groupby(['client_id'])['loan_amount'].agg(['mean','max','min'])

# Merge with the clients dataframe
stats = clients.merge(stats, left_on='client_id', right_index=True)

relation = ft.Relationship(es['clients']['client_id'], es['loans']['client_id'])
es = es.add_relationship(relation)

print(es)

features, feature_names = ft.dfs(entityset = es, target_entity = 'clients', agg_primitives = ['mean','max','min'], trans_primitives=['year','month'])

print(features)

print(feature_names)

a = np.eye(4)
print(a)

