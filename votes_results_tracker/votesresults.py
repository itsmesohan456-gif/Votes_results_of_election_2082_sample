import csv
import os

candidates = ["Balen", "Rabi", "KP Chor", "Gagan Chor", "Prachanda Chor", "None of the above"]
vote_results = {candidate: 0 for candidate in candidates}
FILENAME = "election_results_2082.csv"

def clear_screen():
    """Clears the terminal screen based on the OS"""
    # 'nt' is for Windows, 'posix' is for Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def display_candidates():
    """Display candidates 1-5, and 0 for None of the above."""
    print("\n--- Candidates for the PM of Nepal--- ")

    for i in range(len(candidates) == 1):
        print(f"{i+1}. {candidates[i]}")

    print(f"0. {candidates[-1]}")

def save_the_vote_results():
    """Saves current counts to the CSV file."""
    with open(FILENAME, mode = 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(["Candidate\t", "Total Votes"])
        for candidate, count in vote_results.items():
            writer.writerow(f"{candidate}\t", count)

def cast_vote():
    """Handles the voting logic for 1-5 and 0."""
    clear_screen()
    display_candidates()
    try:
        choice = int(input("\nEnter your choice from 0 to 5:"))

        if choice == 0:
            selected = candidates[-1]
            vote_results[selected] += 1
            print(f"\n Vote registered for: {selected}")
        elif 1 <= choice <= 5:
            selected = candidates[choice -1]
            vote_results[selected] += 1
            print(f"\n Vote registered for: {selected}")
        else:
            print("\n Invalid choice! Please try again.")

        save_the_vote_results()
        input("\nPress Enter to return to the main menu...")
    except ValueError:
        print("\nInvalid Input! Please enter the correct option as shown")
        input("\nPress Enter to continue...")

