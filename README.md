# AirBnB Clone - The Console

## Overview
Welcome to the AirBnB clone project. This is the first step towards building our first full web application. The project focuses on creating a command interpreter to manage the clone AirBnB objects, which will be the foundation for further developments including HTML/CSS templating, database storage, API, and front-end integration.

## Team Members
- Andrew Pabie
- Desmond Karani

## Project Duration
- Start Date: January 8, 2024
- End Date: January 15, 2024

## Features
- A parent class `BaseModel` for initialization, serialization, and deserialization of instances.
- Serialization/Deserialization flow: Instance <-> Dictionary <-> JSON string <-> file.
- Classes for AirBnB (User, State, City, Place) inheriting from `BaseModel`.
- A file storage engine to manage data persistence.
- Comprehensive unit tests for validation of all functionalities.

## Technologies Used
- Python 3.8.5
- unittest module for testing

## Setup and Installation
1. Clone the repository to your local machine.
2. Navigate to the project directory.

```bash
cd path/to/AirBnB_clone
```

3. Run the console in interactive mode:

```bash
./console.py
```

4. For non-interactive mode, use:

```bash
echo "your-command-here" | ./console.py
```

## Usage
- `help`: List available commands.
- `quit`: Exit the console.
- `create`: Create a new object (e.g., `create User`).
- `show`: Retrieve an object (e.g., `show User user_id`).
- `destroy`: Destroy an object (e.g., `destroy User user_id`).
- `update`: Update attributes of an object (e.g., `update User user_id email "user@example.com"`).

## Testing
- Execute all tests with:

```bash
python3 -m unittest discover tests
```

- Test file by file:

```bash
python3 -m unittest tests/test_models/test_base_model.py
```

## Contributions
This project is part of our software engineering training program. Contributions are not accepted.

## Authors
- Andrew Pabie
- Desmond Karani

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- Guillaume, our project coordinator
- Holberton School for providing the learning platform
