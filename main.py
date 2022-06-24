import datetime
import requests, hashlib, time
import pandas
import sqlite3

def connect_to_db():
    try:
        conn = sqlite3.connect('countries_data.db')
        return (conn, True)
    except:
        return (conn, False)

def get_data_countries(url):
    data = requests.get(url)
    return data

def get_countries_info(url):
    start_time = time.process_time()
    conn = connect_to_db()
    if conn[1] == True:

        print(".... Getting data ....")
        str_langs = ""
        list_regions = []
        list_cities = []
        list_lang = []
        list_times = []
        data_df = {}
        try:
            data = get_data_countries(url)
            if data.status_code != 200:
                print("Ha ocurrido un problema al conectar a la API")
                raise SystemExit()
            else:
                data = data.json()
                for item in data:
                    #ALIMENTAR EL DATA FRAME, ARMAR UNA LISTA Y LUEGO ESA COLOCARLA EN EL DICCIONARIO CON CADA CAMPO
                    list_regions.append(item['region'])
                    list_cities.append(item['name']['common'])

                    if item['name']['common'] == "Antarctica":
                        language = "No Language"
                        str_langs = language
                    else:
                        language = item['languages']
                        if len(language) > 1:
                            for item_language in language:
                                str_langs += language[item_language] + ','
                        else:
                            for item_language in language:
                                str_langs = language[item_language]

                    str_lang_encrypted = hashlib.sha1(str_langs.encode())
                    list_lang.append(str_lang_encrypted.hexdigest())
                    end_time = time.process_time()
                    total_time = end_time - start_time
                    list_times.append(total_time)

                data_df['Region'] = list_regions
                data_df['City_Name'] = list_cities
                data_df['Language'] = list_lang
                data_df['Time'] = list_times

                table = pandas.DataFrame(data_df).sort_values(by=['Region']).set_index('Region')

                #calculando el tiempo total de creación de dataframe
                # calcular el tiempo total, tiempo promedio, tiempo minimo y maximo que se tardó en procesar todas las filas de la tabla
                statistics = {
                    'total_time': str(table['Time'].sum())+" secs",
                    'avg_time': str(table['Time'].mean())+" ms",
                    'min_time': str(table['Time'].min())+" ms",
                    'max_time': str(table['Time'].max())+" ms"
                }
                #Guardar resultadp en SQLITE
                #se crea una nueva tabla si no existe y se le agrega una datetime para diferenciar, por si se hace una peticion diferente en el endpoint
                date_db = str(datetime.datetime.now())
                sqlite_tab_name = "countries_data_"+date_db
                table.to_sql(sqlite_tab_name, conn[0])

                #Generar JSON de la tabla creada, guardar como data.json
                table.to_json("data.json", orient='table')

                #returns dataframe y tiempos estadisticos para poder probar en un test
                return [statistics, table]


        except requests.exceptions.RequestException as e:
            print("Ha ocurrido un problema al conectar a la API")
            raise SystemExit(e)

    else:
        print("Hubo un problema al conectar a la DB")
        raise SystemExit()

if __name__ == '__main__':
    # url = 'https://restcountries.com/v3.1/capital/mexico'
    # url = 'https://restcountries.com/v3.1/region/america'
    url = 'https://restcountries.com/v3.1/all'
    res = get_countries_info(url)
    print("---- DataFrame Creado ----")
    print(res[1].sort_values(by=['Region']))
    print("----  ----")
    print("---- Tiempos estadísticos de generación del total filas del DataFrame ----")
    print("* Tiempo total de procesamiento: " + res[0]['total_time'])
    print("* Tiempo promedio de procesamiento: " + res[0]['avg_time'])
    print("* Tiempo minimo de procesamiento: " + res[0]['min_time'])
    print("* Tiempo maximo de procesamiento: " + res[0]['max_time'])
    print("NOTA: para visualizar mejor el contenido de la tabla, consulte la base de datos llamada countries_data.db creada automáticamente o consulte el archivo llamado data.json")
