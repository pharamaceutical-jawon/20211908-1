import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
train = pd.read_csv('train_csv')
test = pd.read_csv('test_csv')
test['Transported'] = None
df = pd.concat([train, test], ignore_index=True)
print("전체 데이터 수:", len(df))
bins = [0,10,20,30,40,50,60,70,80]
labels = ['0s','10s','20s','30s','40s','50s','60s','70s']

df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)

age_transport = df.groupby(['AgeGroup', 'Transported']).size().unstack()

age_transport.plot(kind='bar')

plt.title('Transported by Age Group')
plt.show()
import pandas as pd
print(pd.__version__)
