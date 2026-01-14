# Astrolizer

#### Video Demo: <url>

## Description:

An app written in **PYTHON** that helps users identify what they can see in the sky, regardless of their location in the world or the date! If you are curious about past or future celestial events, it works for those too!

First, the app will ask you which city you want to consult. Then, it will ask if you want to get information for the current day at midnight or manually input a specific date and time. Finally, it will calculate in real time which planets are visible over the horizon and the phase of the moon.

A key feature of this app is its ability to calculate precise timing. Since the "_Ephem_" library works with _UTC+0_, I created a function to handle time zone conversions for users located in different zones.

To build this app, I utilized several libraries:

- **Ephem**: To calculate when planets appear in the sky and the moon phase, given a date and coordinates.
- **Geopy (Nominatim)**: To trace coordinates based on a city name.
- **Pytz & Timezonefinder**: To determine the time zone based on coordinates.
- **Geonamescache**: To validate city names and prevent invalid inputs.

## Project Structure

1. Final_project

   - `location.py`: A specialized module that handles all interactions with the Nominatim API. It is designed with error handling to manage potential timeouts or connection issues.

   - `moon.py`: A focused script that calculates the moon's phase. It converts a raw percentage of illumination into a user-friendly name (e.g., "Full Moon" or "Waning Gibbous").

   - `planets.py`: This module defines how the observer's data is passed to the planetary objects. It iterates through the solar system (Mercury to Saturn) and returns a filtered list of visible bodies.

   - `project.py`: This is the heart of the application. It contains the main function and the essential validators required by the CS50P guidelines. It manages the user flow, from input gathering to final data display. It also contains the function to calculate the different time zones.

   \*`test_project.py`: Following the project requirements, this file contains multiple tests to verify that the date parsing and city validation functions work as expected, including "negative tests" to catch invalid inputs.

## Project Purpose and Motivation

The inspiration for this app came from a desire to build something with real-world utility rather than just a theoretical exercise. When deciding on a theme, I looked at my own hobbies and interests. While I am aware that mobile applications already exist to identify planets in real-time, I wanted to challenge myself by building the foundational logic for a celestial consultation tool.

My goal was to create a reliable engine capable of performing precise astronomical queries for any location and any point in time. I see this as a "Version 1.0" or a prototype. By mastering the core mechanics of planetary positioning and time-zone synchronization, I am laying the groundwork for a more complex ecosystem. This project represents my first step into developing software that connects the user with the cosmos through clean, functional code.

## Installation and Usage:

To run this app, ensure you have Python installed, then:

- Clone the repository.

- Install dependencies: `pip install -r requirements.txt`

- Run the app: `python project.py`

- Follow the on-screen prompts to explore the sky!

## Future Roadmap and Upcoming Features

I designed this application with scalability in mind, and I plan to continue its development beyond the CS50P requirements. Some planned updates include:

- [ ] **Astrological** Integration: I intend to expand the astronomical engine to calculate zodiac signs and horoscopes based on the precise planetary alignment at the time of a user's birth.

- [ ] **Mythological Context**: A future version will include a feature that provides mythological information and lore associated with the planets and constellations visible in the sky at that moment.

- [ ] **Visual Sky Map**: Transitioning from a CLI (Command Line Interface) to a graphical interface that displays a 2D map of the sky.

- [ ] **Internationalization**: Adding support for multiple languages and a broader database of historical astronomical events.
