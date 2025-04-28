import random

# Name parts for different categories
male_first_parts = ["Ael", "Aer", "Ar", "Be", "Cal", "Da", "Ela", "Faer", "Gal", "Hael", "Ith", "Ja", "Kael", "Lae", "Maer"]
female_first_parts = ["Saer", "Shae", "Tael", "Tha", "Ulor", "Vael", "Waer", "Xa", "Ya", "Zael", "Lira", "Mira", "Nysa", "Sira", "Vela"]
creature_first_parts = ["Gor", "Zar", "Thra", "Mog", "Grim", "Vor", "Drak", "Brak", "Krag", "Urth", "Zhul", "Snag", "Thrall"]

middle_parts = ["dor", "drin", "thas", "lith", "mir", "nor", "ril", "sor", "ther", "vor", "wyn", "zor", "bryn", "car", "dan"]
last_parts = ["a", "e", "i", "o", "u", "ae", "ia", "ai", "ea", "io"]

def generate_name(category):
    """Generates a fantasy name based on the selected category."""
    if category == "male":
        first = random.choice(male_first_parts)
    elif category == "female":
        first = random.choice(female_first_parts)
    elif category == "creature":
        first = random.choice(creature_first_parts)
    else:
        first = random.choice(male_first_parts + female_first_parts + creature_first_parts)

    middle = random.choice(middle_parts)
    last = random.choice(last_parts)
    return first + middle + last

def main():
    print("🌟 Welcome to the Fantasy Name Generator!")
    print("-----------------------------------------")
    
    while True:
        print("\nChoose a category:")
        print("1. Male Names 👦")
        print("2. Female Names 👧")
        print("3. Creature Names 🐉")
        print("Q. Quit ❌")
        
        choice = input("Enter choice (1/2/3 or Q): ").lower()
        
        if choice == 'q':
            print("👋 Goodbye! Happy naming!")
            break
        
        if choice not in ['1', '2', '3']:
            print("❌ Invalid choice. Please select 1, 2, 3, or Q.")
            continue
        
        try:
            number = int(input("How many names would you like to generate? "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue
        
        if choice == '1':
            category = "male"
        elif choice == '2':
            category = "female"
        else:
            category = "creature"
        
        print("\n✨ Your Fantasy Names:")
        for _ in range(number):
            print(f"- {generate_name(category)}")

if __name__ == "__main__":
    main()
