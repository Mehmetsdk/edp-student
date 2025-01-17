from student import Student
from embassy import Embassy
from events.embassy_appointment_request_event import EmbassyAppointmentRequestEvent
from events.appointment_confirmation_event import AppointmentConfirmationEvent

class BaseAgent:
    """Base class for all agents."""
    def __init__(self, name):
        self.name = name

    def handle_request(self, request_type, request_detail):
        raise NotImplementedError("This method should be implemented by subclasses.")


class AdvisorAgent(BaseAgent):
    """Agent providing personalized advice on courses or programs."""
    def handle_request(self, request_type, request_detail):
        if request_type == "course_recommendation":
            return f"AdvisorAgent: Based on your interest in {request_detail}, I recommend Course XYZ."
        elif request_type == "program_advice":
            return f"AdvisorAgent: Based on your goals, I recommend the ABC Program."
        else:
            return "AdvisorAgent: I could not process your request."


class EventCoordinatorAgent(BaseAgent):
    """Agent suggesting upcoming events and activities."""
    def handle_request(self, request_type, request_detail):
        if request_type == "event_suggestion":
            return f"EventCoordinatorAgent: Here are some events related to {request_detail}: Hackathon 2025, Workshop on AI."
        elif request_type == "event_schedule":
            return f"EventCoordinatorAgent: The event schedule for {request_detail} is available online."
        else:
            return "EventCoordinatorAgent: I could not process your request."


class MentorAgent(BaseAgent):
    """Agent matching students with mentors."""
    def handle_request(self, request_type, request_detail):
        if request_type == "mentor_match":
            return f"MentorAgent: Based on your interest in {request_detail}, I have matched you with Dr. Smith."
        elif request_type == "mentor_advice":
            return f"MentorAgent: Here is some advice from your mentor about {request_detail}: Keep learning and stay curious."
        else:
            return "MentorAgent: I could not process your request."


class ResourceLocatorAgent(BaseAgent):
    """Agent helping students find relevant academic or career resources."""
    def handle_request(self, request_type, request_detail):
        if request_type == "academic_resources":
            return f"ResourceLocatorAgent: Here are some academic resources on {request_detail}: Online Library, Research Papers."
        elif request_type == "career_resources":
            return f"ResourceLocatorAgent: Here are some career development resources: Job Portals, Resume Templates."
        else:
            return "ResourceLocatorAgent: I could not process your request."


class AgentManager:
    """Manages multiple agents and delegates requests to the appropriate one."""
    def __init__(self):
        self.agents = {
            "advisor": AdvisorAgent("Advisor"),
            "event_coordinator": EventCoordinatorAgent("EventCoordinator"),
            "mentor": MentorAgent("Mentor"),
            "resource_locator": ResourceLocatorAgent("ResourceLocator"),
        }

    def handle_request(self, agent_type, request_type, request_detail):
        agent = self.agents.get(agent_type)
        if not agent:
            return f"No agent found for type: {agent_type}"
        return agent.handle_request(request_type, request_detail)


if __name__ == "__main__":
    manager = AgentManager()

    # Example requests with more specific request types and details
    print(manager.handle_request("advisor", "course_recommendation", "machine learning"))
    print(manager.handle_request("event_coordinator", "event_suggestion", "technology"))
    print(manager.handle_request("mentor", "mentor_match", "data science"))
    print(manager.handle_request("resource_locator", "career_resources", "career development"))
    print(manager.handle_request("event_coordinator", "event_schedule", "Hackathon 2025"))
    print(manager.handle_request("mentor", "mentor_advice", "leadership"))

event_queue = []

# Example Usage
student1 = Student("Piotr1", "Brudny", '1.02.1984', 'Ankara', '5435345345', 'ED4234323', event_queue)
polish_embassy = Embassy('Polish Embassy', 'Ankara, Harika 10', '343242344', 'polishembassy@gov.tr', event_queue)


student1.ask_for_embassy_appointment('10.12.2024')


while event_queue: # it runs as long as there is an event in the list
    event = event_queue.pop(0) # takes the event from the top

    # matches events with the handler
    if isinstance(event, EmbassyAppointmentRequestEvent):
        polish_embassy.handle_appointment_request(event) 
    elif isinstance(event, AppointmentConfirmationEvent):
        student1.handle_appointment_confirmation(event)

    
    