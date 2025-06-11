from datetime import datetime
import sys
# log_string = """
# 09:20 Introduction
# 11:00 Exercises
# 11:15 Break
# 11:35 Numbers and strings
# 12:30 Lunch Break
# 13:30 Exercises
# 14:10 Solutions
# 14:30 Break
# 14:40 Lists
# 15:40 Exercises
# 17:00 Solutions
# 17:30 End

# 09:30 Lists and Tuples
# 10:30 Break
# 10:50 Exercises
# 12:00 Solutions
# 12:30 Dictionaries
# 12:45 Lunch Break
# 14:15 Exercises
# 16:00 Solutions
# 16:15 Break
# 16:30 Functions
# 17:00 Exercises
# 17:30 End
# """
def parse_log_file(file_path):
    """
    Reads the log content from a specified file path.
    """
    try:
        with open(file_path, 'r') as f:
            log_content = f.read()
        return log_content
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def parse_log(log_string):
    categories_total_time = {}
    parsed_log_output = []
    lines = log_string.strip().split('\n')
    
    current_day_activities = []
    for line in lines:
        if not line.strip():  
            if current_day_activities:
                process_day_activities(current_day_activities, categories_total_time, parsed_log_output)
                parsed_log_output.append("") 
                current_day_activities = []
            continue
        current_day_activities.append(line)
    
    
    if current_day_activities:
        process_day_activities(current_day_activities, categories_total_time, parsed_log_output)

    return categories_total_time, parsed_log_output

def process_day_activities(activities, categories_total_time, parsed_log_output):
    for i in range(len(activities) - 1):
        start_time_str, activity_name = activities[i].split(' ', 1)
        end_time_str = activities[i+1].split(' ', 1)[0]

            
        start_time = datetime.strptime(start_time_str, "%H:%M")
        end_time = datetime.strptime(end_time_str, "%H:%M")
        
        duration = (end_time - start_time).total_seconds() / 60  # Duration in minutes
        
        # categories_total_time.setdefault(activity_name.strip(), 0)
        categories_total_time[activity_name.strip()] += duration
        
        parsed_log_output.append(f"{start_time_str}-{end_time_str} {activity_name.strip()}")


if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Usage: python your_script_name.py <path_to_log_file>")
        sys.exit(1) 

    categories_total_time = {}
    log_file_path = sys.argv[1] 
    log_content = parse_log_file(log_file_path)
    
    time_spent, formatted_log = parse_log(log_content)

    # Print the formatted log first
    for line in formatted_log:
        print(line)

    # Calculate total time for the summary
    total_time_minutes = sum(time_spent.values())

    # Prepare the summary output
    summary_output = []
    for category, minutes in sorted(time_spent.items()):
        percentage = (minutes / total_time_minutes) * 100 if total_time_minutes > 0 else 0
        summary_output.append(f"{category.ljust(26)}{int(minutes)} minutes    {int(percentage)}%")

    # Print the summary
    print("\n\n")
    for item in summary_output:
        print(item)