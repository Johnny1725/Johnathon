import pandas as pd

import matplotlib.pyplot as plt

 

df2014 = pd.read_excel('2014.xlsx')

df2015 = pd.read_excel('2015.xlsx')

df2016 = pd.read_excel('2016.xlsx')

df2017 = pd.read_excel('2017.xlsx')

df2018 = pd.read_excel('2018.xlsx')

 

pd.set_option('display.max_columns',999)

pd.set_option('display.width',1200)

 

fig, moneys = plt.subplots(3,2)

 

dfm2014 = df2014.loc[df2014['OCC_TITLE'] == 'Mechanical Engineers']

dfm2015 = df2015.loc[df2015['OCC_TITLE'] == 'Mechanical Engineers']

dfm2016 = df2016.loc[df2016['OCC_TITLE'] == 'Mechanical Engineers']

dfm2017 = df2017.loc[df2017['OCC_TITLE'] == 'Mechanical Engineers']

dfm2018 = df2018.loc[df2018['OCC_TITLE'] == 'Mechanical Engineers']

 

x=[2014,2015,2016,2017,2018]

ymechann10th=[]

ymechann10th.append(dfm2014.loc[194,['A_PCT10']])

ymechann10th.append(dfm2015.loc[194,['A_PCT10']])

ymechann10th.append(dfm2016.loc[194,['A_PCT10']])

ymechann10th.append(dfm2017.loc[191,['A_PCT10']])

ymechann10th.append(dfm2018.loc[191,['A_PCT10']])

 

ymechannmed=[]

ymechannmed.append(dfm2014.loc[194,['A_MEDIAN']])

ymechannmed.append(dfm2015.loc[194,['A_MEDIAN']])

ymechannmed.append(dfm2016.loc[194,['A_MEDIAN']])

ymechannmed.append(dfm2017.loc[191,['A_MEDIAN']])

ymechannmed.append(dfm2018.loc[191,['A_MEDIAN']])

 

ymechann90th=[]

ymechann90th.append(dfm2014.loc[194,['A_PCT90']])

ymechann90th.append(dfm2015.loc[194,['A_PCT90']])

ymechann90th.append(dfm2016.loc[194,['A_PCT90']])

ymechann90th.append(dfm2017.loc[191,['A_PCT90']])

ymechann90th.append(dfm2018.loc[191,['A_PCT90']])

 

moneys[2,1].plot(x,ymechann10th,label='10th Percentile',color='blue')

moneys[2,1].set_ylabel('Annual Salary ($)')

moneys[2,1].set_xlabel('Year')

moneys[2,1].set_title('Annual Salary for Mechanical Engineering')

moneys[2,1].plot(x,ymechannmed,label='Median',color='orange')

moneys[2,1].plot(x,ymechann90th,label='90th Percentile',color='green')

moneys[2,1].legend(loc=2)

 

 

 

dfbe2014 = df2014.loc[df2014['OCC_TITLE'] == 'Biomedical Engineers']

dfbe2015 = df2015.loc[df2015['OCC_TITLE'] == 'Biomedical Engineers']

dfbe2016 = df2016.loc[df2016['OCC_TITLE'] == 'Biomedical Engineers']

dfbe2017 = df2017.loc[df2017['OCC_TITLE'] == 'Biomedical Engineers']

dfbe2018 = df2018.loc[df2018['OCC_TITLE'] == 'Biomedical Engineers']

 

ybe10th=[]

ybe10th.append(dfbe2014.loc[174,['A_PCT10']])

ybe10th.append(dfbe2015.loc[174,['A_PCT10']])

ybe10th.append(dfbe2016.loc[174,['A_PCT10']])

ybe10th.append(dfbe2017.loc[171,['A_PCT10']])

ybe10th.append(dfbe2018.loc[171,['A_PCT10']])

 

ybemed=[]

ybemed.append(dfbe2014.loc[174,['A_MEDIAN']])

ybemed.append(dfbe2015.loc[174,['A_MEDIAN']])

ybemed.append(dfbe2016.loc[174,['A_MEDIAN']])

ybemed.append(dfbe2017.loc[171,['A_MEDIAN']])

ybemed.append(dfbe2018.loc[171,['A_MEDIAN']])

 

ybe90th=[]

ybe90th.append(dfbe2014.loc[174,['A_PCT90']])

ybe90th.append(dfbe2015.loc[174,['A_PCT90']])

ybe90th.append(dfbe2016.loc[174,['A_PCT90']])

ybe90th.append(dfbe2017.loc[171,['A_PCT90']])

ybe90th.append(dfbe2018.loc[171,['A_PCT90']])

 

moneys[0,0].plot(x,ybe10th,label='10th Percentile',color='blue')

