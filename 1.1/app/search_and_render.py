#from nis import cat
import streamlit as st
from db_news import *

# <p><input type="button" value="Read more" style="float: right; background-color:green; color: white"></p>
#31333F

NEWS_HTML_TEMPLATE = """
<div style="width:100%;height:100%;margin:1px;padding:5px;
position:relative;border-radius:5px;border-bottom-right-radius: 10px;
box-shadow:0 0 1px 1px #eee; background-color:black;
border-left: 5px solid #6c6c6c;
border-top: 5px solid #6c6c6c;color:white;">
<h4>{}</h4>
<h5>{}</h5>
<h5>{}</h5>
</div>
"""
#<h5><a href = "{}">{}</a></h5>

def search(search_term):
    # Nav  Search Form

    # Create Search Query
    search_res = search_news(search_term)
    # st.write(search_url)

    # Number of Results
    num_of_results = len(search_res)
    if num_of_results == 0:
        st.subheader("No news found relating to your query")
    else:
        st.subheader("Showing {} News".format(num_of_results))
        # st.write(data)

        for i in search_res:
            # st.subheader(i)
            id = i[0]
            headline = i[2]
            category = i[1]
            _url = i[6]
            date = i[3]
            st.markdown(
                NEWS_HTML_TEMPLATE.format(headline, 'Category: {}'.format(category), 'Date: {}'.format(date[1:-1].replace(',',' - '))),
                unsafe_allow_html=True,
            )
            st.text(" ")
            with st.expander("Read more"):
                st.write(i[4])
            #bclick = st.button("Read more", key=id)
            st.title(" ")

            #if bclick:
             #   st.expander(i[4])
    # if st.button("Read more",key=id):
    #     pass


def render():
    news_res = db_execute()
    '''news_res = db_execute_all()
    category = set()
    for i in news_res:
        category.add(i[1])
    
    st.multiselect('News categories',category)'''

    for i in news_res:
        id = i[0]
        #st.text(id)
        headline = i[2]
        category = i[1]
        _url = i[6]
        date = i[3]
        # st.checkbox("Did you Like it ?")
        # st.checkbox("Did you like it ?",key=headline)
        st.markdown(
            NEWS_HTML_TEMPLATE.format(headline, 'Category: {}'.format(category), 'Date: {}'.format(date[1:-1].replace(',',' - '))),
            unsafe_allow_html=True,
        )
        st.text(" ")
        click = st.button("Read more", key=id)

        if click:

            st.info(i[4])
            st.checkbox("like",key=id)
            st.checkbox("dislike",key=id)


        '''
        exp = st.expander("Read more")
        with exp:
            if exp:
                #st.code(type(exp.expanded))
                st.write(i[4])
                #st.radio('weights',options=('Like','Dislike'))
                st.checkbox("like",key=id)
                st.checkbox("dislike",key=id)
        '''
        st.title(" ")

def recommended_render():
    news_res = db_execute_all()
    category = set()
    for i in news_res:
        category.add(i[1])
    
    st.multiselect('News categories',category)
