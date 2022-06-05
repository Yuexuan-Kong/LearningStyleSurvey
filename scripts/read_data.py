import pandas as pd
import pyreadstat

def read_data(path): # path = "../data/"
       path_ch = path + "chinese.sav"
       path_fr = path + "france.sav"
       df_ch, _ = pyreadstat.read_sav(path_ch)
       df_fr, _ = pyreadstat.read_sav(path_fr)
       dim = {
              "Act_Ref":[4, 10, 16, 22, 28, 34, 40],
              "Sen_Int":[5, 11, 17, 23, 29, 35, 41],
              "Vis_Ver":[6, 12, 18, 24, 30, 36, 42],
              "Seq_Glo":[7, 13, 19, 25, 31, 37, 43],
              "Ded_Ind":[8, 14, 20, 26, 32, 38, 44],
              "Lea_Per":[9, 15, 21, 27, 33, 39, 45]
              }
       df = pd.concat([df_ch, df_fr])
       # df = df.drop(df[df.totalseconds.astype(int) < 380].index)
       # df = df.drop(df[df.totalseconds.astype(int) > 2500].index)

       dim = {
              "Act_Ref": ['Q4', 'Q10', 'Q16', 'Q22', 'Q28', 'Q34', 'Q40'],
              "Sen_Int": ['Q5', 'Q11', 'Q17', 'Q23', 'Q29', 'Q35', 'Q41'],
              "Vis_Ver": ['Q6', 'Q12', 'Q18', 'Q24', 'Q30', 'Q36', 'Q42'],
              "Seq_Glo": ['Q7', 'Q13', 'Q19', 'Q25', 'Q31', 'Q37', 'Q43'],
              "Ded_Ind": ['Q8', 'Q14', 'Q20', 'Q26', 'Q32', 'Q38', 'Q44'],
              "Lea_Per": ['Q9', 'Q15', 'Q21', 'Q27', 'Q33', 'Q39', 'Q45']
       }
       all_Q_index = dim["Act_Ref"] + dim["Sen_Int"] + dim["Vis_Ver"] + dim["Seq_Glo"] + dim["Ded_Ind"] + dim["Lea_Per"]
       all = df.loc[:, all_Q_index]
       all = all.reset_index()
       return all, dim, all_Q_index
