# selenium testing for amazon website -header and footer links validation

## required python packages
### run below commands in either venv or cmd.

- **selenium** 
    > pip install selenium
- **pytest**
    > pip install pytest
- **pytest-html**
    > pip install pytest_html
- **pytest-xdist**
    > pip install pytest-xdist
- **openpyxl**
    > pip install openpyxl
- **pandas**
    > pip install pandas

## drivers required
- **geckodriver** - *firefox*  
- **MicrosoftWebdriver** - *edge*
- **IEDriverServer** - *Internet Explorer*

`place all the driver's exe file in scripts folder of python environment`

## commands to run the script

This command is to run test in parallel in firefox and generate html report
- command -n=2 for  to run 2 test in parallel
>  pytest -s -v -n=2 --html=reports\header_report.html testcases/headers_test.py --browser firefox


this command is to run sequentially (non-parallel) in edge browser
- command --html= for genrating html file
- command --browser for browser specification
>  pytest -s -v --html=reports\header_report.html testcases/headers_test.py --browser edge


additional browsers and drivers can be added in siteconfig.py file


## Reports
    
### Reports folder

- **html reports** 
- **excel reports**
