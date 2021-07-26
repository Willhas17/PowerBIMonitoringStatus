# PowerBIMonitoringStatus

A code for monitoring the staus off all reports in your workspace
- Dinamic monitoring of all reports
- Easy configure

## Installation

PowerBIMonitoringStatus requires [Python](https://www.python.org/) v3 to run.

Install the dependencies.

 - [Chrome Driver](https://chromedriver.chromium.org/downloads)
 - [Azure Theme](https://github.com/rdbende/Azure-ttk-theme)



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

