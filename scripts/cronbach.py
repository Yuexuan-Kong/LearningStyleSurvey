import pingouin as pg
import pandas as pd
import pyreadstat
from read_data import read_data

df_ch, meta_ch = pyreadstat.read_sav('../data/chinese.sav')
df_fr, meta_fr = pyreadstat.read_sav('../data/france.sav')
df = pd.concat([df_fr, df_ch])
# df = df.drop(df[df.totalseconds.astype(int) < 150].index)
# df = df.drop(df[df.totalseconds.astype(int) > 1450].index)
# df = df.replace(4, 5)
# df = df.replace(2, 1)

Dim = {
       "Act_Ref":['Q4', 'Q10', 'Q16', 'Q22', 'Q28', 'Q34', 'Q40'],
       "Sen_Int":['Q5', 'Q11', 'Q17', 'Q23', 'Q29', 'Q35', 'Q41'],
       "Vis_Ver":['Q6', 'Q12', 'Q18', 'Q24', 'Q30', 'Q36', 'Q42'],
       "Seq_Glo":['Q7', 'Q13', 'Q19', 'Q25', 'Q31', 'Q37', 'Q43'],
       "Ded_Ind":['Q8', 'Q14', 'Q20', 'Q26', 'Q32', 'Q38', 'Q44'],
       "Lea_Per":['Q9', 'Q15', 'Q21', 'Q27', 'Q33', 'Q39', 'Q45'],
}

for t in range(100,420,5):
       alpha = []
       for dim in Dim.items():
              df_reduce = df.drop(df[df.totalseconds.astype(int) < t].index)
              test = df_reduce.loc[:, dim[1]]
              a = pg.cronbach_alpha(data=test)
              alpha.append(a[0])
       # if min(alpha)>=0.5:
       print(t, min(alpha))

# test = df.loc[:, Dim["test"]]
# a = pg.cronbach_alpha(data=test)
# print(a)