moneys[0,0].set_ylabel('Annual Salary ($)')

moneys[0,0].set_xlabel('Year')

moneys[0,0].set_title('Annual Salary for Biomedical Engineering')

moneys[0,0].plot(x,ybemed,label='Median',color='orange')

moneys[0,0].plot(x,ybe90th,label='90th Percentile',color='green')

moneys[0,0].legend(loc=2)

 

 

 

dfce2014 = df2014.loc[df2014['OCC_TITLE'] == 'Chemical Engineers']

dfce2015 = df2015.loc[df2015['OCC_TITLE'] == 'Chemical Engineers']

dfce2016 = df2016.loc[df2016['OCC_TITLE'] == 'Chemical Engineers']

dfce2017 = df2017.loc[df2017['OCC_TITLE'] == 'Chemical Engineers']

dfce2018 = df2018.loc[df2018['OCC_TITLE'] == 'Chemical Engineers']

 

yce10th=[]

yce10th.append(dfce2014.loc[176,['A_PCT10']])

yce10th.append(dfce2015.loc[176,['A_PCT10']])

yce10th.append(dfce2016.loc[176,['A_PCT10']])

yce10th.append(dfce2017.loc[173,['A_PCT10']])

yce10th.append(dfce2018.loc[173,['A_PCT10']])

 

ycemed=[]

ycemed.append(dfce2014.loc[176,['A_MEDIAN']])

ycemed.append(dfce2015.loc[176,['A_MEDIAN']])

ycemed.append(dfce2016.loc[176,['A_MEDIAN']])

ycemed.append(dfce2017.loc[173,['A_MEDIAN']])

ycemed.append(dfce2018.loc[173,['A_MEDIAN']])

 

yce90th=[]

yce90th.append(dfce2014.loc[176,['A_PCT90']])

yce90th.append(dfce2015.loc[176,['A_PCT90']])

yce90th.append(dfce2016.loc[176,['A_PCT90']])

yce90th.append(dfce2017.loc[173,['A_PCT90']])

yce90th.append(dfce2018.loc[173,['A_PCT90']])

 

moneys[0,1].plot(x,yce10th,label='10th Percentile',color='blue')

moneys[0,1].set_ylabel('Annual Salary ($)')

moneys[0,1].set_xlabel('Year')

moneys[0,1].set_title('Annual Salary for Biomedical Engineering')

moneys[0,1].plot(x,ycemed,label='Median',color='orange')

moneys[0,1].plot(x,yce90th,label='90th Percentile',color='green')

moneys[0,1].legend(loc=2)

 

 

 

dfciv2014 = df2014.loc[df2014['OCC_TITLE'] == 'Civil Engineers']

dfciv2015 = df2015.loc[df2015['OCC_TITLE'] == 'Civil Engineers']

dfciv2016 = df2016.loc[df2016['OCC_TITLE'] == 'Civil Engineers']

dfciv2017 = df2017.loc[df2017['OCC_TITLE'] == 'Civil Engineers']

dfciv2018 = df2018.loc[df2018['OCC_TITLE'] == 'Civil Engineers']

 

yciv10th=[]

yciv10th.append(dfciv2014.loc[178,['A_PCT10']])

yciv10th.append(dfciv2015.loc[178,['A_PCT10']])

yciv10th.append(dfciv2016.loc[178,['A_PCT10']])

yciv10th.append(dfciv2017.loc[175,['A_PCT10']])

yciv10th.append(dfciv2018.loc[175,['A_PCT10']])

 

ycivmed=[]

ycivmed.append(dfciv2014.loc[178,['A_MEDIAN']])

ycivmed.append(dfciv2015.loc[178,['A_MEDIAN']])

ycivmed.append(dfciv2016.loc[178,['A_MEDIAN']])

ycivmed.append(dfciv2017.loc[175,['A_MEDIAN']])

ycivmed.append(dfciv2018.loc[175,['A_MEDIAN']])

 

yciv90th=[]

yciv90th.append(dfciv2014.loc[178,['A_PCT90']])

yciv90th.append(dfciv2015.loc[178,['A_PCT90']])

yciv90th.append(dfciv2016.loc[178,['A_PCT90']])

yciv90th.append(dfciv2017.loc[175,['A_PCT90']])

yciv90th.append(dfciv2018.loc[175,['A_PCT90']])

 

moneys[1,0].plot(x,yciv10th,label='10th Percentile',color='blue')

moneys[1,0].set_ylabel('Annual Salary ($)')

moneys[1,0].set_xlabel('Year')

moneys[1,0].set_title('Annual Salary for Civil Engineering')

moneys[1,0].plot(x,ycivmed,label='Median',color='orange')

