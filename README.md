# PowerBI Monitoring Status

## About

A code for monitoring the status off all reports in your workspaces
- Dinamic monitoring of all reports
- Easy configure

## How it works

The program is refresh every 5 minutes and check if the reports have next scheduled hour, if the report has next scheduled hour, it's okay and the status color is "green", else if the status color is "red".


## Installation

PowerBIMonitoringStatus requires [Python](https://www.python.org/) v3 to run.

Install the dependencies.

 - [Chrome Driver](https://chromedriver.chromium.org/downloads)
 - [Azure Theme](https://github.com/rdbende/Azure-ttk-theme)

- [Tkinter]
```sh
pip install tkinter
```
- [Selenium]
```sh
pip install selenium
```

## Tips

#### Building in an exe file

Install the libraries

```sh
pip install pyinstaller
```

Generating the exe file:

- Unique file:
```sh
pyinstaller --noconfirm --onefile --noconsole "'directory'/PowerBI.py"
```

- Unzipped files:
```sh
pyinstaller --noconfirm --noconsole "'directory'/PowerBI.py"
```
## Development

Want to contribute? Great!

## License

**Free Code, Hell Yeah!**

