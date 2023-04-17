# select cs.* from SCF_VEICULOCONTROLESIMAM cs
# join SCF_VEICULO v on (cs.IDVEICULO = v.IDVEICULO)
# join scp55_bem b on (b.idbem = v.idbem)
# where
# cs.dtlancamento > '27.12.2022' and
# v.CODENTIDADE = 39
#
# select 'CE', b.codbem as bem, 'N', 'Comp', 'Exer', 'N', cs.vlracumuladorinicial as inicio, cs.vlracumuladorfinal as final from SCF_VEICULOCONTROLESIMAM cs
# join SCF_VEICULO v on (cs.IDVEICULO = v.IDVEICULO)
# join scp55_bem b on (b.idbem = v.idbem)
# where
# cs.dtlancamento between '27.12.2022' and '27.01.2023' and
# v.CODENTIDADE = 39