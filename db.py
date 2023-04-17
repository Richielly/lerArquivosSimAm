import fdb

# Substitua os valores entre aspas pelos detalhes do seu banco de dados.
database_path = r"D:\Unifica\283\destino\EQUIPLANO.FDB"
user = "sysdba"
password = "masterkey"
host = "localhost"  # ou o endereço IP do servidor

codEntidade = 53

# String de conexão.
dsn = f"{host}:{database_path}"

# Conectando ao banco de dados.
connection = fdb.connect(dsn=dsn, user=user, password=password)

# Criando um cursor para executar consultas SQL.
cursor = connection.cursor()

# Executando uma consulta SQL de exemplo.
cursor.execute(f"""select cs.vlracumuladorinicial as inicio, cs.vlracumuladorfinal as final from SCF_VEICULOCONTROLESIMAM cs
join SCF_VEICULO v on (cs.IDVEICULO = v.IDVEICULO)
join scp55_bem b on (b.idbem = v.idbem)
where
cs.dtlancamento between '27.12.2022' and '27.01.2023' and
v.CODENTIDADE = {codEntidade} """)

# Exibindo os resultados da consulta.
for row in cursor.fetchall():
    print(row)

# Fechando o cursor e a conexão.
cursor.close()
connection.close()