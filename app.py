import streamlit as st

def main():
    st.title("Digital Twin Add-on Selector for SMEs")
    
    # Step 1: Business Size
    size = st.selectbox("Select your business size:", ["Small (1-10 employees)", "Medium (11-100 employees)", "Large (100+ employees)"])
    
    # Step 2: Maintenance Priorities
    reliability = st.checkbox("Reliability is important (Avoid failures)")
    availability = st.checkbox("Availability is important (Maximize uptime)")
    maintainability = st.checkbox("Maintainability is important (Ease of repairs)")
    sustainability = st.checkbox("Sustainability is important (Eco-friendly maintenance)")
    
    # Step 3: Technical Considerations
    cloud_required = st.radio("Do you require a cloud-based solution?", ["Yes", "No"])
    security_level = st.radio("How critical is data privacy & security?", ["Low", "Medium", "High"])
    scalability = st.radio("How scalable should your system be?", ["Low", "Medium", "High"])
    
    # Step 4: Budget & Maintenance Type
    budget = st.radio("Budget for maintenance:", ["Low", "Medium", "High"])
    maintenance_type = st.selectbox("Type of maintenance strategy:", ["Reactive", "Preventive", "Predictive", "Prescriptive"])
    
    # Step 5: Decision Output
    st.subheader("Recommended Add-ons Based on Your Selection:")
    recommendations = []
    
    if reliability:
        recommendations.append("Predictive Maintenance, Advanced IoT Integration")
    if availability:
        recommendations.append("Big Data Processing, Automated Workflows")
    if maintainability:
        recommendations.append("AI-driven Data Analytics, Preventive Maintenance")
    if sustainability:
        recommendations.append("Carbon Footprint Tracking, Eco-Friendly Optimization")
    if cloud_required == "Yes":
        recommendations.append("Hybrid Cloud Deployment, API for Future Add-ons")
    if security_level == "High":
        recommendations.append("Advanced Cybersecurity, Blockchain for Secure Data Logs")
    if scalability == "High":
        recommendations.append("Scalable AI & IoT Infrastructure, Modular System Design")
    if budget == "Low":
        recommendations.append("Start with Core System, Add Predictive Maintenance if feasible")
    if maintenance_type == "Reactive":
        recommendations.append("Core System Only")
    elif maintenance_type in ["Preventive", "Predictive", "Prescriptive"]:
        recommendations.append("IoT, AI-driven Analytics, Advanced Decision Support")
    
    if recommendations:
        for rec in recommendations:
            st.write(f"- {rec}")
    else:
        st.write("Based on your inputs, the core system is sufficient for your needs.")

if __name__ == "__main__":
    main()
