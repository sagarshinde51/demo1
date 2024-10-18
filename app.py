import streamlit as st

# Hardcoded credentials for demonstration
credentials = {
    "student": "student123",
    "teacher": "teacher123"
}

# Function to check login
def check_login(user_id, password):
    return credentials.get(user_id) == password

# Streamlit app title
st.title("Subjective Answers Evaluation Login Page")

# Create a two-column layout
col1, col2 = st.columns(2)

# Column for the image
with col1:
    st.image("nlp2.jpg", use_column_width=True)  # Adjust the path as necessary

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_id = None

# Column for the login form
with col2:
    # Use HTML to set the font size for the title
    st.markdown("<h2 style='font-size: 30px;'>Login System</h2>", unsafe_allow_html=True)

    if not st.session_state.logged_in:
        with st.form("login_form"):
            user_id = st.text_input("Enter your User ID (e.g., student or teacher):")
            password = st.text_input("Password", type="password")
            
            # Submit button
            submitted = st.form_submit_button("Login")
            
            if submitted:
                if check_login(user_id.lower(), password):
                    st.session_state.logged_in = True
                    st.session_state.user_id = user_id.lower()
                    st.success(f"Welcome, {user_id}!")
                    
                    # Provide link to the dashboard in a new tab
                    if st.session_state.user_id == "student":
                        pass
                    elif st.session_state.user_id == "teacher":
                        import os
                        a = "streamlit run C:\\Users\\DELL\Desktop\\AI\\pdfEval.py"
                        os.system(a)
                else:
                    st.error("Incorrect user ID or password. Please try again.")

