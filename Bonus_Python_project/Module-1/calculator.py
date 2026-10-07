import streamlit as st
st.header("Calculator")
st.divider()
num1=st.number_input("Enter a Number: ",value=None,placeholder="type number one",key="n")
num2=st.number_input("Enter a Number: ",value=None,placeholder="type number one",key="m")
select=st.selectbox("Choose Operation",['+','-','*','/'],index=None)
result=st.button("Result",type="primary")

if result:
    if num1 and num2:
        st.write("Successfully Input two Numbers")

        if select=="+":
            sum=num1+num2
            st.write(f"The Sum is : {sum}")
        elif select=="-":
            sub=num1-num2
            st.write(f"The Sum is : {sub}")
        elif select=="*":
            mul=num1*num2
            st.write(f"The Sum is : {mul}")
        elif select=="/":
            div=num1/num2
            st.write(f"The Sum is : {div}")
        else:
            st.warning("No operator Selected")
    else:
        st.error("Enter Numbers Properly")

        

    