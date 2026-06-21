# Register Employee Bot 

บอทสำหรับเพิ่มพนักงาน บนเว็บไซต์ [https://jarvizweb.jarvizapp.com](https://jarvizweb.jarvizapp.com)  
โดยใช้ข้อมูลจากไฟล์ Excel 

1. **Selenium + Excel** : `bot_selenium_jarviz.js`
2. **Playwright + Excel** (รันแบบ back-end, headless) : `bot_playwright_jarviz.js`
> ตัวอย่างการรันบอทด้วย Playwright:
>```bash
> node bot_playwright_jarviz.js

---


## Feature

- อ่านข้อมูลพนักงานจากไฟล์ `.xlsx`
- เปิดเบราว์เซอร์อัตโนมัติ
- ล็อกอินเข้าสู่ระบบ
- เข้าหน้า User Management
- เพิ่มพนักงานทีละคน
- กดปุ่ม OK หากมี alert แจ้ง "Add successfully"


## ตัวอย่างไฟล์ jarviz_test.xlsx

| emp_id | full_name   | email              | position     | phone      |
|--------|-------------|--------------------|--------------|------------|
| 10001  | John Smith  | john@example.com   | Developer    | 0812345678 |
| 10002  | Jane Doe    | jane@example.com   | UX Designer  | 0899999999 |



## ข้อมูลที่ต้องแก้ไข
- Excel path
#### หน้า Log in
- Company Code
- UserID
- Password

-------------------------------------------------------------------------------

# Register Employee Bot

An automation bot for adding employees to the Jarviz User Management system at: https://jarvizweb.jarvizapp.com

The bot reads employee information from an Excel file and automatically creates user accounts in the system.

## Available Versions

1. **Selenium + Excel**

   * `bot_selenium_jarviz.js`

2. **Playwright + Excel** (Backend / Headless Mode)

   * `bot_playwright_jarviz.js`

### Example: Run the Playwright Bot

```bash
node bot_playwright_jarviz.js
```

---

## Features

* Read employee information from an Excel (`.xlsx`) file
* Automatically launch a browser session
* Log in to the Jarviz system
* Navigate to the User Management page
* Create employee accounts one by one
* Automatically click the **OK** button when the success message ("Add successfully") appears


## Sample Excel File (`jarviz_test.xlsx`)

| emp_id | full_name  | email                                       | position    | phone      |
| ------ | ---------- | ------------------------------------------- | ----------- | ---------- |
| 10001  | John Smith | [john@example.com](mailto:john@example.com) | Developer   | 0812345678 |
| 10002  | Jane Doe   | [jane@example.com](mailto:jane@example.com) | UX Designer | 0899999999 |


## Required Configuration

Before running the bot, update the following settings in the script:

### Excel File

* Excel file path (`.xlsx`)

### Login Credentials

* Company Code
* User ID
* Password


## Prerequisites

### Node.js

Install Node.js (version 18 or later recommended).

### Required Packages

For Selenium version:

```bash
npm install selenium-webdriver xlsx chromedriver
```

For Playwright version:

```bash
npm install playwright xlsx
```


## How It Works

1. Read employee data from the Excel file.
2. Open the Jarviz login page.
3. Sign in using the configured credentials.
4. Navigate to **User Management**.
5. Create employee records using data from Excel.
6. Detect the success popup message.
7. Click **OK** and continue with the next employee.
8. Repeat until all records have been processed.


## Notes

* Ensure the Excel file format matches the expected column names.
* Verify that the login credentials have permission to access the User Management module.
* The Playwright version can run in headless mode, making it suitable for server-side automation and scheduled jobs.
* It is recommended to test with a small dataset before processing a large number of employee records.


## Disclaimer

This automation tool is intended for authorized use only. Ensure that you have permission to create and manage user accounts within the Jarviz system before running the bot.

