import streamlit as st
import pandas as pd
import random
import time

# Title
st.title("IoT Sensor Dashboard")

# Create empty dataframe
data = pd.DataFrame(columns=["Temperature", "Humidity"])

# Placeholder
chart = st.line_chart(data)

# Table placeholder
table = st.empty()

# Motion placeholder
motion_text = st.empty()

# Simulate live data
for i in range(20):

    # Random sensor values
    temperature = random.randint(25, 35)
    humidity = random.randint(40, 70)
    motion = random.choice(["Detected", "No Motion"])

    # Add data
    new_data = pd.DataFrame({
        "Temperature": [temperature],
        "Humidity": [humidity]
    })

    data = pd.concat([data, new_data], ignore_index=True)

    # Update chart
    chart.line_chart(data)

    # Update table
    table.dataframe(data)

    # Motion display
    motion_text.write(f"Motion Status: {motion}")

    # Delay
    time.sleep(2)