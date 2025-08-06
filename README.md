# 🏠 E2E Automated Test for Publishing a Property Ad on homme.co.il

This project contains an end-to-end (E2E) test written in Python using [Playwright](https://playwright.dev/python/) for automating the process of publishing a real estate ad on [https://homme.co.il](https://homme.co.il).

## 📸 What It Does

The test script mimics a real user publishing a property listing. It performs the following steps:

1. Navigates to the site and accepts terms of service.
2. Logs in with credentials from environment variables.
3. Fills in all the steps of the ad publishing form:
   - Basic details
   - Property info
   - Features and description
   - Payment details
   - Uploads an image
   - Contact information
4. Publishes the ad.
5. Verifies the ad was added to the user's stock.

## 📂 Project Structure

.
├── main_test.py # Main E2E test file
├── helpers/ # Helper functions for each form step
│ └── ... # fill_step_one_form, login, etc.
├── files/
│ ├── ad_photo.png # Test image used for uploading
│ └── screenshots/
│ └── success.png # Screenshot after submission
├── .env # Stores sensitive credentials (optional)
└── README.md

bash

## ⚙️ Requirements

- Python 3.8+
- [Playwright for Python](https://playwright.dev/python/)
- [Loguru](https://github.com/Delgan/loguru)

## 📦 Installation

```bash
# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install playwright loguru python-dotenv

# Install browser drivers
playwright install
🔐 Environment Variables
Create a .env file or set the following variables in your shell:

env
HOMME_EMAIL=your_email@example.com
HOMME_PASSWORD=your_password
Or export them directly in the terminal:

bash
export HOMME_EMAIL=your_email@example.com
export HOMME_PASSWORD=your_password
▶️ Run the Test
bash
python main_test.py
The browser will open (not headless), navigate through the site, fill in the forms, and complete the ad publishing flow.

🧪 Features Covered
Full multi-step form automation

Hebrew UI element targeting

Dynamic selectors

Screenshot capture

Assertion of final outcome

🧰 Tech Stack
Python

Playwright (sync API)

Loguru for logging

📸 Screenshot Output
A screenshot of the success message after publishing is saved at:

bash
./files/screenshots/success.png
👤 Author
Eliram Shemesh
QA Automation Engineer

Feel free to open an issue or contribute improvements!

Let me know if you'd like a version in Hebrew, or tailored for Pytest test runners.

Ask ChatGPT
