import pickle
import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
import category_encoders as ce

model = pickle.load(open("airmodel.pkl","rb"))

scaler = pickle.load(open("scaler.pkl","rb"))

 
page_bg_img = '''
<style>
body {
background-image: url("http://4.bp.blogspot.com/-ULp7Ya5BFUQ/T5prNDFwfVI/AAAAAAAAC7g/uS84hxSssQI/s1600/HDHD.blogspot.com.+%252817%2529.jpg");
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
}
</style>
'''



def input_page():
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown('<h2><b>Airline Passenger Satisfaction</b></h2>', unsafe_allow_html=True)
    
    

    cust_type = st.selectbox('Customer Type', ["Loyal Customer","disloyal Customer"])
        
    age = st.slider('Age', min_value=10, max_value=80)

    
    travel_type= st.selectbox('Type of Travel', ["Personal Travel","Business travel"])
    class_= st.selectbox('Class', ["Business","Eco","Eco Plus"])
    
    flight_dist= st.text_input('Flight Distance', 0)
    
    wifi_service = st.slider('Inflight wifi service', min_value=0, max_value=5)
    ease_ol_book = st.slider('Ease of Online booking', min_value=0, max_value=5)
    food = st.slider('Food and drink', min_value=0, max_value=5)
    ol_boarding = st.slider('Online boarding', min_value=0, max_value=5)
    seat = st.slider('Seat comfort', min_value=0, max_value=5)
    ent = st.slider('Inflight entertainment', min_value=0, max_value=5)
    on_board_service = st.slider('On-board service', min_value=0, max_value=5)
    Leg = st.slider('Leg room service', min_value=0, max_value=5)
    Bagg = st.slider('Baggage handling', min_value=0, max_value=5)
    Checkin = st.slider('Checkin service', min_value=0, max_value=5)
    Inflight_service = st.slider('Inflight service', min_value=0, max_value=5)
    cleanliness = st.slider('Cleanliness', min_value=0, max_value=5)
    
    dept_delay= st.text_input('Departure Delay in Minutes',0)
    arr_delay= st.text_input('Arrival Delay in Minutes', 0)

    
    
    
    

    btn = st.button("Predict")
    
    if btn:
        
        cust_type = Customer_Type_encoder.transform(np.array(cust_type).reshape(-1,1))[0]
        age = scaler.transform(np.array(float(age)).reshape(-1,1))
        travel_type = Type_of_Travel_encoder.transform(np.array(travel_type).reshape(-1,1))[0]
        class_ = Class_encoder.transform(np.array(class_).reshape(-1,1))[0]
        flight_dist = scaler.transform(np.array(float(flight_dist)).reshape(-1,1))
        dept_delay = scaler.transform(np.array(float(dept_delay)).reshape(-1,1))
        arr_delay = scaler.transform(np.array(float(arr_delay)).reshape(-1,1))
    
        test=np.array([[cust_type,age,travel_type,class_,flight_dist,
                       wifi_service,ease_ol_book,food,ol_boarding,seat,
                       ent,on_board_service,Leg,Bagg,Checkin,Inflight_service,
                       cleanliness,dept_delay,arr_delay]])
        test = encoder.fit_transform(test)
        test['Age'] = scaler.transform(np.array(test['Age']).reshape(-1,1))
        test['Flight Distance'] = scaler.transform(np.array(est['Flight Distance']).reshape(-1,1))
        test['Departure Delay in Minutes'] = scaler.transform(np.array(test['Departure Delay in Minutes']).reshape(-1,1))
        test['Arrival Delay in Minutes'] = scaler.transform(np.array(test['Arrival Delay in Minutes']).reshape(-1,1))
        result = model.predict(test)[0]
        if result==0:
            st.markdown('<h4><b>The Passenger was NOT SATISFIED.</b></h4>', unsafe_allow_html=True)

        if result==1:
            st.markdown('<h4><b>The Passenger was SATISFIED.</b></h4>', unsafe_allow_html=True)

        

    
    
input_page()      
    
