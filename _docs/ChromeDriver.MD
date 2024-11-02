Version 130.0.6723.92 (Official Build) (64-bit)

The path to your ChromeDriver depends on where you have downloaded and saved the ChromeDriver executable on your system. Here are the steps to find and set the path:

1. **Download ChromeDriver**:
   If you haven't already, download ChromeDriver from the official site: [ChromeDriver Download](https://sites.google.com/a/chromium.org/chromedriver/downloads)

2. **Extract and save ChromeDriver**:
   Extract the downloaded file and save the `chromedriver.exe` to a directory on your system. For example, you might save it to `C:\WebDriver\bin\chromedriver.exe`.

3. **Set the path in your script**:
   Update the path in your script to point to the location where you saved `chromedriver.exe`.

Here is how you can update the path in your script:

```python
# Set up the WebDriver
service = Service('C:\\WebDriver\\bin\\chromedriver.exe')  # Change this to the path of your chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)
```

Make sure to use double backslashes (

HealthcareReportDownloader

) in the path if you are on Windows.