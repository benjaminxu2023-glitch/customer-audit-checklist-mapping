# Supplier Audit Checklist Auto-Fill Tool

from datetime import datetime

# Get the current date and time in the specified format
current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

# Function to get current user login
def get_current_user():
    return 'benjaminxu2023-glitch'

if __name__ == '__main__':
    print(f'Current Date and Time (UTC - YYYY-MM-DD HH:MM:SS formatted): {current_time}')
    print(f"Current User's Login: {get_current_user()}")