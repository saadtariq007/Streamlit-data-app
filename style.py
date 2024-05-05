# styles.py
def load_css():
    css = """
    <style>
        /* Main text and headers color - Slate Grey */
        body, h1, h2, h3, h4, h5, h6, .stButton > button {
            color: #596E79;
        }
        
        /* Primary background color - Light Blue Grey */
        body, .stApp, .stTextInput > input {
            background-color: #ECEFF1;
        }
        
        /* Sidebar background - Grey */
        .css-1lcbmhc {
            background-color: #B2B2B2;
        }
        
        /* Accent color for buttons and active elements - Green */
        .stButton > button, .stTextInput > input:focus {
            background-color: #4CAF50;
            border-color: #4CAF50;
        }
        
        /* Hover effect for buttons */
        .stButton > button:hover {
            background-color: #367c39;
        }
    </style>
    """
    return css
