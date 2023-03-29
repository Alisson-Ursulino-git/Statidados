#%% """Importanto Pacotes"""
import os
import dotenv


import dtale.global_state as global_state
from dtale.app import build_app
from dtale.views import startup
from flask import redirect
from waitress import serve #server()

#%% Importando Dataframe
#import sys
#caminho = r'C:\Users\aliss\Meu Drive (pesquisaursulino@gmail.com)\statidados\Live2'
#sys.path.append(caminho)

#import tratamento
from data_frame.tratamento import created_data
df = created_data()

#%% Extraindo Senhas
#dotenv.load_dotenv(caminho+'\security\stat.env')
login=os.getenv('login')
password=os.getenv('senha')
#%% Run D-Tale Flask APP



global_state.set_auth_settings({'active': True, 'username': login, 'password': password})
global_state.set_app_settings({'language':'pt', 'theme':'dark'})


app_dtale = build_app(reaper_on=False)


def location_df():
    instance = startup(data_id="1", data=df, ignore_duplicate=True)
    location = f"/dtale/main/{instance._data_id}"
    return location

#link_url='http://127.0.0.1:5000'+ location_df()
#print(link_url)
 
@app_dtale.route("/")
def create_df():
    return redirect(location_df(), code=302)
   
if __name__ == '__main__':
    #app_dtale.run(host="127.0.0.1", port='5000')
    serve(app_dtale)
   
