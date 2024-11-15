import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from utils.util import extract_geolocation
from utils.google_map import GoogleMAP
from utils.route_guru import RouteGuru
from decouple import config

st.set_page_config(page_title="Noela's RouteGuru", page_icon="🗺️", layout="wide")

# Sidebar for navigation and API key input
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
rg = RouteGuru(api_key=api_key)

with st.sidebar:
    page = option_menu(
        "RouteGuru",
        ["Home", "About Me", "RouteGuru"],
        icons=['house', 'person-circle', 'map'],
        menu_icon="list",
        default_index=0,
    )

if not api_key:
    st.warning("Please enter your OpenAI API Key in the sidebar to use the application.")

else:
    if page == "Home":
        st.title("RouteGuru: Your Delivery Route Optimization Assistant")
        st.write("Welcome to RouteGuru, the ultimate delivery route optimization assistant. Designed for parcel delivery drivers, RouteGuru ensures efficient routes, saves time, and enhances customer satisfaction.")

        st.write("## What RouteGuru Does")
        st.write("RouteGuru offers a robust solution for delivery route optimization with the following key features:")
        st.write("- **Route Planning:** Computes the most efficient delivery routes based on input parcel addresses and estimated delivery windows.")
        st.write("- **Geolocation Integration:** Provides precise latitude and longitude details for origins, destinations, and waypoints.")
        st.write("- **Delivery Prioritization:** Ensures that time-sensitive parcels are delivered within the required time windows.")

        st.write("## How It Works")
        st.write("### Delivery Route Optimization")
        st.write("1. **Input Delivery Details:** Provide the addresses of the parcels and their estimated delivery windows.")
        st.write("2. **Optimize Routes:** RouteGuru analyzes the delivery constraints and computes the best route for the day.")
        st.write("3. **Geolocation Details:** Get detailed geolocation coordinates for origins, destinations, and waypoints to use with GPS navigation systems.")

        st.write("## Why Use RouteGuru?")
        st.write("- **Efficiency:** Minimize travel time and fuel consumption with optimized routes.")
        st.write("- **Reliability:** Provides accurate geolocation details to ensure smooth navigation.")
        st.write("- **Delivery Success:** Helps prioritize time-sensitive parcels, improving customer satisfaction.")

        st.write("## Ideal Users")
        st.write("RouteGuru is perfect for:")
        st.write("- Parcel delivery drivers aiming to streamline their daily operations.")
        st.write("- Logistics companies looking for effective route optimization solutions.")
        st.write("- Businesses managing fleets of delivery vehicles in Metro Manila or beyond.")

        st.write("Start using RouteGuru today to simplify your delivery operations and optimize your routes for success!")

        

    elif page == "About Me":
        st.header("About Me")
        st.markdown("""
        Hi! I'm Noela Jean Bunag, a Python Developer and AI Enthusiast. I'm passionate about creating accessible AI solutions and exploring the possibilities of Natural Language Processing.
        
        Connect with me on [LinkedIn](https://www.linkedin.com/in/noela-bunag/) to discuss AI, Python development, or potential collaborations.
        
        Check out my portfolio at [noelabu.github.io](https://noelabu.github.io/) to see more of my projects and work.
        """)

    elif page == "RouteGuru":
        st.header("RouteGuru: Your Delivery Route Optimization Assistant")

        deliveries = []

        if "click_count" not in st.session_state:
            st.session_state.click_count = 1

        def add_delivery_input():
            st.session_state.click_count += 1

        if st.button("➕ Add Delivery Details"):
            add_delivery_input()

        for i in range(st.session_state.click_count):
            delivery_address = st.text_input(f"Enter Delivery Address #{i + 1}:")
            delivery_time_window = st.text_input(f"Enter Delivery Time Window #{i + 1}:")
            deliveries.append(f"{delivery_address} ({delivery_time_window})")
            
        origin_location = st.text_input("Enter the origin location:")

        struct = []
        if st.button("Recommend Route!"):
            structured_prompt = rg.get_structured_prompt(deliveries=deliveries, origin=origin_location)
            resp = rg.route_recommendation(structured_prompt)
            st.session_state.messages.append({"role": "assistant", "content": resp["response"]})
            struct = resp["struct"]

            geo_locations = extract_geolocation(resp["response"])
            gm = GoogleMAP(key=config('GOOGLE_MAPS_API_KEY'))
            gm_source = gm.getEmbededMapsSource(
                origin=geo_locations["origin"],
                destination=geo_locations["destination"],
                waypoints="|".join(geo_locations["waypoints"])
            )
            # Google Maps iframe embed example
            iframe_html = f"""
            <iframe src={gm_source} width="800" height="600"></iframe>
            """

            # Display the iframe in the Streamlit app
            components.html(iframe_html, height=600)
            
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Accept user input
        if st.session_state.messages:
            if prompt := st.chat_input("Are there any more questions?"):
                # Add user message to chat history
                st.session_state.messages.append({"role": "user", "content": prompt})
                # Display user message in chat message container
                with st.chat_message("user"):
                    st.markdown(prompt)
                # Display assistant response in chat message container
                with st.chat_message("assistant"):
                    response = st.write_stream(rg.route_guru_chat(struct, st.session_state.messages))

                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})