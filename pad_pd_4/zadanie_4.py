import pandas as pd
import numpy as np
from datetime import datetime, timedelta

doctor_df = pd.read_csv("./Zadanie_4.csv", sep=";")
def accumulator(x,y):
  if type(x) is not tuple:
    x = (x,x)
  
  if datetime.strptime(y, '%d.%m.%Y %H:%M') - datetime.strptime(x[1], '%d.%m.%Y %H:%M') == timedelta(seconds=60):
    return (x[0],y)
  else:
    return (y,y)

f = np.frompyfunc(accumulator, 2, 1)
doctor_df['SlotID'] = f.accumulate(doctor_df['DateTime']).apply(lambda x: x[0] if type(x) is tuple else x).apply(lambda x: datetime.strptime(x, '%d.%m.%Y %H:%M').timestamp())
slots_df = doctor_df[['DoctorID', 'DateTime', 'Type', 'City', 'SlotID']].groupby(['DoctorID', 'City', 'Type', 'SlotID']).agg(datetime_start=('DateTime', 'min'), datetime_end=('DateTime', 'max'))
slots_df.to_csv('Doctor_slots.csv', sep=';')