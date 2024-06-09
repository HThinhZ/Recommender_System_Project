import streamlit as st
from new_user import App as New_User_App

class App():
    def __init__(self) -> None:
        pass
    
    def traditional_survey(self):
        fmi_df = st.session_state['fmi_df']

        genre = fmi_df[["genre"]].explode("genre")
        ls_genre = genre["genre"].dropna().unique()

        actor = fmi_df[["actors"]].explode("actors")
        ls_actor = actor["actors"].dropna().unique()

        director = fmi_df[["directors"]].explode("directors")
        ls_director = director["directors"].dropna().unique()
        
        ls_country =  fmi_df["releaseLocation"].dropna().unique()

        st.header("Khảo sát truyền thống")
        genres = st.multiselect("Chọn thể loại phim yêu thích:", ls_genre)
        actors = st.multiselect("Chọn diễn viên yêu thích:", ls_actor)
        directors = st.multiselect("Chọn đạo diễn yêu thích:", ls_director)
        country = st.multiselect("Chọn quốc gia yêu thích:", ls_country)
        interest = st.selectbox("Chọn sở thích khám phá:", ["Phim mới", "Bình thường", "Phim cổ điển"],index=1)

        if st.button("Gửi", key="traditional_but"):
            New_User_App(type_survey=0, data=[genres, actors, directors, country, interest]).run()


    def modern_survey(self):
        st.header("Khảo sát hiện đại")
        experience = st.text_area("Hãy cho chúng tôi biết trải nghiệm xem phim của bạn, các sở thích về phim:")

        if st.button("Gửi", key="modern_but"):
            New_User_App(type_survey=1, data=experience).run()


    def run(self):
        st.title("Khảo sát")

        # Tạo 2 tab cho 2 loại survey
        tabs = st.tabs(["Khảo sát truyền thống", "Khảo sát hiện đại"])

        with tabs[0]:
            self.traditional_survey()
        with tabs[1]:
            self.modern_survey()