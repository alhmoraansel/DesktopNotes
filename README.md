# DesktopNotes

Make Rainmeter INI file for creating custom notes using this script. This tool provides a graphical user interface (GUI) to easily generate Rainmeter skins for displaying customizable notes on your desktop.

## Features and Functionality

*   **GUI Interface:** User-friendly Tkinter-based GUI for easy note creation.
*   **Note Title and Text:** Allows users to specify a title and the main text content of the note.
*   **Font Customization:** Users can select font face, size, and color.  Supports all fonts available on the system.
*   **Anti-Aliasing:** Option to enable or disable anti-aliasing for smoother text rendering.
*   **INI File Generation:** Generates a Rainmeter-compatible `.ini` file based on the user's configurations.
*   **Load/Save Functionality:** Load settings from existing `.ini` files, and saves the file path to a text file for future use.
*   **Color Picker:** Integrated color picker for selecting the desired font color.
*   **Automatic Last File Load:** Remembers the last used `.ini` file and loads it on startup.

## Technology Stack

*   **Python:** Primary programming language.
*   **Tkinter:** GUI toolkit for creating the user interface.
*   **ttk (Themed Tkinter):** Provides enhanced styling for Tkinter widgets.
*   **configparser:** Used for reading and parsing Rainmeter INI files when loading.

## Prerequisites

*   **Python 3.x:**  Make sure you have Python 3 installed on your system.
*   **Rainmeter:** This tool is designed to create skins for Rainmeter, so Rainmeter must be installed to use the generated `.ini` files.  Download it from [https://www.rainmeter.net/](https://www.rainmeter.net/).

## Installation Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/alhmoraansel/DesktopNotes.git
    cd DesktopNotes
    ```

2.  **Run the script:**

    ```bash
    python make.py
    ```

    This will launch the Rainmeter Note Generator GUI.

## Usage Guide

1.  **Launch the application:** Run `python make.py`.

2.  **Enter Note Details:**
    *   **Note Title:** Enter the title of your note in the "Note Title" field.
    *   **Note Text:** Enter the content of your note in the "Note Text" text area.  Newlines will be converted to spaces in the generated `.ini` file.
    *   **Font:** Select the desired font from the "Font" dropdown menu.  The list includes all available fonts on your system.
    *   **Font Size:** Enter the font size in the "Font Size" field.  A default value of '14' is provided.
    *   **Font Color:** Click the "Choose Color" button to select the desired font color using the color picker.
    *   **Anti-Aliasing:** Check the "Enable Anti-Aliasing" checkbox to enable anti-aliasing for the text.

3.  **Export to INI:** Click the "Export to INI" button to save the Rainmeter skin configuration to a `.ini` file.  You'll be prompted to choose a file name and location. The suggested name defaults to `[Note Title].ini`.

4.  **Load from INI:** Click the "Load from INI" button to load settings from an existing Rainmeter `.ini` file. The tool looks for the `TitleText`, `NoteText`, `FontFace`, `FontSize`, `FontColor`, and `AntiAlias` variables within the `[Variables]` section of the `.ini` file.

5.  **Using the generated INI file with Rainmeter:**
    *   Copy the generated `.ini` file to your Rainmeter skins folder (usually located in `Documents\Rainmeter\Skins`).
    *   Refresh Rainmeter.
    *   Load the skin from the Rainmeter Manage window.

## API Documentation

This project does not expose a public API.  The script is designed to be run as a standalone GUI application.

## Contributing Guidelines

Contributions are welcome! Here's how you can contribute:

1.  **Fork the repository.**
2.  **Create a new branch for your feature or bug fix.**
3.  **Implement your changes.**
4.  **Submit a pull request with a clear description of your changes.**

## License Information

No license is specified for this project. All rights are reserved by the author.

## Contact/Support Information

For questions, issues, or support, please contact the repository owner through GitHub.  You can open an issue on the GitHub repository: [https://github.com/alhmoraansel/DesktopNotes](https://github.com/alhmoraansel/DesktopNotes)