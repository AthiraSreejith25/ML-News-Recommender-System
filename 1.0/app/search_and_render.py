import streamlit as st
from db_news import *

NEWS_HTML_TEMPLATE = """
<div style="width:100%;height:100%;margin:1px;padding:5px;
position:relative;border-radius:5px;border-bottom-right-radius: 10px;
box-shadow:0 0 1px 1px #eee; background-color: #31333F;
  border-left: 5px solid #6c6c6c;color:white;">
<h4>{}</h4>
<h5><a href = "{}">{}</a></h5>
<h6>{}</h6>
<h6>{}</h6>
</div>
<br></br>
"""

def search(search_term,submit_search):
    # Nav  Search Form
    col,_ = st.columns([2,1])
    with col:
        if submit_search:
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
                #st.subheader(i)
                headline = i[1]
                category = i[0]
                _url = i[5]
                date = i[2]
                st.markdown(NEWS_HTML_TEMPLATE.format(headline,_url,category,date),
                        unsafe_allow_html=True)

def render():
    news_res = db_execute()
    for i in news_res:
            headline = i[1]
            category = i[0]
            _url = i[5]
            date = i[2]
            #st.checkbox("Did you Like it ?")
            st.checkbox("Did you like it ?",key=headline)
            st.markdown(NEWS_HTML_TEMPLATE.format(headline,_url,_url,category,date),
                    unsafe_allow_html=True)
            