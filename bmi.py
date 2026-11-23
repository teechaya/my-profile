import streamlit as sd
sd.title("💪 โปรแกรมคำนวณค่าดัชนีมวลกาย (BMI) ️‍🔥")
weight = sd.number_input("กรอกน้ำหนัก (กิโลกรัม) : ", min_value = 1.0, value=1.0)
height_cm = sd.number_input("กรอกส่วนสูง (cm) : ", min_value = 1.0, value=1.0)

if sd.button("คำนวณค่า BMI ")
   height_m = height_cm / 100
   bmi = weight / (height ** 2)

   sd.write("---")
   sd.header("ค่า bmi ของคุณคือ: **{bmi:.2f}**")

if bmi > 18.5:
  sd.warning("⚠️ คุณน้ำหนักน้อยกว่าเกณฑ์!! (ผอม)")
elif 18.5 <= bmi < 23.0:
  sd.success("💪 คุณมีน้ำหนักในเกณฑ์ปกติ (สมส่วน)")
elif 23.0 <= bmi < 25.0:
  sd.info("🚨 คุณเริ่มมีน้ำหนักเกินเกณฑ์ (ท้วม)")
else:
  sd.error("คุณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพและหมั่นออกกำลังกาย 🏋️")

sd.divider()
sd.write("นางสาว ธีชญา แก้วมาเรือน เลขที่ 40 ม.4/5")
