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

        with st.form("traditional_form"):

            st.header("Khảo sát truyền thống")
            genres = st.multiselect("Chọn thể loại phim yêu thích:", ls_genre)
            actors = st.multiselect("Chọn diễn viên yêu thích:", ls_actor)
            directors = st.multiselect("Chọn đạo diễn yêu thích:", ls_director)
            country = st.multiselect("Chọn quốc gia yêu thích:", ls_country)
            interest = st.selectbox("Chọn sở thích khám phá:", ["Phim mới", "Bình thường", "Phim cổ điển"],index=1)

            submitted = st.form_submit_button("Submit")
        if submitted:
            # placeholder.empty()
            # with placeholder.container():
            New_User_App(type_survey=0, data=[genres, actors, directors, country, interest]).run()


    def modern_survey(self):
        with st.form("modern_form"):
            st.header("Khảo sát hiện đại")
            experience = st.text_area("Hãy cho chúng tôi biết trải nghiệm xem phim của bạn, các sở thích về phim.", 
                                      placeholder =" Ví dụ: Tôi thích các bộ phim kinh dị và cũng thích khám phá những bộ phim đã cũ")

            submitted = st.form_submit_button("Submit")
        if submitted:
            # placeholder.empty()
            # with placeholder.container():
            New_User_App(type_survey=1, data=experience).run()


    def run(self):
        # placeholder = st.empty()
        # with placeholder.container(): 
        st.title("Khảo sát")

        # Tạo 2 tab cho 2 loại survey
        tabs = st.tabs(["Khảo sát truyền thống", "Khảo sát hiện đại"])

        with tabs[0]:
            self.traditional_survey()
        with tabs[1]:
            self.modern_survey()
        

        
