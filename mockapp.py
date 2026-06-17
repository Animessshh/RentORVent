import streamlit as st
import pandas as pd
import pickle

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="RentORVent",
    page_icon="🏠",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_resource
def load_model():
    with open("Rent_predictor.pkl", "rb") as file:
        model = pickle.load(file)
    return model


@st.cache_data
def load_data():
    return pd.read_csv("Rent_cleaned_data.csv")


model = load_model()
df = load_data()

# =====================================================
# DROPDOWN VALUES
# =====================================================

cities = sorted(df["city"].unique())

property_types = sorted(
    df["property_type"].unique()
)

furnishing_options = sorted(
    df["furnishing"].unique()
)

# =====================================================
# HELPER FUNCTIONS
# =====================================================

def predict_rent(
    locality,
    city,
    area,
    beds,
    bathrooms,
    balconies,
    furnishing,
    property_type
):
    input_df = pd.DataFrame(
        {
            "locality": [locality],
            "city": [city],
            "area": [area],
            "beds": [beds],
            "bathrooms": [bathrooms],
            "balconies": [balconies],
            "furnishing": [furnishing],
            "property_type": [property_type]
        }
    )

    prediction = model.predict(input_df)[0]

    return prediction


def reset_home():
    st.session_state.page = "home"


# =====================================================
# SESSION STATE
# =====================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

# =====================================================
# HOME PAGE
# =====================================================

if st.session_state.page == "home":

    st.title("🏠 RentORVent")

    st.markdown(
        """
        ### Predict. Compare. Decide.

        Whether you're a tenant looking for a fair deal
        or a property owner setting a rental price,
        RentORVent helps you make data-driven decisions.
        """
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🔍 Customer")

        st.write(
            """
            Looking for a property on rent?

            Check whether the quoted rent is fair
            using our ML-powered rent estimator.
            """
        )

        if st.button(
            "I'm Looking For a Rental",
            use_container_width=True
        ):
            st.session_state.page = "customer"
            st.rerun()

    with col2:

        st.subheader("🏢 Property Owner")

        st.write(
            """
            Planning to list your property?

            Estimate the ideal rental price
            using market patterns.
            """
        )

        if st.button(
            "I'm a Property Owner",
            use_container_width=True
        ):
            st.session_state.page = "owner"
            st.rerun()

# =====================================================
# CUSTOMER PAGE
# =====================================================

elif st.session_state.page == "customer":

    st.title("🔍 Rent Fairness Checker")

    if st.button("← Back"):
        reset_home()
        st.rerun()

    st.divider()

    city = st.selectbox(
        "City",
        cities
    )

    filtered_localities = sorted(
        df[df["city"] == city]["locality"].unique()
    )

    locality = st.selectbox(
        "Locality",
        filtered_localities
    )

    col1, col2 = st.columns(2)

    with col1:

        area = st.number_input(
            "Area (sq.ft)",
            min_value=100,
            max_value=10000,
            value=1000
        )

        beds = st.number_input(
            "Bedrooms",
            min_value=1,
            max_value=10,
            value=2
        )

        bathrooms = st.number_input(
            "Bathrooms",
            min_value=1,
            max_value=10,
            value=2
        )

    with col2:

        balconies = st.number_input(
            "Balconies",
            min_value=0,
            max_value=10,
            value=1
        )

        furnishing = st.selectbox(
            "Furnishing",
            furnishing_options
        )

        property_type = st.selectbox(
            "Property Type",
            property_types
        )

    quoted_rent = st.number_input(
        "Quoted Rent by Owner (₹)",
        min_value=0,
        step=1000
    )

    if st.button(
        "Check Fairness",
        use_container_width=True
    ):

        prediction = predict_rent(
            locality,
            city,
            area,
            beds,
            bathrooms,
            balconies,
            furnishing,
            property_type
        )

        st.success(
            f"Predicted Fair Rent: ₹{prediction:,.0f}"
        )

        difference_pct = (
        (quoted_rent - prediction)
        / prediction
        ) * 100

        st.write(
            f"Difference from predicted rent: "
            f"{difference_pct:.2f}%"
)

        if difference_pct > 20:

            st.error(
                "🔴 Significantly Overpriced"
            )

        elif difference_pct > 10:

            st.warning(
                "🟡 Slightly Overpriced"
            )

        elif -10 <= difference_pct <= 10:

            st.success(
                "🟢 Fair Price"
            )

        elif -20 <= difference_pct < -10:

            st.info(
                "🔵 Good Deal"
            )

        elif -40 <= difference_pct < -20:

            st.success(
                "⭐ Excellent Deal"
            )

        else:

            st.warning(
                "⚠️ Unusually Low Price - Verify Property Details"
            )
# =====================================================
# OWNER PAGE
# =====================================================

elif st.session_state.page == "owner":

    st.title("🏢 Rental Price Analyzer")

    if st.button("← Back"):
        reset_home()
        st.rerun()

    st.divider()

    city = st.selectbox(
        "City",
        cities,
        key="owner_city"
    )

    filtered_localities = sorted(
        df[df["city"] == city]["locality"].unique()
    )

    locality = st.selectbox(
        "Locality",
        filtered_localities,
        key="owner_locality"
    )

    col1, col2 = st.columns(2)

    with col1:

        area = st.number_input(
            "Area (sq.ft)",
            min_value=100,
            max_value=10000,
            value=1000,
            key="owner_area"
        )

        beds = st.number_input(
            "Bedrooms",
            min_value=1,
            max_value=10,
            value=2,
            key="owner_beds"
        )

        bathrooms = st.number_input(
            "Bathrooms",
            min_value=1,
            max_value=10,
            value=2,
            key="owner_bathrooms"
        )

    with col2:

        balconies = st.number_input(
            "Balconies",
            min_value=0,
            max_value=10,
            value=1,
            key="owner_balconies"
        )

        furnishing = st.selectbox(
            "Furnishing",
            furnishing_options,
            key="owner_furnishing"
        )

        property_type = st.selectbox(
            "Property Type",
            property_types,
            key="owner_property_type"
        )

    if st.button(
        "Analyse Rent",
        use_container_width=True
    ):

        prediction = predict_rent(
            locality,
            city,
            area,
            beds,
            bathrooms,
            balconies,
            furnishing,
            property_type
        )

        lower = prediction * 0.90
        upper = prediction * 1.10

        st.success(
            f"Recommended Monthly Rent: ₹{prediction:,.0f}"
        )

        st.info(
            f"""
            Suggested Listing Range

            ₹{lower:,.0f}
            to
            ₹{upper:,.0f}
            """
        )

        st.write("### Market Insight")

        st.write(
            f"""
            • Property Type: **{property_type}**

            • Furnishing: **{furnishing}**

            • Area: **{area} sq.ft**

            • Locality: **{locality}**

            Properties with similar characteristics
            are generally expected to rent around
            the recommended range above.
            """
        )