from utils.retry import retry_agent


def execute_agent(agent_function, *args, **kwargs):

    @retry_agent(max_attempts=3)
    def run():
        return agent_function(*args, **kwargs)

    try:
        return {
            "success": True,
            "result": run(),
            "error": None
        }

    except Exception as error:
        return {
            "success": False,
            "result": None,
            "error": str(error)
        }