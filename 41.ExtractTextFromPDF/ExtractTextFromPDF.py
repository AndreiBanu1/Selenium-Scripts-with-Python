from io import BytesIO
from urllib.request import urlopen
from pdfminer.high_level import extract_text
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

class PdfReader:

    def setUp(self):
        options = Options()
        options.headless = True
        self.service = Service('path/to/chromedriver')
        self.driver = webdriver.Chrome(service=self.service, options=options)

    def test_print_pdf_text(self):
        self.driver.get('https://file-examples.com/wp-content/uploads/2017/10/file-sample_150kB.pdf')
        self.driver.maximize_window()

        # Wait for the PDF to load
        time.sleep(5)

        # Get PDF content as bytes and extract text
        pdf_bytes = urlopen(self.driver.current_url).read()
        output = extract_text(BytesIO(pdf_bytes))

        print('PDF Content:\n', output)

    def tearDown(self):
        self.driver.quit()
        self.service.stop()
