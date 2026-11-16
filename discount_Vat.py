import streamlit as jb
jb.title("แอปพลิเคชั่นคำนวณราคาสินค้า")
price = jb.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0 , value=0.0)
discount = jb.number_input("กรอกเปอร์เซ็นส่วนลด (%):", min_value=0.0 , value=0.0)

r_discount = price * (discount/100)
dis_price = price - r_discount
vat = dis_price * 0.07
net_price = dis_price + vat

jb.write(f"• ส่วนลด ({discount}%) : -**{r_discount:.2f}** บาท")
jb.write(f"• ราคาหลังส่วนลด: {dis_price:.2f} บาท")
jb.write(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): +**{vat:.2f}** บาท")
jb.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
jb.divider()
jb.write("นางสาวธีชญา แก้วมาเรือน เลขที่40  ม.4/5")
