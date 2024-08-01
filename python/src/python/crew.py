from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class PythonCrew():
    """Python crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def project_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['project__manager'],
            verbose=True
        )

    @agent
    def python_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['python_developer'],
            verbose=True
        )

    @agent
    def python_documentation_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['python_documentation_specialist'],
            verbose=True
        )

    @agent
    def python_quality_assurance_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['python_quality_assurance_analyst'],
            verbose=True
        )

    @task
    def requirements_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['requirements_analysis_task'],
            agent=self.project_manager()
        )

    @task
    def python_development_task(self) -> Task:
        return Task(
            config=self.tasks_config['python_development_task'],
            agent=self.python_developer(),
            output_file='app.py'
        )

    @task
    def testing_and_quality_assurance_task(self) -> Task:
        return Task(
            config=self.tasks_config['testing_and_quality_assurance_task'],
            agent=self.python_quality_assurance_analyst(),
            output_file='code_review.md'
        )

    @task
    def documentation_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['documentation_creation_task'],
            agent=self.python_documentation_specialist(),
            output_file='README.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Python crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=2,
            # process=Process.hierarchical, # In case you want to use hierarchical process
        )

# Running the crew
def run():
    inputs = {
        'description': """
        The application is a basic Task Manager that helps users to manage their to-do tasks. 
        It includes the following features:
        1. User Registration: Users can register with a unique username and password.
        2. User Login: Registered users can log in to the application using their credentials.
        3. Create Task: Users can create new tasks by providing a title and description.
        4. View Tasks: Users can view a list of their created tasks.
        5. Update Task: Users can update the title and description of their existing tasks.
        6. Delete Task: Users can delete their tasks when they are completed.
        The application is built using Python and utilizes a simple SQLite database to store user credentials and tasks.
        """
    }
    PythonCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()