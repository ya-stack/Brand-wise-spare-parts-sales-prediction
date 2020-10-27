#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pickle
import streamlit as st
pickle_in = open('model.pkl', 'rb') 
regressor = pickle.load(pickle_in) 
  
  
# defining the function which will make the prediction using  
# the data which the user inputs 
def prediction(amount, customer_type, items, order_status, quantity, shipping_state, sku_name, source, warehouse_name, pending_orders, overdue_days):   
   
    prediction = regressor.predict( 
        [[amount, customer_type, items, order_status, quantity, shipping_state, sku_name, source, warehouse_name, pending_orders, overdue_days]]) 
    print(prediction) 
    return prediction 
      
  
#this is the main function in which we define our webpage  
def main(): 
      # giving the webpage a title 
    st.title("Prediction of future sale of Spare Parts") 
      
    # here we define some of the front end elements of the web page like  
    # the font and background color, the padding and the text to be displayed 
    html_temp = """ 
    <div style ="background-color:tomato;padding:13px"> 
    <h1 style ="color:white;text-align:center;">Brand Wise Sales Prediction ML App </h1> 
    </div> 
    """
      
    # this line allows us to display the front end aspects we have  
    # defined in the above code 
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # the following lines create text boxes in which the user can enter  
    # the data required to make the prediction 
    amount = st.text_input("Amount(in cube root)", "Type Here") 
    customer_type = st.text_input("customer_type", "Type Here") 
    items = st.text_input("items", "Type Here") 
    order_status = st.text_input("order_status", "Type Here") 
    quantity = st.text_input("quantity", "Type Here") 
    shipping_state = st.text_input("shipping_state", "Type Here") 
    sku_name = st.text_input("sku_name", "Type Here") 
    source = st.text_input("source", "Type Here") 
    warehouse_name = st.text_input("warehouse_name", "Type Here") 
    pending_orders = st.text_input("pending_orders", "Type Here") 
    overdue_days = st.text_input("overdue_days", "Type Here") 
    result ="" 
      
    # the below line ensures that when the button called 'Predict' is clicked,  
    # the prediction function defined above is called to make the prediction  
    # and store it in the variable result 
    if st.button("Predict"): 
        result = prediction(amount, customer_type, items, order_status, quantity, shipping_state, sku_name, source, warehouse_name, pending_orders, overdue_days) 
    st.success('Predicted future sales for spare parts is (in cube root){}'.format(result))
    if st.button("About"):
        st.text("Developed By Yachna Hasija")

     
if __name__=='__main__': 
    main() 

