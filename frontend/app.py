
import streamlit as st
import requests


# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="AmanAI Lab | Competitor Intelligence",
    page_icon="📊",
    layout="wide"
)


# =====================================
# HEADER
# =====================================

st.title("📊 Competitor Intelligence Platform")

st.write(
    "AI-powered market research and competitor analysis "
    "using a multi-agent system."
)

st.divider()


# =====================================
# RESEARCH INPUT FORM
# =====================================

st.header("Create New Research")

with st.form("research_form"):

    company = st.text_input(
        "Company Name",
        placeholder="Example: Netflix"
    )

    competitors = st.text_input(
        "Competitors",
        placeholder="Amazon Prime Video, Disney+"
    )

    country = st.selectbox(
        "Select Country",
        [
            "India",
            "USA",
            "UK",
            "Canada",
            "Australia"
        ]
    )

    research_objective = st.text_area(
        "Research Objective",
        placeholder="Analyze market position, products, pricing and SWOT..."
    )

    submitted = st.form_submit_button(
        "🚀 Start Competitor Research",
        use_container_width=True
    )


# =====================================
# CALL FASTAPI BACKEND
# =====================================

if submitted:

    if not company.strip():
        st.error("Please enter a company name.")

    elif not competitors.strip():
        st.error("Please enter competitors.")

    elif not research_objective.strip():
        st.error("Please enter a research objective.")

    else:

        competitor_list = [
            item.strip()
            for item in competitors.split(",")
            if item.strip()
        ]

        payload = {
            "company": company.strip(),
            "competitors": competitor_list,
            "country": country,
            "research_objective": research_objective.strip()
        }

        api_url = "http://127.0.0.1:8000/api/v1/research"

        try:

            with st.spinner(
                "AI agents are researching. Please wait..."
            ):

                response = requests.post(
                    api_url,
                    json=payload,
                    timeout=600
                )

            if response.status_code == 200:

                result = response.json()

                st.session_state["research_result"] = result

                st.success("Research completed successfully!")

            else:

                st.error(
                    f"API Error: {response.status_code}"
                )

                st.code(response.text)

        except requests.exceptions.ConnectionError:

            st.error(
                "Cannot connect to FastAPI. "
                "Please make sure the backend is running."
            )

        except requests.exceptions.Timeout:

            st.error(
                "The request timed out. Check the backend terminal."
            )

        except requests.exceptions.RequestException as error:

            st.error(f"Request failed: {error}")


# =====================================
# DISPLAY FINAL REPORT
# =====================================

if "research_result" in st.session_state:

    result = st.session_state["research_result"]

    st.divider()

    st.header("Research Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Company",
        result["company"]
    )

    col2.metric(
        "Competitors",
        len(result["competitors"])
    )

    col3.metric(
        "Country",
        result["country"]
    )

    st.divider()

    st.header("Final Competitor Intelligence Report")

    st.markdown(result["report"])

    st.download_button(
        "📥 Download Research Report",
        data=result["report"],
        file_name="competitor_intelligence_report.txt",
        mime="text/plain"
    )
