import seaborn as sns

tips = sns.load_dataset("tips")
#print(tips)

# head/tail 상위/하위 n개를 가져와라 (default 5개)
tips_h5=tips.head()
tips_h10=tips.head(10)
tips_h10=tips.tail(10)
# print(tips_h5)
# print(tips_h10)

#column, 'total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size'
tips_col = tips.columns
# print(tips_col)

#column 사용법, 그냥 column명을 변수처럼 집어넣으면 된다.
tips_sm = tips.smoker
tips_sm2=tips['smoker'] #문자열의 key값으로 꺼내올때는 있는 그대로인 콜론을 쳐줘야 함
# print(tips_sm)


# tips['tip','day','size']는 불가능
tips_list = tips[['tip','day','size']] #list로 만들어주어야 사용가능
tips_list_h = tips[['tip','day','size']].head() #list로 만들어주어야 사용가능
# print(tips_list)
# print(tips_list_h)


# loc은 index형식으로 찾는 거 아니였나??
# 결과를 보니 실제tuple의 갯수를 0~3까지 보여줌
tips_loc=tips.loc[0:3]
print(tips_loc)
print()

# iloc는 기존에 알던 대로 
tips_iloc=tips.iloc[0:3]
print(tips_iloc)

#결과창을 보면 tuple의 갯수가 다르다는 것을 확인할 수 있음