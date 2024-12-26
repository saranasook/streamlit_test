import streamlit as st
import pandas as pd

with st.echo():
    st.title("Getting start streamlit")
    # st.write("test")

    st.markdown("## my mark down")

    code = '''def hello():
        print("Hello, Streamlit!")'''


    run_btn         = st.button("Show code!")
    if run_btn:
        st.markdown("Button has already clicked!")
        st.code(code, language="python")


    cols            = st.columns(2)

    with cols[0]:
        age_inp         = st.number_input("Input your age")
        st.markdown(f"Your age is {age_inp}")

    with cols[1]:
        # st.markdown("# NLP Task")
        text_inp        = st.text_input("Input you text")
        word_tokenize   = "|".join(text_inp.split()) 
        st.markdown(f"{word_tokenize}") 

    df                  = pd.DataFrame(
        {
            'first column': [1,2,3,4],
            'second column': [10,20,60,90]
        }
    )

    st.dataframe(df)
    show_chart_btn       = st.button("Show Chat")

    if show_chart_btn:
        st.line_chart(df, x = 'first column', y = 'second column')