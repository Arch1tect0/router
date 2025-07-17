from router import Supervisor

if __name__ == "__main__":
    supervisor = Supervisor()
    query = "Marketing: Can you get me the sales data from Jan 1 to Feb 1?"
    response = supervisor.route_task(query)
    print("Final Output:", response)

