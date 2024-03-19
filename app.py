import json

from ufc import get_event

def main():
    # Get event data
    event_data = get_event('UFC 4')

    # Write event data to a JSON file
    with open('event_data.json', 'w') as json_file:
        json.dump(event_data, json_file, indent=4)

if __name__ == "__main__":
    main()
    
    
    
    
# import json
# from ufc import get_fighter

# def main():
#     # Get fighter data
#     fighter_data = get_fighter('Jon Jones')

#     # Write fighter data to a JSON file
#     with open('fighter_data.json', 'w') as json_file:
#         json.dump(fighter_data, json_file, indent=4)

# if __name__ == "__main__":
#     main()

