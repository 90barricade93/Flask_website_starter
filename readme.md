# Flask Website README

This repository contains the necessary files to build a Flask website with a home and about page.

## The purpose of this repository is to quickly create a Flask website with a home and about page to get you started on your project.

## Getting Started

To get started, clone this repository to your local machine:

``` git clone '' ```

Then, create a virtual environment in the root directory of the project:

``` python3 -m venv env ```

Activate the virtual environment:

``` source env/bin/activate ```

Install the required packages:

``` pip install -r requirements.txt ```

## Running the Website

Then run the following command:

```
python main.py
```

This will start the Flask development server, and you should be able to view the website by navigating to `http://localhost:5000/` in your web browser.

## File Structure

- `main.py`: The main Flask application file, containing the routing and logic for the website.
- `templates/`: The directory containing the Jinja2 templates for the website.
  - `home.html`: The template for the home page.
  - `about.html`: The template for the about page.
- `static/css/`: The directory containing the CSS file for styling the website.
  - `style.css`: The CSS file for styling the website.

## CSS Styling

The website is styled using the `style.css` file located in the `static/css/` directory. The CSS defines styles for the header, body, and content areas of the website. You can modify the styles in this file to customize the look and feel of your website.

## License

This project is licensed under the CC3 License - see the [https://creativecommons.org/licenses/by/3.0/] for details.