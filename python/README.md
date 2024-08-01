# Task Manager Application

## Overview

This project is a basic Task Manager application that helps users manage their to-do tasks. The application includes features such as user registration, login, task creation, viewing, updating, and deletion. It is built using Python and utilizes a simple SQLite database to store user credentials and tasks.

## Features

1. **User Registration**: Users can register with a unique username and password.
2. **User Login**: Registered users can log in to the application using their credentials.
3. **Create Task**: Users can create new tasks by providing a title and description.
4. **View Tasks**: Users can view a list of their created tasks.
5. **Update Task**: Users can update the title and description of their existing tasks.
6. **Delete Task**: Users can delete their tasks when they are completed.

## Requirements

- Python 3.8 or higher
- `pip` package manager


# Python Crew

Welcome to the Python Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
poetry lock
```
```bash
poetry install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/python/config/agents.yaml` to define your agents
- Modify `src/python/config/tasks.yaml` to define your tasks
- Modify `src/python/crew.py` to add your own logic, tools and specific args
- Modify `src/python/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
poetry run python
```

This command initializes the python Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The python Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Python Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.



