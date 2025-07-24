const { chromium } = require('playwright');
const XLSX = require('xlsx');

(async () => {
  // STEP 1: อ่านข้อมูล Excel
  const workbook = XLSX.readFile('/Users/Documents/jarviz_test.xlsx');  // Excel path
  const sheet = workbook.Sheets[workbook.SheetNames[0]];
  const data = XLSX.utils.sheet_to_json(sheet);

  // STEP 2: เปิด browser
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  // STEP 3: Login
  await page.goto('https://jarvizweb.jarvizapp.com/login');  // Web link
  await page.fill('#input-19', 'Company_Code');  // Your Company Code
  await page.fill('#input-22', 'UserID');  // Your UserID
  await page.fill('#input-25', 'Password');  // Your Passwword
  await page.click('text=Login');
  await page.waitForTimeout(3000);

  // STEP 4: เข้าหน้า user management
  await page.goto('https://jarvizweb.jarvizapp.com/dashborad/users');
  await page.waitForTimeout(2000);

  page.on('dialog', async dialog => {
    console.log('Alert:', dialog.message());
    await dialog.accept();
  });

  // STEP 5: Loop เพิ่มพนักงานจาก Excel
  for (const emp of data) {
    await page.click('button:has-text("New Employee")');

    await page.fill('#inputEmpID', String(emp.emp_id));
    const inputs = await page.$$('input.form-control');

    await inputs[1].fill(emp.full_name);       // Full Name
    await page.fill('#inputEmail', emp.email);   // Email
    await inputs[3].fill(emp.position);        // Position
    await page.fill('#inputphoneno', String(emp.phone));  // Phone no
    await page.fill('#inputuID', String(emp.emp_id));  // UserID

    await page.click('button:has-text("Add")');

    await page.waitForTimeout(1000);
  }

  await browser.close();
})();
