Childhood Autism Rating Scale (CARS) Web App
This web application provides a user-friendly interface for administering and scoring the Childhood Autism Rating Scale (CARS). It is built using Dash, a Python library for creating interactive web dashboards.

Features
Easy-to-follow interface for navigating through CARS items.
Option to save and load partially completed assessments.
Automatic scoring based on user selections.
Clear presentation of final scores.

Installation
Requirements:
See requirements.txt

Running the App:

Clone this repository or download the files.
Open a terminal in the project directory.
Run the following command:

Bash

python src/app.py

This will launch the web app in your default browser, typically at http://127.0.0.1:8050/.

Usage
The web app guides you through each CARS item with clear instructions and radio buttons for selecting the appropriate response. You can navigate forward and backward through the items using the provided buttons.

Saving and Loading: During an assessment, you can save your progress by clicking the "Save" button. This will store your selections in local storage. To resume a saved assessment, click the "Upload" button and select the saved file.

Scoring: As you make selections, the app automatically calculates the score in the background. The final score is displayed iteractively in the Results tab.

Disclaimer
Important Note: This web app is intended only for professional psychologists to use. 

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
We welcome contributions to improve this web app! If you have suggestions or bug fixes, feel free to fork the repository and submit a pull request.

![](https://github.com/llazzari/cars/blob/main/cars.gif)
