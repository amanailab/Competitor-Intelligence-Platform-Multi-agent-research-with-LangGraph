
from utils.agent_executor import execute_agent


attempt_count = 0


def sample_agent():

    global attempt_count

    attempt_count += 1

    print(f"Agent execution attempt: {attempt_count}")

    if attempt_count < 3:
        raise TimeoutError("Temporary connection timeout")

    return "Agent completed successfully!"


result = execute_agent(sample_agent)

print("\nFINAL RESULT:")
print(result)
