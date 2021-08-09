# PowerBI Monitoring Status

## About

A code for monitoring the status of all reports in your workspaces
- Dinamic monitoring of all reports
- Easy configure

## How it works

The program is refresh every 5 minutes and check if the reports has next scheduled hour. If the report has next scheduled hour, it's okay and the status color is "green", else if the status color is "red".


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

## Print

![PBIStatus](https://user-images.githubusercontent.com/77687020/128714649-77c1f42a-5884-4ecb-98f0-61789a647910.png)


