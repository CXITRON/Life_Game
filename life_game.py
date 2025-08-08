class LifeGame:
    def __init__(self):
        # Initialize player stats
        self.stats = {
            'health': 100,
            'happiness': 50,
            'money': 0
        }

        # Define how activities affect stats
        self.activity_effects = {
            'work': {'health': -10, 'happiness': -5, 'money': 100},
            'exercise': {'health': 5, 'happiness': 10, 'money': -10},
            'rest': {'health': 10, 'happiness': 5, 'money': 0},
            'shopping': {'health': 0, 'happiness': 5, 'money': -50},
        }

    def apply_activity(self, activity: str):
        """Apply an activity to update player stats."""
        if activity not in self.activity_effects:
            raise ValueError(f"Unknown activity: {activity}")

        effects = self.activity_effects[activity]
        for stat, change in effects.items():
            self.stats[stat] += change

        # Clamp stats between 0 and 100 where appropriate
        for stat in ('health', 'happiness'):
            self.stats[stat] = max(0, min(100, self.stats[stat]))

        return self.stats


def main():
    game = LifeGame()
    print("Welcome to Life Game! Enter activities: work, exercise, rest, shopping or quit.")
    while True:
        activity = input("What did you do today? ").strip().lower()
        if activity == 'quit':
            print("Goodbye!")
            break
        try:
            stats = game.apply_activity(activity)
            print(f"Updated stats: {stats}")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
