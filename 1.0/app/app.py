import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from db_credentials import *
from search_and_render import *
import numpy as np



def main():
    """Securing Login Apps"""

    st.title("News Recommender")

    menu = ["Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        # st.subheader("Login Into App")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        if st.sidebar.checkbox("Login"):
            create_usertable()
            result = login_user(username, password)
            # result = login_user_unsafe(username,password)
            # if password == "12345":
            if result:
                st.success("Logged In as {}".format(username))

                # task = st.selectbox("Task",["Add Posts","Analytics","Manage"])

                selected = option_menu(
                    menu_title=None,
                    options=["Home", "Recommended", "Search"],
                    icons=["house", "activity", "search"],
                    orientation="horizontal",
                    default_index=0,
                )

                if selected == "Home":
                    col1, col2 = st.columns([3, 1])
                    #data = np.random.randn(10, 1)

                    col1.subheader("News")
                    with col1:
                        render()
                        
                    # container = st.container()
                    # with col1.st.container():
                    #col1.subheader("This is an example headline for a news article")
                    #col1.image("https://static.streamlit.io/examples/dice.jpg")

                    #col2.subheader("Trending")
                    #col2.write(data)

                if selected == "Recommended":
                    pass

                if selected == "Search":
                    with st.form(key="searchform"):
                        nav1, nav2 = st.columns([3, 1])

                    with nav1:
                        search_term = st.text_input("Search")

                    with nav2:
                        st.text("Search ")
                        submit_search = st.form_submit_button(label="Search")
                        
                    #st.success("You searched for {} ".format(search_term))
                    search(search_term,submit_search)
                    # Results

            else:
                st.warning("Incorrect Username/Password")

    if choice == "SignUp":
        st.subheader("Create An Account")
        new_username = st.text_input("User name")
        new_password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        if new_password == confirm_password:
            st.success("Valid Password Confirmed")
        else:
            st.warning("Password not the same")

        if st.button("Sign Up"):
            create_usertable()
            add_userdata(new_username, new_password)
            st.success("Successfully Created an Account")


if __name__ == "__main__":
    main()
