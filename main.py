import os

import pandas as pd
import glob

codEntidade = 39

file = glob.glob(r'C:\Users\Equiplano\Desktop\Relatorios\Controle_Interno')
file_2 = glob.glob(r'C:\Users\Equiplano\Desktop\Relatorios\01-2023')
# os.chdir(file[0])

df = pd.read_csv(file[0]+'\HodometroHorimetro.txt', sep="|", header=None, dtype="str") #header=None se quiser colocar sem cabeçalho
df_2 = pd.read_csv(file_2[0]+'\HodometroHorimetro.txt', sep="|", header=None, dtype="str")

df = df.astype(str)
df_2 = df_2.astype(str)

df = df.get([1, 3, 4, 6, 7])
df_2 = df_2.get([1, 3, 4, 6, 7])

result = pd.DataFrame(df)
result_2 = pd.DataFrame(df_2)

file_name = "sqlUpdate_Hodometro_Horimetro.txt"

def data_inicial():
    for linha in result.values:
    #     sql = f"select * from SCP55_BEM where codbem = '{linha[0]}' union all"
        sql = f""" update SCF_VEICULOCONTROLESIMAM cs set cs.VLRACUMULADORINICIAL = {linha[4]} where cs.IDVEICULOCONTROLESIMAM = (select cs.IDVEICULOCONTROLESIMAM from SCF_VEICULOCONTROLESIMAM cs
                    join SCF_VEICULO v on (cs.IDVEICULO = v.IDVEICULO)
                    join scp55_bem b on (b.idbem = v.idbem)
                    where
                    cs.dtlancamento between '01.01.2023' and '01.02.2023' and
                    v.CODENTIDADE = {codEntidade} and 
                    b.codbem = '{linha[0]}'); """

        with open('Inicial'+file_name, 'a', encoding='utf-8') as file:
            file.write(f'\n{sql}')


def data_final():
    for linha in result.values:
        sql = f""" update SCF_VEICULOCONTROLESIMAM cs set cs.VLRACUMULADORFINAL = {linha[4]} where cs.IDVEICULOCONTROLESIMAM = (select cs.IDVEICULOCONTROLESIMAM from SCF_VEICULOCONTROLESIMAM cs
                    join SCF_VEICULO v on (cs.IDVEICULO = v.IDVEICULO)
                    join scp55_bem b on (b.idbem = v.idbem)
                    where
                    cs.dtlancamento between '27.12.2022' and '27.01.2023' and
                    v.CODENTIDADE = {codEntidade} and 
                    b.codbem = '{linha[0]}'); """

        with open('Final'+file_name, 'a', encoding='utf-8') as file:
            file.write(f'\n{sql}')

data_final()