sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []
while sandwich_orders:
    temp = sandwich_orders.pop()
    print(f"I made your {temp} sandwich")
    finished_sandwiches.append(temp)

print("\nSandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")