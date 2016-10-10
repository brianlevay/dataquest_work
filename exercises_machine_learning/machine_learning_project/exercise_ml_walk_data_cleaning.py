## 3. Reading in to Pandas ##

import pandas as pd

loans_2007 = pd.read_csv("loans_2007.csv")
print(loans_2007.head(1))
print(len(loans_2007.columns))

## 4. First group of columns ##

to_drop = ['id','member_id','funded_amnt','funded_amnt_inv','grade','sub_grade','emp_title','issue_d']
loans_2007.drop(to_drop,axis=1,inplace=True)

## 5. Second group of features ##

to_drop = ['zip_code','out_prncp','out_prncp_inv','total_pymnt','total_pymnt_inv','total_rec_prncp']
loans_2007.drop(to_drop,axis=1,inplace=True)

## 6. Third group of features ##

to_drop = ['total_rec_int','total_rec_late_fee','recoveries',\
           'collection_recovery_fee','last_pymnt_d','last_pymnt_amnt']
loans_2007.drop(to_drop,axis=1,inplace=True)

print(loans_2007.head(1))
print(len(loans_2007.columns))

## 7. Target column ##

loan_status_cts = loans_2007['loan_status'].value_counts()
print(loan_status_cts)

## 8. Binary classification ##

to_keep = (loans_2007['loan_status'] == "Fully Paid") | (loans_2007['loan_status'] == "Charged Off")
loans_2007 = loans_2007.loc[to_keep]

replace_dict = {'loan_status': {"Fully Paid": 1, "Charged Off": 0}}
loans_2007 = loans_2007.replace(replace_dict)

## 9. Removing single value columns ##

drop_columns = []

for col in loans_2007:
    non_null = loans_2007[col].dropna()
    unique_non_null = non_null.unique()
    num_true_unique = len(unique_non_null)
    if num_true_unique == 1:
        drop_columns.append(col)

loans_2007.drop(drop_columns,axis=1,inplace=True)
print(drop_columns)