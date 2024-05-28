# Import libraries
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st
from streamlit_option_menu import option_menu

# Import file.py
from init import *
from settings import *
from modules.home import App as Home_App
from modules.advancedsearch import App as AS_App


# Main
if __name__ == '__main__':
    setup()
    ## Connect to MongoDB:
    client =  MongoClient(MONGODB_HOST)
    db = client['T2_PreprocessedData']
    collector = Collector(client, db)
    fmi_df, mi_df, ui_df, r_df = collector.run()

    with st.sidebar:
        page = option_menu("Main Menu", ['Trang chủ', '??', '???', "Tìm kiếm nâng cao"], 
            icons=['house', 'gear'], menu_icon="cast", default_index=1)
        
    # page = option_menu("Menu", ["???", "???", "???", '???'], 
    #     icons=['house', 'cloud-upload', "list-task", 'gear'], 
    #     menu_icon="cast", default_index=0, orientation="horizontal")

    ## Function
    if page == "Trang chủ":
        home_app = Home_App()
        home_app.run()
    elif page == "Tìm kiếm nâng cao":
        as_app = AS_App(fmi_df)
        as_app.run()
