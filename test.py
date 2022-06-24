from main import get_data_countries, connect_to_db

#probar conexion a la db
def test_connect_to_db():
    db_con = connect_to_db()
    assert db_con[1] == True

#comprobar si hay respuesta de la api consumida
def test_get_data_countries():
    url = "https://restcountries.com/v3.1/all"
    res = get_data_countries(url)
    assert res.status_code == 200