moneys[1,0].plot(x,yciv90th,label='90th Percentile',color='green')

moneys[1,0].legend(loc=2)

 

 

 

dfelec2014 = df2014.loc[df2014['OCC_TITLE'] == 'Electrical Engineers']

dfelec2015 = df2015.loc[df2015['OCC_TITLE'] == 'Electrical Engineers']

dfelec2016 = df2016.loc[df2016['OCC_TITLE'] == 'Electrical Engineers']

dfelec2017 = df2017.loc[df2017['OCC_TITLE'] == 'Electrical Engineers']

dfelec2018 = df2018.loc[df2018['OCC_TITLE'] == 'Electrical Engineers']

 

yelec10th=[]

yelec10th.append(dfelec2014.loc[183,['A_PCT10']])

yelec10th.append(dfelec2015.loc[183,['A_PCT10']])

yelec10th.append(dfelec2016.loc[183,['A_PCT10']])

yelec10th.append(dfelec2017.loc[180,['A_PCT10']])

yelec10th.append(dfelec2018.loc[180,['A_PCT10']])

 

yelecmed=[]

yelecmed.append(dfelec2014.loc[183,['A_MEDIAN']])

yelecmed.append(dfelec2015.loc[183,['A_MEDIAN']])

yelecmed.append(dfelec2016.loc[183,['A_MEDIAN']])

yelecmed.append(dfelec2017.loc[180,['A_MEDIAN']])

yelecmed.append(dfelec2018.loc[180,['A_MEDIAN']])

 

yelec90th=[]

yelec90th.append(dfelec2014.loc[183,['A_PCT90']])

yelec90th.append(dfelec2015.loc[183,['A_PCT90']])

yelec90th.append(dfelec2016.loc[183,['A_PCT90']])

yelec90th.append(dfelec2017.loc[180,['A_PCT90']])

yelec90th.append(dfelec2018.loc[180,['A_PCT90']])

 

moneys[1,1].plot(x,yelec10th,label='10th Percentile',color='blue')

moneys[1,1].set_ylabel('Annual Salary ($)')

moneys[1,1].set_xlabel('Year')

moneys[1,1].set_title('Annual Salary for Electrical Engineering')

moneys[1,1].plot(x,yelecmed,label='Median',color='orange')

moneys[1,1].plot(x,yelec90th,label='90th Percentile',color='green')

moneys[1,1].legend(loc=2)

 

 

 

dfindus2014 = df2014.loc[df2014['OCC_TITLE'] == 'Industrial Engineers']

dfindus2015 = df2015.loc[df2015['OCC_TITLE'] == 'Industrial Engineers']

dfindus2016 = df2016.loc[df2016['OCC_TITLE'] == 'Industrial Engineers']

dfindus2017 = df2017.loc[df2017['OCC_TITLE'] == 'Industrial Engineers']

dfindus2018 = df2018.loc[df2018['OCC_TITLE'] == 'Industrial Engineers']

 

yindus10th=[]

yindus10th.append(dfindus2014.loc[189,['A_PCT10']])

yindus10th.append(dfindus2015.loc[189,['A_PCT10']])

yindus10th.append(dfindus2016.loc[189,['A_PCT10']])

yindus10th.append(dfindus2017.loc[186,['A_PCT10']])

yindus10th.append(dfindus2018.loc[186,['A_PCT10']])

 

yindusmed=[]

yindusmed.append(dfindus2014.loc[189,['A_MEDIAN']])

yindusmed.append(dfindus2015.loc[189,['A_MEDIAN']])

yindusmed.append(dfindus2016.loc[189,['A_MEDIAN']])

yindusmed.append(dfindus2017.loc[186,['A_MEDIAN']])

yindusmed.append(dfindus2018.loc[186,['A_MEDIAN']])

 

yindus90th=[]

yindus90th.append(dfindus2014.loc[189,['A_PCT90']])

yindus90th.append(dfindus2015.loc[189,['A_PCT90']])

yindus90th.append(dfindus2016.loc[189,['A_PCT90']])

yindus90th.append(dfindus2017.loc[186,['A_PCT90']])

yindus90th.append(dfindus2018.loc[186,['A_PCT90']])

 

moneys[2,0].plot(x,yindus10th,label='10th Percentile',color='blue')

moneys[2,0].set_ylabel('Annual Salary ($)')

moneys[2,0].set_xlabel('Year')

moneys[2,0].set_title('Annual Salary for Industrial Engineering')

moneys[2,0].plot(x,yindusmed,label='Median',color='orange')

moneys[2,0].plot(x,yindus90th,label='90th Percentile',color='green')

moneys[2,0].legend(loc=2)

 

 

plt.tight_layout()

plt.show()