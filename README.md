# Register Employees Bot 

บอทสำหรับเพิ่มพนักงานใหม่ (New Employee) บนเว็บไซต์ [https://jarvizweb.jarvizapp.com](https://jarvizweb.jarvizapp.com)  
โดยใช้ข้อมูลจากไฟล์ Excel 

1. **Selenium + Excel**
2. **Playwright + Excel** (รันแบบ back-end, headless)
> ตัวอย่างการรันบอทด้วย Playwright:
node jarviz_bot.js

## Feature

- อ่านข้อมูลพนักงานจากไฟล์ `.xlsx`
- เปิดเบราว์เซอร์อัตโนมัติ
- ล็อกอินเข้าสู่ระบบ
- เข้าหน้า User Management
- เพิ่มพนักงานทีละคน
- กดปุ่ม OK หากมี alert แจ้ง "Add successfully"

---

## ตัวอย่างไฟล์ jarviz_test.xlsx

emp_id	full_name	email	position	phone
10001	John Smith	john@example.com	Developer	0812345678
10002	Jane Doe	jane@example.com	UX Designer	0899999999

## ข้อมูลที่ต้องแก้ไข
หน้า Log in
- Company Code
- UserID
- Password
