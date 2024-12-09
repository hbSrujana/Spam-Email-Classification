import streamlit as st
import pickle
from PIL import Image

# Load model and vectorizer
model = pickle.load(open('spam123.pkl', 'rb'))
cv = pickle.load(open('vec123.pkl', 'rb'))

# Set page configuration
st.set_page_config(
    page_title="Email Spam Classifier",
    page_icon="📧",
    layout="wide",
)

# Add custom background and styling
def add_custom_styles():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f4f4f4;
        }
        .main-title {
            font-size: 30px;
            color: #2e3b4e;
            font-weight: bold;
        }
        .sub-text {
            color: #606c81;
            font-size: 16px;
        }
        .footer {
            text-align: center;
            color: #7a7a7a;
            font-size: 14px;
        }
        .email-classification {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .result-box {
            border: 2px solid #007bff;
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            margin-top: 10px;
            font-size: 18px;
            font-weight: bold;
            color: black;
            text-align: center;
        }
        .spam {
            border-color: #dc3545;
        }
        .not-spam {
            border-color: #28a745;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def main():
    add_custom_styles()
    
    # Add sidebar
    with st.sidebar:
        st.header("📑 About")
        st.write("This app uses a Machine Learning model to classify emails as spam or not spam.")
        st.write("Enter an email and click **Classify** to see the result.")
    
    # Header
    st.markdown("<h1 class='main-title'>Email Spam Classifier</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-text'>Detect spam emails with this simple app powered by Machine Learning.</p>", unsafe_allow_html=True)
    
    # Main classification section
    with st.container():
        st.markdown("<div class='email-classification'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: black;'>🔍 Email Classification</h3>", unsafe_allow_html=True)
        
        user_input = st.text_area(
            "Enter your email content below:",
            height=200,
            placeholder="Type your email here...",
        )
        
        if st.button("Classify 🚀"):
            if user_input.strip():
                data = [user_input]
                vec = cv.transform(data).toarray()
                result = model.predict(vec)
                
                if result[0] == 0:
                    st.markdown(
                        "<div class='result-box not-spam'>✅ This is <strong>Not a Spam Email</strong></div>",
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        "<div class='result-box spam'>🚨 This is <strong>A Spam Email</strong></div>",
                        unsafe_allow_html=True,
                    )
            else:
                st.warning("⚠️ Please enter some text to classify.")
        st.markdown("</div>", unsafe_allow_html=True)

    # Footer
    st.markdown(
        "<div class='footer'>Developed by Srujana H B • Powered by Streamlit</div>",
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
