roles = ["Researcher", "Coder", "Critic", "Manager"]
tasks = [
    "Gather data sources.",
    "Write data processing code.",
    "Review code for errors.",
    "Coordinate report delivery."
]
for role, task in zip(roles, tasks):
    print(f"{role} assigned to: {task}")
