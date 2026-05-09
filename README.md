# AirTicketPrototypeTesting

An airline ticketing prototype project with a Java codebase and a Streamlit tutor app that explains how the reservation logic works.

## What This Project Is About

This repository started as a Java Eclipse prototype for modeling passengers, tickets, seats, and seating-plan behavior. It now also includes a Streamlit tutor app that turns the same ideas into an interactive lesson, helping users understand pricing, discount rules, seat assignment, and testing-oriented thinking.

This is a **Java OOP and testing project with an AI tutor style Streamlit app**.

## What The Tutor App Teaches

- how business and economy ticket pricing differs
- how staff discounts affect totals
- how seat assignment works when preferred seats are not available
- how to think about edge cases the way a tester would

## Project Structure

- `app.py` - Streamlit tutor app
- `requirements.txt` - Python dependencies for the tutor app
- `com/cc/airline/...` - main airline source files
- `src/rojina/saberi/airticket/tests/SeatingPlanTest.java` - test class
- `META-INF/` - manifest metadata
- Eclipse project files: `.project`, `.classpath`, `.settings/`

## Run The Streamlit App

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Open The Java Project

Import into Eclipse to inspect or run the original Java prototype and test scaffold.

## Tech Stack

- Java
- Python
- Streamlit
- Eclipse
- JUnit-style testing structure
