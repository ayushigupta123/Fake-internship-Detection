

import streamlit as st
import fake_file as fk
import real_company as rc





# Create input fields
name = st.text_input("ComapnyName:")


email = st.text_input(" Company Email:")

if name and email:
    c=rc.check(name,email)


description = st.text_input("Description:")
if description:
    d = fk.faker(description)
    

# Create button
button = st.button("Submit")

# Define output
output = None

# Handle button click event
if button:
    # Validate input fields
    warnings = []
    if not name:
        warnings.append("Please enter a Company name.\n")
    if not email:
        warnings.append("Please enter an Company email.\n")
    if not description:
        warnings.append("Please enter an Description.\n")
    if warnings:
        # Display all warnings together
        st.warning("\n".join(warnings))
    
    else:
        # Perform some operation with the validated inputs
        # Here, we concatenate the inputs into a single string
        if c==True:
            if d==True:
                output="This is real internship"
            
        else:
            output ="This is fake internship"

# Display output
if output:
    st.write("Output:")
    st.write(output)
