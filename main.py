import argparse
import os
import time
from datetime import datetime
from browser import determine_browser
from extractor import Extractor
from println import println

driver = None
arguments = argparse.ArgumentParser()

arguments.add_argument('--start', action='store', type=int, required=False, default=0, help="What page would you like us to start scrape from Google's search result")
arguments.add_argument('--stop', action='store', type=int, required=False, default=14, help="At what page would you want to stop scraping Google's search result")
arguments.add_argument('--file', action='store', type=str, required=False, help="File name to save extracted data")
arguments.add_argument('--browser', action='store', type=str, required=False, default="chrome", help="What browser should we scrape with?")
arguments.add_argument('--driver', action='store', type=str, required=False, help="Browser executable path")

args = arguments.parse_args()

def main():
    executor_url = ""
    session_id = ""
    selected_browser = args.browser
    browser_driver_path = args.driver
    query = os.getenv('QUERY')  # Read from environment variable
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = args.file or f"data_{timestamp}.txt"
    start_page = args.start - 1
    stop_page = args.stop - 1

    # Wait until QUERY environment variable is set
    while not query:
        println("Waiting for query to be provided...", "normal")
        time.sleep(5)
        query = os.getenv('QUERY')

    if start_page < 0:
        start_page = 0  # If the user puts in 0, we auto make it one
    elif (stop_page - start_page) > 15:
        println("You cannot search more than 15 pages at a time")

    # Determine what browser to use for this tool
    driver = determine_browser(selected_browser, browser_driver_path)
    if type(driver) == str:
        println(driver)
    else:
        executor_url = driver.command_executor._url
        session_id = driver.session_id

        # Maximize chrome height to highest
        driver.set_window_size(1920, 8000)

        println(f"Google's Query: {query}", "normal")
        extractor = Extractor(driver, query, start_page, stop_page, file_name)
        driver.close()

try:
    main()
except Exception as e:
    println("Oops, something's off here", "fail")
