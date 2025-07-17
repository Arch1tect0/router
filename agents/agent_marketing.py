def marketing_agent(task, supervisor):
    print("[Marketing Agent] Received task:", task)

    # Needs data help
    if "sales data" in task:
        print("[Marketing] Requesting data from data agent...")
        result = supervisor.agents["data"]("Get sales data from Jan 1 to Feb 1")
        return f"Marketing Analysis based on: {result}"
    
    return "Marketing task completed."
