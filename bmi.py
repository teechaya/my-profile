import streamlit as sd
sd.markdown("# :violet[💪โปรแกรมคำนวณค่าดัชนีมวลกาย BMI]")
sd.write("กรอกข้อมูลน้ำหนักส่วนสูงของคุณ เพื่อเช็คสุขภาพเบื้องต้น")
weight = sd.number_input("กรอกน้ำหนัก (กิโลกรัม) : ", min_value = 1.0, value=1.0)
height_cm = sd.number_input("กรอกส่วนสูง (cm) : ", min_value = 1.0, value=1.0)
 
if sd.button("คำนวณค่า BMI "):
   height_m = height_cm / 100
   bmi = weight / (height_m ** 2)

   if bmi < 18.5:
     sd.warning("⚠️ คุณน้ำหนักน้อยกว่าเกณฑ์!! (ผอม)")
   elif 18.5 <= bmi < 23.0:
     sd.success("💪 คุณมีน้ำหนักในเกณฑ์ปกติ (สมส่วน)")
   elif 23.0 <= bmi < 25.0:
     sd.info("🚨 คุณเริ่มมีน้ำหนักเกินเกณฑ์ (ท้วม)")
   else:
     sd.error("คุณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพและหมั่นออกกำลังกาย 🏋️")

   sd.write("---")
   sd.header(f"ค่า bmi ของคุณคือ: **{bmi:.2f}**")
   
sd.divider()
sd.write("นางสาว ธีชญา แก้วมาเรือน เลขที่ 40 ม.4/5")
