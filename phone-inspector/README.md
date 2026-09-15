# Phone Inspector

A lightweight Python command-line utility for inspecting phone-number metadata using the `phonenumbers` library.

## Features

* International phone-number parsing
* Number validity checking
* Possible-number checking
* Country code detection
* Region detection
* Carrier information when available
* Geographic description when available
* Associated time-zone information
* Cross-platform terminal interface
* Clean error handling
* No automatic package installation
* No phone numbers are stored or logged

## Requirements

* Python 3.9 or newer
* Internet access is not required for the basic `phonenumbers` database operations after the package has been installed.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/phone-inspector.git
cd phone-inspector
```

Create a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Start the application:

```bash
python app.py
```

Enter a phone number using international format.

Example:

```text
+919876543210
```

The application can display:

* Internationally formatted number
* Country calling code
* Region
* Carrier information
* Geographic description
* Time zones
* Whether the number is valid
* Whether the number is potentially possible

## Example

```text
╔══════════════════════════════════════════════════════╗
║                                                      ║
║              P H O N E   I N S P E C T O R           ║
║                                                      ║
║       Lightweight phone-number metadata utility      ║
║                                                      ║
╚══════════════════════════════════════════════════════╝

Phone number > +919876543210

──── Analysis ────
International     +91 98765 43210
Country code      +91
Region            IN
Carrier           ...
Location          ...
Time zone         Asia/Calcutta
Valid number      VALID
Possible number   YES
──────────────────
```

The exact metadata depends on the information available in the underlying `phonenumbers` database.

## Important limitations

This tool does **not**:

* reveal a person's live location
* track a phone
* access private subscriber information
* identify the owner of a number
* retrieve SMS messages or call records
* bypass telecom-provider systems

Carrier and geographic information may also be unavailable, outdated, or different from the current network/location of the number.

## Privacy

Phone numbers entered into the application are processed locally by the program.

The application does not intentionally save submitted phone numbers to files, databases, or logs.

Do not modify the project to collect or publish other people's phone numbers without appropriate authorization.

## License

MIT License

Copyright (c) 2026 YOUR_NAME

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, subject to the conditions of the MIT License.
