# selenium_grid_test

 
# requirements

python 
selenium module (installation command - pip install selenium)
browser - Firefox
geckodriver
    -place the geckodriver.exe file in virtual environment path
    -//env/Scripts/geckodriver.exe
    
pytest -s -v -n=2 --html=reports\header_report.html testcases/headers_test.py --browser firefox