import oracledb


engine_oracle = oracledb.connect('system/iaea_123@localhost:1523/IAEA')


with engine_oracle.cursor() as conn:
    respuesta = conn.execute("""SELECT * FROM IAEA.REACTORES R WHERE R.ID = 9""")
    columns = [col[0] for col in respuesta.description]
    respuesta.rowfactory = lambda *args: dict(zip(columns, args))
    respuesta = respuesta.fetchall()

print('respuesta: ', respuesta)
