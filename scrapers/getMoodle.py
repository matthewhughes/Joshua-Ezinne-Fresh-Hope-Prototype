#!/usr/bin/env python
import requests

def main():
    HopeHomepage = requests.get("https://moodle.hope.ac.uk/login/index.php")
    print(HopeHomepage.content)

if __name__ == '__main__':
    main()
