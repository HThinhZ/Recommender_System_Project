import streamlit as st
from datetime import timedelta
import pandas as pd
from tool import *

def check_in_list(x, val_to_check):
  return any(value in x for value in val_to_check)

def suggest_for_newuser(mi_df, type_filter, filter, discover):
    ls_movie = ()
    new_movie = ()
    top_by_filter = ()

    #  Lọc df theo sở thích
    if filter != []: filter_movie = mi_df[mi_df[type_filter].apply(lambda x: check_in_list(x, filter))]
    else: filter_movie = pd.DataFrame()


    if discover == "Phim mới":
        timedelta_to_compare = timedelta(days=730)
        if filter != []:
            new_movie = filter_movie.sort_values("deltaDate")["movie_id"].head(9).to_list()
            top_by_filter =  filter_movie[filter_movie["deltaDate"] <= timedelta_to_compare].sort_values(["ratingStar","totalRatings"],  ascending=False)["movie_id"].head(6).to_list()
        else:
            new_movie = mi_df.sort_values("deltaDate")["movie_id"].head(9).to_list()
            top_by_filter =  mi_df[mi_df["deltaDate"] <= timedelta_to_compare].sort_values(["ratingStar","totalRatings"],  ascending=False)["movie_id"].head(6).to_list()

    elif discover == "Bình thường":
        if filter != []:
            new_movie = filter_movie.sort_values("deltaDate")["movie_id"].head(9).to_list()
            top_by_filter =  filter_movie.sort_values(["ratingStar","totalRatings"],  ascending=False)["movie_id"].head(8).to_list()
        else:
            new_movie = mi_df.sort_values("deltaDate")["movie_id"].head(9).to_list()
            top_by_filter =  mi_df.sort_values(["ratingStar","totalRatings"],  ascending=False)["movie_id"].head(8).to_list()

    else:
        timedelta_to_compare = timedelta(days=1825)
        if filter != []:
            new_movie = filter_movie[filter_movie["ratingStar"] >= 7.5].sort_values("deltaDate", ascending=False)["movie_id"].head(9).to_list()
            top_by_filter =  filter_movie[filter_movie["deltaDate"] >= timedelta_to_compare].sort_values(["ratingStar","totalRatings"],  ascending=False)["movie_id"].head(6).to_list()
        else:
            new_movie = mi_df[mi_df["ratingStar"] >= 7.5].sort_values("deltaDate", ascending=False)["movie_id"].head(9).to_list()
            top_by_filter =  mi_df[mi_df["deltaDate"] >= timedelta_to_compare].sort_values(["ratingStar","totalRatings"],  ascending=False)["movie_id"].head(6).to_list()


    ls_movie = top_by_filter.copy()
    for item in new_movie:
        if item not in top_by_filter and len(ls_movie) < 9:
            ls_movie.append(item)

    return ls_movie


def get_inf(mi_df, set_item):
    sr = pd.DataFrame(set_item, columns=["movie_id"])
    res = mi_df.merge(sr, on="movie_id", how="inner")
    return res



class App():
    def __init__(self, type_survey, data):
        # data=[ls_genre, ls_actor, ls_director, ls_country, interest]
        self.type_survey = type_survey
        if self.type_survey == 0:
            self.ls_genre = data[0]
            self.ls_actor = data[1]
            self.ls_director = data[2]
            self.ls_country = data[3]
            self.interest = data[4]
        else:
            self.text = data

    def display_movies_based_on_preference(self, fmi_df, preference_list, input,header, all_movies_set):
        if input:
            st.header(header)
            st.write(display_columns(get_inf(fmi_df, preference_list), 3))
            return False
        else:
            all_movies_set.update(preference_list)
            return True
    
    def run(self):
        fmi_df = st.session_state['fmi_df']
        
        st.title("Các phim có thể bạn thích")
        option = st.selectbox(
        'Chọn nội dung muốn hiển thị:',
        ('Kết quả', 'Thông tin')
        )
        

        if self.type_survey == 0:
            lis_genre = suggest_for_newuser(fmi_df, "genre", self.ls_genre, self.interest)
            lis_actor =  suggest_for_newuser(fmi_df, "actors", self.ls_actor, self.interest)
            lis_director =  suggest_for_newuser(fmi_df, "directors", self.ls_director, self.interest)
            lis_location =  suggest_for_newuser(fmi_df, "releaseLocation", self.ls_country, self.interest)

            set_movie = set()
            have_empty = False
            if option == 'Kết quả':
                have_empty |= self.display_movies_based_on_preference(fmi_df, lis_genre, self.ls_genre,"Các bộ phim thuộc thể loại bạn thích:", set_movie)
                have_empty |= self.display_movies_based_on_preference(fmi_df, lis_actor, self.ls_actor,"Các bộ phim của diễn viên bạn thích:", set_movie)
                have_empty |= self.display_movies_based_on_preference(fmi_df, lis_director, self.ls_director,"Các bộ phim của đạo diễn bạn thích:", set_movie)
                have_empty |= self.display_movies_based_on_preference(fmi_df, lis_location, self.ls_country,"Các bộ phim của quốc gia bạn thích:", set_movie)

                if have_empty:
                    ls_movie = list(set_movie)
                    st.header("Các bộ phim có thể bạn thích:")
                    st.write(display_columns(get_inf(fmi_df, ls_movie), 3))

            else:
                st.write("hi")
