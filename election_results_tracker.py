import sqlite3

def display_polling_unit_results():
    # Connect to the database
    conn = sqlite3.connect('bincom_test.sql')
    cursor = conn.cursor()

    # Get polling unit ID from user
    polling_unit_id = input("Enter Polling Unit Unique ID: ")

    # Query to fetch results
    query = """
    SELECT apr.party_abbreviation, apr.party_score
    FROM polling_unit pu
    JOIN announced_pu_results apr ON pu.uniqueid = apr.polling_unit_uniqueid
    WHERE pu.uniqueid = ?
    """
    cursor.execute(query, (polling_unit_id,))
    results = cursor.fetchall()

    # Display results
    if results:
        print(f"Results for Polling Unit ID {polling_unit_id}:")
        for result in results:
            print(f"Party: {result[0]}, Score: {result[1]}")
    else:
        print("No results found for this polling unit.")

    # Close connection
    conn.close()

# Run the function
display_polling_unit_results()


import sqlite3

def display_lga_total_results():
    # Connect to the database
    conn = sqlite3.connect('bincom_test.sql') 
    cursor = conn.cursor()

    # Get LGA ID from user
    lga_id = input("Enter Local Government Area (LGA) ID: ")

    # Query to fetch and sum results
    query = """
    SELECT apr.party_abbreviation, SUM(apr.party_score) as total_score
    FROM polling_unit pu
    JOIN announced_pu_results apr ON pu.uniqueid = apr.polling_unit_uniqueid
    WHERE pu.lga_id = ?
    GROUP BY apr.party_abbreviation
    """
    cursor.execute(query, (lga_id,))
    results = cursor.fetchall()

    # Display results
    if results:
        print(f"Total Results for LGA ID {lga_id}:")
        for result in results:
            print(f"Party: {result[0]}, Total Score: {result[1]}")
    else:
        print("No results found for this LGA.")

    # Close connection
    conn.close()

# Run the function
display_lga_total_results()

#question3
def insert_polling_unit_results():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Ask user for the polling unit ID
    polling_unit_id = input("Enter the Polling Unit Unique ID: ")

    # Ask for the number of parties and their scores
    party_scores = {}
    num_parties = int(input("Enter the number of parties: "))
    for i in range(num_parties):
        party = input(f"Enter party abbreviation for party {i + 1}: ")
        score = int(input(f"Enter score for {party}: "))
        party_scores[party] = score

    # Insert the results into the database
    for party, score in party_scores.items():
        query = """
        INSERT INTO announced_pu_results (polling_unit_uniqueid, party_abbreviation, party_score)
        VALUES (?, ?, ?)
        """
        cursor.execute(query, (polling_unit_id, party, score))

    # Commit the transaction
    conn.commit()
    print("Results inserted successfully.")

    conn.close()

# Run the function
insert_polling_unit_results()


