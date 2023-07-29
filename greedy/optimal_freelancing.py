# Optimal Freelancing
# Write a function that takes in an array of hash tables that give the deadline and payment for some freelancing jobs
# {"deadline": 2, "payment": 1}
# Each job takes one day to complete
# 

# Write a function that returns the maximum possible profit 

def optimal_profit(jobs):
    jobs.sort(key= lambda job: job['payment'], reverse=True)
    schedule = [0] * 7
    for job in jobs:
        deadline = job['deadline'] - 1
        deadline = min(deadline, 6)
        if schedule[deadline] == 0:
            schedule[deadline] = job['payment']
        elif schedule[deadline] != 0 and 0 in schedule[:deadline+1]:
            for i in reversed(range(len(schedule[:deadline]))):
                if schedule[i] == 0:
                    schedule[i] = job['payment']

    return sum(schedule)

# Optimal Time Complexity: O(n log(N))
# Optimal Space Complexity: O(1)

if __name__ == "__main__":
    job = [
        {
            "deadline": 1,
            "payment": 2
        },
        {
            "deadline": 3,
            "payment": 1
        },
        {
            "deadline": 1,
            "payment": 1
        },
        {
            "deadline": 9,
            "payment": 2
        }
    ]

    optimal_profit(jobs)