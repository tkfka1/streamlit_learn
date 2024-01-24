import streamlit as st

st.set_page_config(page_title="Data Engineering Zoomcamp 2023", page_icon='👨‍🔧')

st.write("#")

st.markdown("### 👨‍🔧 Data Engineering Zoomcamp 2023 by [DataTalksClub](https://datatalks.club/)")

st.markdown("""
### 📄 Syllabus

##### <a href="ApexCharts" target='_self'>ApexCharts</a>
##### <a href="app" target='_self'>app</a>
##### <a href="Week_3_Data_Warehouse" target='_self'>Week 3: Data Warehouse</a>
##### <a href="Week_4_Analytics_Engineering" target='_self'>Week 4: Analytics Engineering</a>
##### <a href="Week_5_Batch_processing" target='_self'>Week 5: Batch Processing</a>
##### <a href="Week_6_Stream_Processing" target='_self'>Week 6: Stream Processing</a>
##### <a href="Week_7_Project" target='_self'>Week 7: Project</a>

---

### 👨‍🎓 Taking the course

####

##### 👨‍👦‍👦 2024 Cohort

* **Start**: 15 January 2024 
* **Registration link**: https://airtable.com/appzbS8Pkg9PL254a/shr6oVXeQvSI5HuWD 


##### 👥 2023 Cohort

* **Start**: 16 January 2023 (Monday) at 18:00 CET
* **Registration link**: https://airtable.com/shr6oVXeQvSI5HuWD
* Subscribe to our [public Google Calendar](https://calendar.google.com/calendar/?cid=ZXIxcjA1M3ZlYjJpcXU0dTFmaG02MzVxMG9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ) (it works from Desktop only)
* [Cohort folder](cohorts/2023/) with homeworks and deadlines""", unsafe_allow_html=True)

st.error("2023 Cohort ended in the 18th May of 2023. To see 2023 cohort ressources see this [link](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/cohorts/2023).")


hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 