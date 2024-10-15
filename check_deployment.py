import os

def check_environment_variables():
    print("Checking deployment configuration...")
    
    # Check if DATABASE_URL is set
    if 'DATABASE_URL' in os.environ:
        print("DATABASE_URL is set in the environment variables.")
    else:
        print("WARNING: DATABASE_URL is not set in the environment variables.")

    # Check other relevant environment variables
    for var in ['PGPORT', 'PGHOST', 'PGUSER', 'PGDATABASE', 'PORT']:
        if var in os.environ:
            print(f"{var} is set in the environment variables.")
        else:
            print(f"WARNING: {var} is not set in the environment variables.")

    # Check if FLASK_ENV is set to production
    if os.environ.get('FLASK_ENV') == 'production':
        print("FLASK_ENV is correctly set to production.")
    else:
        print("WARNING: FLASK_ENV is not set to production.")

    # Check if running on Replit
    if os.environ.get('REPLIT') == 'true':
        print("Running on Replit environment.")
    else:
        print("Not running on Replit environment.")

if __name__ == "__main__":
    check_environment_variables()
