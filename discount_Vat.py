import streamlit as jb
jb.title("แอปพลิเคชั่นคำนวณราคาสินค้า")
price = jb.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0 , value=0.0)
discount = jb.number.input("เปอร์เซ็นส่วนลด (%):", min_value=0.0 , value=0.0)
r_discount = price * (discount/100)
vat = price * 0.07
net_price = price - (vat + r_discount)

st.write(f"• ส่วนลด (discount %): **{discout:.2f}** บาท")
st.write(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
st.divider()
st.write("นางสาวธีชญา แก้วมาเรือน เลขที่40  ม.4/5")
