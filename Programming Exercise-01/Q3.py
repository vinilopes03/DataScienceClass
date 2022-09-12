import pandas as pd
import numpy as np


def get_df_anal(df, year):
  new_df=pd.DataFrame()
  #data
  vec_data=[df.loc[t,'COLUMN'].split('\t')[0] for t in range(1, len(df)-6, 6)]
  vec_data.append(df['COLUMN'].values[-5].split('\t')[0])
  new_df['DATE']=vec_data
  #season
  new_df['season']=np.ones((len(new_df), 1), dtype=int)*int(year)
  #opponent
  vec_data=[df.loc[t,'COLUMN'].split('\t')[1].split('Football')[0] for t in range(1, len(df)-6, 6)]
  vec_data.append(df['COLUMN'].values[-5].split('\t')[1].split('Football')[0])
  new_df['opponent']=vec_data
  #homeaway
  vec_data=[df.loc[t,'COLUMN'].split(',')[0] for t in range(3, len(df)-6, 6)]
  vec_data.append(df['COLUMN'].values[-3].split(',')[0])
  for i in range(len(vec_data)):
    if vec_data[i]=='Notre Dame Stadium':
      vec_data[i]='Home'
    else:
      vec_data[i]='Away'    
  new_df['homeaway']=vec_data
  #gametime
  vec_data=[df.loc[t,'COLUMN'] for t in range(4, len(df)-6, 6)]
  vec_data.append(df['COLUMN'].values[-2].split(',')[0])
  new_df['gametime']=vec_data

  #winlose
  vec_data=[df.loc[t,'COLUMN'].split('\t')[-1].split(' ')[0] for t in range(5, len(df)-6, 6)]
  vec_data.append(df['COLUMN'].values[-1].split('\t')[-1].split(' ')[0])
  new_df['winlose']=vec_data

  #ndscore (a ,1 ) opponetscore(b, 2)
  vec_dataA=[df.loc[t,'COLUMN'].split('\t')[-1].split(' ')[1].split('-')[0] for t in range(5, len(df)-6, 6)]
  vec_dataA.append(df['COLUMN'].values[-1].split('\t')[-1].split(' ')[1].split('-')[0])
  vec_dataB=[df.loc[t,'COLUMN'].split('\t')[-1].split(' ')[1].split('-')[1].split('(')[0] for t in range(5, len(df)-6, 6)]
  vec_dataB.append(df['COLUMN'].values[-1].split('\t')[-1].split(' ')[1].split('-')[1])
  vec_data1=[]
  vec_data2=[]

  for i in range(len(new_df)):
    if new_df.loc[i,'homeaway']=='Home':
      vec_data1.append(vec_dataA[i])
      vec_data2.append(vec_dataB[i])
    else:
      vec_data1.append(vec_dataB[i])
      vec_data2.append(vec_dataA[i])

  new_df['ndscore']=vec_data1
  new_df['opponetscore']=vec_data2

  #plusminus
  new_df['plusminus']= np.array(vec_data1, dtype=int)-np.array(vec_data2, dtype=int)

  #tvchannel
  vec_data=[df.loc[t,'COLUMN'].split('\t')[0].split(' ')[0] for t in range(5, len(df)-6, 6)]
  vec_data.append(df['COLUMN'].values[-1].split('\t')[0].split(' ')[0])
  for i in range(len(vec_data)):
    if len(vec_data[i])==1:
      vec_data[i]= 'UNK'
  new_df['tvchannel']=vec_data

  return new_df



df=pd.DataFrame()
df['COLUMN']=pd.DataFrame(pd.read_csv('C:/Users/Vinicius/Desktop/datasets/fbschedules_raw/fbschedules2022.txt', sep='=').values)
year=2008
get_df_anal(df, year)


