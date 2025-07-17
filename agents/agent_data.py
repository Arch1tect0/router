def data_retrieval_agent(task):
    print("[Data Retrieval Agent] Task:", task)
    if "sales data" in task:
        return "Sales data from Jan 1 to Feb 1: [1234, 5678, 91011]"
    return "Data not found."
