# Enterprise Python Project

Repository URL: https://github.com/thatdudetebo/Enterprise-Python-Project

This project is a Python-based enterprise learning system developed as part of the ITEPA3 module. It models a simplified academic registration environment where learners can register for courses, manage assessments, and generate support tickets. The project also demonstrates enterprise software design principles through object-oriented modeling and common software design patterns.

## Project Overview

The system is designed to simulate an academic registration and monitoring workflow for a training or university environment. It includes:

- Learner records
- Course registration logic
- Capacity validation
- Assessment scoring
- Support ticket creation and resolution
- Monitoring and performance tracking
- Threaded processing for concurrent registration requests

The project highlights practical enterprise Python development practices and focuses on clean design, modularity, and testability.

## Features

- Learner registration management
- Course creation with capacity limits
- Registration success and failure handling
- Duplicate registration prevention
- Assessment score recording and validation
- Support ticket handling for academic and technical issues
- Strategy pattern for grading classification
- Factory pattern for ticket creation
- Singleton pattern for application configuration
- Concurrent registration processing with thread-safe logic
- Monitoring and reporting of system performance events

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Threading
- Unit testing with unittest
- Design patterns:
  - Singleton
  - Factory
  - Strategy

## Project Structure

```text
Enterprise-Python-Project/
├── main.py
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── monitoring/
│   │   ├── __init__.py
│   │   └── bugzot.py
│   ├── patterns/
│   │   ├── __init__.py
│   │   ├── grading_strategies.py
│   │   └── ticket_factory.py
│   └── services/
│       ├── __init__.py
│       └── registration_engine.py
├── tests/
│   ├── __init__.py
│   └── test_enterprise_system.py
└── README.md
```

## Main Modules

### `main.py`
The entry point of the project. It demonstrates the functionality of the system by creating learners, courses, registrations, tickets, and assessment outputs.

### `src/models.py`
Defines the core domain entities:
- `Learner`
- `Course`
- `Registration`
- `Assessment`
- `SupportTicket`

### `src/services/registration_engine.py`
Handles registration logic, validation, duplicate checks, capacity constraints, and concurrent processing.

### `src/patterns/ticket_factory.py`
Creates different ticket types using the Factory design pattern.

### `src/patterns/grading_strategies.py`
Implements the Strategy pattern for classifying assessment results.

### `src/monitoring/bugzot.py`
Tracks key system metrics and generates reports for monitoring and system analysis.

### `tests/test_enterprise_system.py`
Contains unit tests validating:
- singleton behavior
- ticket creation
- grading logic
- concurrent registration processing
- monitoring output

## How It Works

The application models a learning system where:

1. A learner is created with a unique ID, name, and email.
2. A course is created with a course ID, title, and capacity.
3. A registration request is processed to validate:
   - learner information
   - duplicate registration attempts
   - course availability
4. Successful registrations are added to the learner and course records.
5. Assessment results are validated and recorded.
6. Support tickets are generated for academic or technical issues.
7. Monitoring logs track events and system performance.

## Running the Project

1. Clone the repository:
```bash
git clone https://github.com/thatdudetebo/Enterprise-Python-Project.git
```

2. Navigate to the project folder:
```bash
cd Enterprise-Python-Project
```

3. Run the project:
```bash
python main.py
```

## Running the Tests

```bash
python -m unittest discover -s tests
```

## Academic Context

This project was developed as an academic assignment for the ITEPA3 module and is intended to demonstrate:

- enterprise application modeling
- Python software design
- object-oriented programming
- concurrency and validation logic
- monitoring and reporting
- software design patterns in real-world problem solving

## Conclusion

This project is a practical demonstration of enterprise system design using Python. It shows how software engineering principles can be applied to solve real academic and institutional problems in a structured, maintainable, and testable way.

## License

This project is intended for academic learning and coursework purposes.
