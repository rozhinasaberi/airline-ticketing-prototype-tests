import streamlit as st


BUSINESS_PRICE = 750.0
ECONOMY_PRICE = 500.0


def seat_label(row: int, letter: str) -> str:
    return f"{row}{letter}"


st.set_page_config(page_title="Airline Ticketing Tutor", page_icon="🧪", layout="wide")

st.title("🧪 Airline Ticketing Test Tutor")
st.write(
    "This tutor-style app explains the airline ticketing prototype by walking through "
    "pricing, discounts, seat assignment, and the kinds of checks a JUnit test would verify."
)

tab1, tab2, tab3 = st.tabs(["Pricing Rules", "Seat Assignment", "Test Thinking"])

with tab1:
    st.subheader("Ticket Pricing")
    passenger_type = st.selectbox("Passenger type", ["Standard Passenger", "Frequent Flyer", "Staff Passenger"])
    seating_class = st.selectbox("Seating class", ["BUSINESS", "ECONOMY"])
    base_price = BUSINESS_PRICE if seating_class == "BUSINESS" else ECONOMY_PRICE
    final_price = base_price / 2 if passenger_type == "Staff Passenger" else base_price

    st.metric("Base fare", f"${base_price:.2f}")
    st.metric("Final fare", f"${final_price:.2f}")

    if passenger_type == "Staff Passenger":
        st.info("Staff passengers implement the discount behavior in the Java version, so the ticket price is cut in half.")
    elif passenger_type == "Frequent Flyer":
        st.info("Frequent flyers store a membership ID, but in this version they keep the regular ticket price.")
    else:
        st.info("Standard passengers pay the regular fare for the seating class they choose.")

with tab2:
    st.subheader("Seat Assignment Logic")
    sold_business = st.slider("Business seats already sold", 0, 2, 1)
    sold_economy = st.slider("Economy seats already sold", 0, 12, 4)
    requested_class = st.radio("Requested class", ["BUSINESS", "ECONOMY"], horizontal=True)

    if requested_class == "BUSINESS":
        total = 2
        sold = sold_business
        rows = ["1A", "1B"]
    else:
        total = 12
        sold = sold_economy
        rows = ["2A", "2B", "2C", "2D", "3A", "3B", "3C", "3D", "4A", "4B", "4C", "4D"]

    available = rows[sold:]
    if available:
        st.success(f"First guaranteed fallback seat: {available[0]}")
        st.write(
            "The Java project first tries a random seat in the requested section; if that seat is taken, "
            "it falls back to the first open seat in that section."
        )
    else:
        st.error("That seating section is sold out.")

    st.write(f"Seats sold: {sold}/{total}")

with tab3:
    st.subheader("How To Test This System")
    scenario = st.selectbox(
        "Choose a test idea",
        [
            "Staff discount is applied",
            "Frequent flyer keeps full fare",
            "Random seat fallback finds first open seat",
            "Sold-out section blocks ticket issuance",
        ],
    )

    explanations = {
        "Staff discount is applied": "Create a staff passenger, issue a business-class ticket, and assert that the final price is $375 instead of $750.",
        "Frequent flyer keeps full fare": "Create a frequent flyer passenger and verify that the stored ID changes the passenger type but not the ticket price.",
        "Random seat fallback finds first open seat": "Fill a few seats, simulate a duplicate random pick, and verify that the first open seat in that section is assigned next.",
        "Sold-out section blocks ticket issuance": "Pre-fill every seat in a section and verify that the sale method returns failure instead of creating a ticket.",
    }
    st.code(explanations[scenario], language="text")
    st.caption("This app is a teaching layer over the original Java prototype and test scaffold.")
